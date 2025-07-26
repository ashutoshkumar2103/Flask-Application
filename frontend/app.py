# # Importing Flask to create a web application

from flask import Flask,render_template, request
from datetime import datetime
import requests

# Backend URL for API calls
BACKEND_URL = 'http://192.168.1.7:9000'

# # Initializing the Flask application
app = Flask(__name__)

# # Defining a route for the home page
@app.route('/')
# # Function to handle requests to the home page
def home():
    day_of_the_week = datetime.now().strftime("%A")
    print("Today is " + day_of_the_week)
    return render_template('index.html', dayOfTheWeek=day_of_the_week)


@app.route('/submit', methods=['POST'])
def submit():
    # Collecting form data from the request
    form_data = dict(request.form)
    
    # Sending a POST request to the backend to submit the data
    requests.post(BACKEND_URL + '/submit', json=form_data)
    
    # Returning the response from the backend
    return 'Data submitted successfully!'

# # This allows the app to be run with the command `python app.py` and it will start the Flask development server
if __name__ == '__main__':
#     # Running the Flask application
    app.run(host='0.0.0.0', port=8000, debug=True)