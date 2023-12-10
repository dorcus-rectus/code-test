import json
import unittest
#from show_item import lambda_handler
from show_item import app

class TestShowItem(unittest.TestCase):

    def test_success(self):
        #event = {'queryStringParameters': {'id': 'test_id'}}
        event = {'queryStringParameters': {'id': '10'}}
        resp = app.lambda_handler(event, None)        
        self.assertEqual(resp['statusCode'], 200)
        body = resp['body']
        data = json.loads(body)
        self.assertEqual(data['id'], '10')
        self.assertEqual(data['item'], 'test')

    def test_missing_id(self):
        event = {}
        resp = app.lambda_handler(event, None)        
        self.assertEqual(resp['statusCode'], 400)

    def test_item_not_found(self):
        event = {'queryStringParameters': {'id': 'invalid_id'}}
        resp = app.lambda_handler(event, None)        
        self.assertEqual(resp['statusCode'], 404)

if __name__ == '__main__':
    unittest.main()