from flask import Flask, jsonify, abort, request
app = Flask(__name__)
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
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

#get book by id

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
