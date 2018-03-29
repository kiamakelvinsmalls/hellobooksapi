# class of unittests
import unittest
from app import app
from model import Books,books
import json
class HelloBook(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        self.book=[{
                      "book_id":3,
                      "bookname":"life in the hood",
                      "author":"kelvin kiama",
                      "category":"drama,action",
                      "quantity":10,
                      "publication_year":2018
                    },
                    {
                      "bookname":"real niggas do real things",
                      "author":"kelvin kiama",
                      "category":"drama,action",
                      "quantity":40,
                      "publication_year":2018
                    }

                    ]

    def tearDown(self):
        pass
    
    def test_view(self):
        response_get = self.app.get('/api/books')
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(len(books), 2)


    def test_view_one(self):
        response_get = self.app.get('/api/books/1')
        self.assertEqual(response_get.status_code,200)
        self.assertEqual(books[1]['bookname'], 'a niggas life')
        self.assertEqual(books[1]['author'], 'kelvin kiama')

    def test_item_not_exist(self):
        response = self.app.get('/api/book/9')
        self.assertEqual(response.status_code, 404)

    def test_add_book(self):
        response_add = self.app.post('/api/books',
                                 data=json.dumps(self.book[0]),
                                 content_type='application/json')
        self.assertEqual(response_add.status_code, 201)

    def test_update(self):
        response_update = self.app.put("api/books/2",
                                data=json.dumps(self.book[1]),
                                content_type='application/json')
        self.assertEqual(response_update.status_code, 200)
        # self.assertEqual(data[books][2]['quantity'], 30)
      
    def test_delete(self):
        response_delete = self.app.delete('/api/books/2')
        self.assertEqual(response_delete.status_code, 204)

    def test_delete_item_not_exist(self):
        response_delete = self.app.delete('/api/books/9')
        self.assertEqual(response_delete.status_code, 204)
    
if __name__ == "__main__":
    unittest.main()
