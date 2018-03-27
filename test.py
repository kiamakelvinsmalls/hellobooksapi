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
                      "id":3,
                      "bookname":"life in the hood",
                      "author":"kelvin kiama",
                      "category":"drama,action",
                      "quantity":10
                    }


    def tearDown(self):
        pass
    
    def test_view(self):
        response_get = self.app.get('/api/books')
        self.assertEqual(response_get.status_code, 200)
        data = json.loads(response_get.get_data())
        self.assertEqual(len(data['books']), 3)


    def test_view_one(self):
        response_get = self.app.get('/api/books/1')
        data = json.loads(response_get.get_data())
        self.assertEqual(response_get.status_code,200)
        self.assertEqual(data['books']['bookname'], 'a niggas life')

    def test_add_book(self):
        response_add = self.app.post('/api/books',
                                 data=json.dumps(self.book),
                                 content_type='application/json')
        self.assertEqual(response_add.status_code, 201)

    def test_update(self):
        response_update = self.app.put("api/books/63",
                                data=json.dumps(books),
                                content_type='application/json')
        self.assertEqual(response_update.status_code, 200)
        data = json.loads(response_update.get_data())
        self.assertEqual(data[books][2]['quantity'], 30)
      
    def test_delete(self):
        response_delete = self.app.delete('/api/books/2')
        self.assertEqual(response_delete.status_code, 204)
        response_delete = self.app.delete('/api/books/5')
        self.assertEqual(response_delete.status_code, 404)
    
if __name__ == "__main__":
    unittest.main()
