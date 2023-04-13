import requests

api_url = 'http://localhost:5000/api'
api_token = '123'


def get_api_value():
    headers = {'Authorization': f'Token {api_token}'}
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
    return response_data['value']

def get_mean_value(numOfValues):
    values = [get_api_value() for _ in range(numOfValues)]
    mean = sum(values) / len(values)
    return mean

if __name__ == '__main__':
    num_of_values = int(input('How many values do you need?: '))
    print(f'Mean value: {get_mean_value(num_of_values)}')