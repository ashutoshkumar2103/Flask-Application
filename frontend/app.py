# importing necessary libraries 

from flask import Flask, render_template, request, redirect, url_for
import datetime
import requests

BACKEND_URL = 'http://127.0.0.1:2000'

app = Flask(__name__)

@app.route('/')
def home():
    day_of_the_week = datetime.datetime.now().strftime('%A')
    print("Today is:", day_of_the_week)

    return render_template('index.html', dayOfTheWeek=day_of_the_week)

# Submitting data to the backend
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return redirect(url_for('success'))

# Success route to handle redirection after form submission
@app.route('/success')
def success():
    return ("Data submitted successfully!")

# Fetching data from the backend to display on the frontend
@app.route('/data')
def data():
    response = requests.get(BACKEND_URL + '/data')
    return response.json()

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=1000, debug=True)
