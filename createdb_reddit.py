from pymongo import MongoClient
import json
import os
# Creating a client
client = MongoClient()
# Create database
db = client.get_database('reddit')
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
                # insert into db
                result = collection.insert_one(reddit)
# Print total number of data in the collection
document_count = collection.count_documents({})
print("Number of documents:", document_count)
