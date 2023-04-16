import unittest
from unittest.mock import patch
import requests


import app
import server



class TestApi(unittest.TestCase):

    def test_valid_token(self):
        headers = {'Authorization': f'Token 123'}
        response = requests.get('http://localhost:5000/api', headers=headers)
        self.assertEqual(response.status_code, 200)



    def test_invalid_token(self):
        headers = {'Authorization': f'Token'}
        response = requests.get('http://localhost:5000/api', headers=headers)
        self.assertEqual(response.status_code, 401)
    


    @patch('app.get_api_value')
    def test_get_mean_value(self, mock_api_value):
        """
        Test if calulation of mean is working correctly
        """
        mock_api_value.side_effect = [1,1,1,1,1,3,3,3,3,3]
        result = app.get_mean_value(10)
        self.assertEqual(result, 2) 

   



if __name__ == '__main__':
    unittest.main()

  