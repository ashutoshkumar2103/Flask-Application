# # Importing Flask to create a web application

from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

# defining the database to use
# The 'test' database is a placeholder; you can change it to your desired database name 
db = client.flaskdata

collection = db['flask_tutorial']

# # Initializing the Flask application
app = Flask(__name__)

@app.route('/submit' , methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data submitted successfully!'
    
@app.route('/data')
def data():
    # Fetching all documents from the collection
    data = collection.find()
    
    data = list(data)  # Convert cursor to list for easier handling

    for item in data:
        print(item)

        del item['_id']  # Remove the MongoDB ObjectId field for cleaner output 

    data = {
        'data': data
    }

    print('Data fetched successfully!')
    return data

# # Checking if the script is run directly
# # This allows the app to be run with the command `python app.py` and it will start the Flask development server
if __name__ == '__main__':
#     # Running the Flask application
    app.run(host='192.168.1.7', port=9000, debug=True)