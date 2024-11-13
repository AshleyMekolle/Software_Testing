# test_app.py
import unittest

# imports the instance of the object app from the class app
from app import app 

# Defines a new class called testapp
class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the response JSON matches the expected message
        expected_response = {"message": "Hello level 400 FET, Quality Assurance!"}
        self.assertEqual(response.get_json(), expected_response)

if __name__ == '__main__':
    unittest.main()


