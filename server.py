import os
import logging
import random
from datetime import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Loads Token from credentials.env

load_dotenv(dotenv_path='credentials.env')
TOKEN = os.environ.get('api_token')


# Creates app and sets up the logger

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



@app.route('/api')
def get_value():
    """
    Function checks if authorization token is valid or not.
    If Authorization is valid it returns a value with timestamp
    
    :return: JSON Object containing timestamp and int-value
    """

    if request.headers.get('Authorization') != f'Token {TOKEN}':
        app.logger.warning('Unauthorized access attempt: %s', request.remote_addr)
        return jsonify({'error': 'Unauthorized access'}), 401
        

    value = get_random_value()
    timestamp = datetime.utcnow()
    response_data = {'ts': timestamp, 'value': value}
    app.logger.info('API request successful')
    return jsonify(response_data)

def get_random_value():
    """
    :return: Random integer between 0 and 100
    """
    return random.randint(0, 100)



if __name__ == '__main__':
    app.run()


