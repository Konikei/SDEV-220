#https://www.youtube.com/watch?v=qbLc5a9jdXo
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    Author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.id} - {self.book_name} - {self.Author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    
    return {"drinks": "drink data"}