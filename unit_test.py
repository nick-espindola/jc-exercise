from pathlib import Path
import unittest
import json

from flask.wrappers import Response
from test2 import app
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/manage_file"



    def test_1_get_all_files(self):
        tester = app.test_client(self)
        response = tester.post('/manage_file', data=json.dumps(dict({"action":"download"})), content_type='application/json')
        resp = requests.get(self.URL)
        self.assertEqual(Response.status_code, 200)
        print("Test 1 completed")

    def test_2_get_all_files(self):
        tester = app.test_client(self)
        response = tester.post('/manage_file', data=json.dumps(dict({"action":"read"})), content_type='application/json')
        resp = requests.get(self.URL)
        self.assertEqual(Response.status_code, 201)
        print("Test 2 completed")

    def test_3_get_all_files(self):
        path = Path('sample.txt')
        assert path.is_file()
        print("Test 3 completed")


    if __name__ == "__main__":
        unittest.main()
        
        #tester.test_2_get_all_todo