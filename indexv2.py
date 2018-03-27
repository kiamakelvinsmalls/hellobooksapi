
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None
@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)
books = [
    {
        "id":1,
        "bookname":"a niggas life",
        "author":"kelvin kiama",
        "category":"drama,action",
        "quantity":10
    },
    {
        "id":2,
        "bookname":"life in the hood",
        "author":"kelvin kiama",
        "category":"drama,action",
        "quantity":10
    },
    {
        "author": "kelvin",
        "bookname": "A NIGGA GO TO DO WHAT HAS TO BE DONE",
        "category": "historical",
        "id": 63,
        "quantity": 18
    }
    ]
class HelloBooksALLAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('idno', type=int, required=True,
                                   help='enter the books id',
                                   location='json')
        self.reqparse.add_argument('bookname', type=str, required=True,
                                   help='No bookname provided',
                                   location='json')
        self.reqparse.add_argument('author', type=str, required=True,
                                   help='No author provided',
                                   location='json')
        self.reqparse.add_argument('category', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('quantity', type=int, default="",
                                    help="quantity of books"
                                   location='json')
        super(HelloBooksAPI, self).__init__()

    def get_book(self):
        return {'books': [marshal(book, book_fields) for book in books]}

    def add_book(self):
        args = self.reqparse.parse_args()
        book = {
            'id': args['id'],
	        'bookname': args['bookname'],
	        'author': args['author'],
	        'category': args['category'],
	        'quantity':args['quantity']
        }
        books.append(book)
        return {'book': marshal(book, book_fields)}, 201

api.add_resource(HelloBooksAPI, '/books', endpoint='books')


class HelloBooksidAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('idno', type=int, required=True,
                                   help='enter the books id',
                                   location='json')
        self.reqparse.add_argument('bookname', type=str, required=True,
                                   help='No bookname provided',
                                   location='json')
        self.reqparse.add_argument('author', type=str, required=True,
                                   help='No author provided',
                                   location='json')
        self.reqparse.add_argument('category', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('quantity', type=int, default="",
                                    help="quantity of books"
                                   location='json')
        super(HelloBooksAPI, self).__init__()

    def get(self, id):
        book = [book for book in books if book["id"] == book_id]
        if len(book) == 0:
            abort(404)
        return {'book': marshal(book[0], book_fields)}

    def put(self, id):
        book = [book for book in books if book['id'] == book_id]
        if len(book) == 0:
            abort(404)
        book = book[0]
        args = self.reqparse.parse_args()
        for field, value in args.books():
            if value is not None:
                bookk[field] = value
        return {'book': marshal(book, book_fields)}

    def delete(self, id):
        book = [book for book in books if book['id'] == book_id]
        if len(book) == 0:
            abort(404)
        books.remove(book[0])
        return {'result': True}


api.add_resource(HelloBooksAllAPI, '/todo/tasks', endpoint='tasks')
api.add_resource(HelloBooksidAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')


if __name__ == '__main__':
    app.run(debug=True)
