import requests

api_url = 'http://localhost:5000/api'
api_token = '123'

num_of_values = 10


def get_api_value():
    """
    Makes a GET request to the server

    :return: Integer value
    """

    try:

        headers = {'Authorization': f'Token {api_token}'}
        response = requests.get(api_url, headers=headers)
        response_data = response.json()
        return response_data['value']

    except Exception as e:

        print(f'Something went wrong in get_api_value(): {e}')
        return None


def get_mean_value(num_of_values):
    """
    Function gets values and calculates the mean.

    :param num_of_values: Number of values we want to get the mean from
    :return: The mean of the values
    """
    try:
        values = [get_api_value() for _ in range(num_of_values)]
        mean = sum(values) / len(values)
        return mean
    except Exception as e:
        print(f'Error in get_mean_value(): {e}')
        return None


if __name__ == '__main__':
    print(f'Mean value: {get_mean_value(num_of_values)}')
