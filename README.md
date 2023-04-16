# API Test Project

This is a test project for an API that returns a random integer value with a timestamp. The project consists of three files:

- `app.py`: A client script that sends requests to the server and calculates the mean value of the responses.
- `server.py`: A Flask server that responds to requests with a random integer value and a timestamp. The server also checks for a valid authorization token before responding.
- `test_app.py`: A unittest file that tests the functionality of the client and server scripts.

## Requierements

- Python 3.x
- Flask
- requests
