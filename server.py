import os
import logging
import random
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

os.environ["api_token"] = '123'
TOKEN = os.environ.get('API_TOKEN')



@app.route('/api')
def get_value():
    if request.headers.get('Authorization') != f'Token {TOKEN}':
        
        app.logger.warning('Unauthorized access attempt: %s', request.remote_addr)
        return jsonify({'error': 'Unauthorized access'}), 401

    value = get_random_value()
    timestamp = datetime.utcnow()
    response_data = {'ts': timestamp, 'value': value}
    app.logger.info('API request: %s', response_data)
    return jsonify(response_data)

def get_random_value():
    return random.randint(0, 100)



if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    app.run(debug=True)


