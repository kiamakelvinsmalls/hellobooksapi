# class of unittests
import unittest
from index import app
import json
class HelloBook(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        self.book= {
                      "id":2,
                      "bookname":"life in the hood",
                      "author":"kelvin kiama",
                      "category":"drama,action",
                      "quantity":10
                    }


    def tearDown(self):
        pass
    #test for index page
    def test_view(self):
    # creates a test client
        response_get = self.app.get('/books')
        self.assertEqual(response_get.status_code, 200)


    
    
if __name__ == "__main__":
    unittest.main()
