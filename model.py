class Books(object):
    def __init__(self,books):
        self.book={}
        self.books=books
        
    def create_book(self,book_id,bookname,author,category,quantity,publication_year):  
        self.bookname=bookname
        self.author=author
        self.id=book_id
        self.category=author
        self.quantity=quantity
        self.year=publication_year
        self.book={"bookname":self.bookname,"author":self.author,"category":self.category,"quantity":self.quantity,"publication_year":self.year}
        self.books[self.id]=self.book
        return self.books

    #get books
    def get_all(self):
        return self.books

    #get book by id
    def get_bookbyid(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
        else:
            return"book not available"
    	

    #edit a book 
    def put(self,book_id,bookname,author,category,quantity,publication_year):
        if book_id in self.books:
           self.bookname=bookname
           self.author=author
           self.category=category
           self.quantity=quantity
           self.year=publication_year
           self.book={"bookname":self.bookname,"author":self.author,"category":self.category,"quantity":self.quantity,"publication_year":self.year}
           self.books[book_id]=self.book
           return self.books
        return "book not found"

    #delete a book  
    def delete(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return self.books
        return "book not found"


books={1:{"id":1,"bookname":"a niggas life","author":"kelvin kiama","category":"drama/action","quantity":10,"publication_year":1993},
       2:{"id":2,"bookname":"Real Gs","author":"kelvin kiama","category":"drama/action","quantity":30,"publication_year":2010}}


