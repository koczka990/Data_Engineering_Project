from pymongo import MongoClient
import json
import os

# Initialization 
insert_error_cnt =0
insert_error_record = {}
# Creating a client
client = MongoClient('mongodb://localhost:27017/')
# Create database
db = client.get_database('test')
# Create a document into a collection
collection = db['collection']
# set source folder
file_path = 'reddit_data/corpus-webis-tldr-17.json'
# open each txt file
with open(file_path, 'r') as file:
        # get each line in text
        for obj in file:
                # load the read text into json onject
                reddit = json.loads(obj)
                print(reddit)
                # insert into db
                result = collection.insert_one(reddit)
                if result.acknowledged:
                     print("Insertion successful. Inserted document ID:", result.inserted_id)
                else:
                     insert_error_cnt += 1
                     err_msg = str(result.write_error)
                     print("Insertion failed:", err_msg)
                     insert_error_record[reddit['id']] = err_msg
# Print total number of data in the collection
document_count = collection.count_documents({})
print("Number of documents:", document_count)
# Print total errors
print("Total insertion error: ", insert_error_cnt)
print(insert_error_record)
