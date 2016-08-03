from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base	
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
