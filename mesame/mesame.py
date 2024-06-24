from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # SQLite baza
db = SQLAlchemy(app)

# modeli
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', author='{self.author}')"
    # __str__-s nacvlas sheidzleba __repr__, str ufro user_frinedly-ia da wakitxvadlobistvisac da repr aris ufro objectis 'shida mdgomareobostbis'

# tableis sheqmna
with app.app_context():  # es minda tore ise ar sheiqmneba, appis shignit unda iyos
    db.create_all()

    initial_books = [
        {
            "id": 1,
            "name": "Elon Musk",
            "author": "Ashlee Vance"
        },
        {
            "id": 2,
            "name": "Steve Jobs",
            "author": "Walter Isaacson"
        }
    ]
    
    for book_data in initial_books:
        book = Book(**book_data) #cal-calke amovighot dictebi
        db.session.add(book)

    db.session.commit()

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [{"id": book.id, "name": book.name, "author": book.author} for book in books]
    return jsonify(books_list)

if __name__ == '__main__':
    app.run(debug=True)
