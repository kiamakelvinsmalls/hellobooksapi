from flask import Flask, jsonify, abort, request, url_for,make_response
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__,static_url_path="")

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
#get all books
def make_public_book(books):
    new_book = {}
    for field in books:
        if field == 'id':
            new_book['uri'] = url_for('get_book', book_id=books['id'], _external=True)
        else:
            new_book[field] = books[field]
    return new_book
#get all books
@app.route('/books', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': [make_public_book(books) for books in books]})


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'books': books[0]})

#add  book
@app.route('/books', methods=['POST'])
def add_book():
    book = {
	       'id': request.json['id'],
	       'bookname': request.json['bookname'],
	       'author': request.json['author'],
	       'category': request.json['category'],
	       'quantity': request.json['quantity']
	    }
    books.append(book)
    return jsonify({'book': book}), 201
#update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    book[0]['id'] = request.json.get('id', book[0]['id'])
    book[0]['bookname'] = request.json.get('bookname', book[0]['bookname'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['category'] = request.json.get('category', book[0]['category'])
    book[0]['quantity'] = request.json.get('quantity', book[0]['quantity'])
    return jsonify({'book': book[0]})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_task(book_id):
    book = [book for book in books if book['id'] == book_id]
    books.remove(book[0])
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=True)
