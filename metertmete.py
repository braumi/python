# Flask-ის გარემოში შექმენით წიგნების სია, მათი დასახელებით, ფასით და isbn კოდით, შემდეგ შესაბამისი url მისამართის
#  საშუალებით, წიგნის isbn კოდის მიხედვით მოახდინეთ წიგნის დასახელების და ფასის, ბრაუზერის ეკრანზე გამოტანა. 
from flask import Flask, jsonify
app = Flask(__name__)

books = [
    {
        'book': 'pride and prejudice',
        'price': '12$',
        'isbn': '123'
    },
    {
        'book': 'pride and prejudice2',
        'price': '12.0$',
        'isbn': '1234'
    },
    {
        'book': 'pride and prejudice3',
        'price': '12.6$',
        'isbn': '1234'
    }
]

@app.route('/', methods = ['GET'])
def home_page():
    return jsonify('this is home page')
    

@app.route('/<int:isbn>', methods = ['GET'])
def get_book(isbn):
    for book in books:
        if book['isbn'] == str(isbn):
            # return jsonify({'book': book['book'], 'price': book['price']})
            return jsonify(book) #es isbn-sac abrunebs
    return jsonify({'message': 'Book not found'})

        
if __name__ == '__main__':
    app.run(debug=True)