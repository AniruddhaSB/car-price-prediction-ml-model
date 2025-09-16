import os
from flask import Flask
from datetime import datetime

from modelTraining.buildModel import build_model_using_local_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the current date and time
    current_time = datetime.now()

    # Format the date and time as a string
    # %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %S = Second
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Create the final response string
    response = f'Hello World! The current date and time is: {formatted_time}'

    return response

@app.route('/build_model_locally')
def build_model_locally():
    msg = build_model_using_local_data()
    return msg

# This block must be at the same level of indentation as the import statement and app = Flask(__name__)
if __name__ == '__main__':
    # Get the port from the environment variable, defaulting to 5000 if not found
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)