# To execute this test run python app_test.py on the Terminal
# Reading the defined test you'll see that we should expect
# a successful test, as we are passing 6 and 2 and getting 8 back
# but also a failure, as we'll purposely check a wrong value

from app import app

import os
import json
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):
    # Our first unit test - We are using the unittest
    # library, calling the _add_numbers route from the app
    # passing a pair of numbers, and checking that the
    # returned value, contained on the JSON response, match
    # the sum of those parameters
    def test_sum(self):
        tester = app.test_client(self)
        response = tester.get('/_add_numbers?a=2&b=6', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Check that the result sent is 8: 2+6
        self.assertEqual(json.loads(response.data), {"result": 8})

    def test_sum_with_none_values(self):
        tester = app.test_client(self)
        response = tester.get('/_add_numbers',content_type='application/json')
        self.assertEqual(response.status_code,200)
        #check the result send is 0
        self.assertEqual(json.loads(response.data),{"result":0})

    # This test will purposely fail
    # We are checking that 2+6 is 10
    def test_sum_fail(self):
        tester = app.test_client(self)
        response = tester.get('/_add_numbers?a=-2&b=-6', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": -8})


if __name__ == '__main__':
    unittest.main()