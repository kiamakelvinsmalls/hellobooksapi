from flask import Flask, jsonify, abort, request, url_for,make_response,redirect
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
from model import Books,books
app = Flask(__name__,static_url_path="")
Bootstrap(app)


auth = HTTPBasicAuth()

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']
        return redirect (url_for("get_books"))
    return """<html>
    <body>
    <form action="/login" method='POST'>
    <input type='text' placeholder='username' name="username" class="form-control">
    <input type='password' placeholder='password' name="password" class="form-control">
    <input type='submit' value='login'>
    <input type='reset'> 
    </form>
    <body>
    <html>"""


@auth.get_password
def get_password(username):
    if username == user:
        return  password
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
lib=Books(books)
#get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(lib.get_all()),200


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(lib.get_bookbyid(book_id)),200

#add  book
@app.route('/api/books', methods=['POST'])
def add_book():
	new = {
	       'book_id': request.json['book_id'],
	       'bookname': request.json['bookname'],
	       'author': request.json['author'],
	       'category': request.json['category'],
	       'quantity': request.json['quantity'],
	       'publication_year':request.json['publication_year']
	    }
	book_id = new['book_id']
	bookname=new['bookname']
	author =new['author']
	category =new['category']
	quantity= new['quantity']
	publication_year=new['publication_year']
	return jsonify(lib.create_book(book_id,bookname,author,category,quantity,publication_year)),201
    #update a book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
	edit = {
	       'bookname': request.json['bookname'],
	       'author': request.json['author'],
	       'category': request.json['category'],
	       'quantity': request.json['quantity'],
	       'publication_year':request.json['publication_year']
	    }
	bookname=edit['bookname']
	author =edit['author']
	category =edit['category']
	quantity= edit['quantity']
	publication_year=edit['publication_year']
	return jsonify(lib.put(bookname,author,category,quantity,publication_year)),200
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_task(book_id):
    return jsonify(lib.delete(book_id)),204

if __name__ == "__main__":
    app.run(debug=True)
