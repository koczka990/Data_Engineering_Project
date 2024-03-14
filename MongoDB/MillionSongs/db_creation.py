from pymongo import MongoClient
import json 
import os
import hdf5_utils as HDF5
import hdf5_getters as GETTERS
import tables
import h5py
import json
import math
import numpy as np



# Get all getters (fields)
getters = [getter for getter in GETTERS.__dict__.keys() if getter.startswith('get_')]

 # Remove special case
getters.remove('get_num_songs')  


def get_song_details(h5, songidx):

    # Initialize an empty dict
    song_dict = {}

    # Iterate over all getters and save it in a dict
    for getter in getters:
        try:
            song_dict[getter[4:]] = getattr(GETTERS, getter)(h5, songidx)
        except AttributeError as e:
            print(e)
            print('Forgot -summary flag? Specified wrong getter?')

    
    return song_dict



def data_type_conversion(song):

    for key, value in song.items():
    
            # Convert np int32 to int
            if isinstance(value, np.int32):
                song[key] = int(value)
                              
            # Convert nparray to list
            if isinstance(value, np.ndarray):
                song[key] = song[key].tolist()
                # Convert byte str in nparray to regular str
                if value.size > 0 and isinstance(value[0], bytes):
                    song[key] = [item.decode('utf-8') for item in value]
            
            # Convert Nan to None
            if isinstance(value, float) and math.isnan(value):
                song[key] = None

            # Decode byte str to regular str
            if isinstance(value, bytes):  # Check if value is a byte string
                song[key] = value.decode('utf-8')  # Decode byte string to regular string
    
    return song


def insert_data(h5file):

    insert_error_cnt = 0
    insert_error_record = {}
    
    # Read aggregate songs' h5file
    h5 = GETTERS.open_h5_file_read(h5file)
    
    # Get the total number of songs in the file
    num_songs = GETTERS.get_num_songs(h5)
    
    for songidx in range(num_songs):
        
        print('Song Index:', songidx)
        # Get each song's data
        song = get_song_details(h5, songidx)
        # Convert data type to prevent MongoDB error and improve readibility
        song = data_type_conversion(song)
        # Insert into db
        result = collection.insert_one(song)
        # Check for insertion errors
        if result.acknowledged:
            print("Insertion successful. Inserted document ID:", result.inserted_id)
        else:
            insert_error_cnt += 1
            err_msg = str(result.write_error)
            print("Insertion failed:", err_msg)
            insert_error_record[song['title']] = err_msg
        
    h5.close()
    print("Total insertion error: ", insert_error_cnt)
    print(insert_error_record)

if __name__ == '__main__':

    
    h5file = 'output.h5'
    
    # Creating a client
    client = MongoClient("mongodb://localhost:27017/")
 
    # Create database
    db = client.get_database('database')

    # Create a document into a collection
    collection = db['collection']

    insert_data(h5file)

    
    # Query the total count of docs
    try:
        document_count = collection.count_documents({})
        print("Number of documents:", document_count)
    except Exception as e:
        print("Error:", e)
        

    client.close()
