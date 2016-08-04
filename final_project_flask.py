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

@app.route('/food', methods=["GET", "POST"])
def food():
    if request.method == 'GET' :
    	return render_template('food.html')
    else: 
    	new_ingredients=request.form['ingredients']
    	new_steps=request.form['steps']
    	new_name=request.form['name']

    	comment=Food_Comments(ingredients=new_ingredients, name=new_name, steps=new_steps)
        session.add(friend)
        session.commit()

        return redirect(url_for('food.html'))



@app.route('/music', methods=["GET", "POST"])
def music():
	if request.method == "GET":
    return render_template('music.html')
	else: 
    	new_song=request.form['song']
    	new_artist=request.form['artist']
    	new_link=request.form['link']
    	new_name=request.form['name']

    	comment=Music_Comments(song=new_song, artist= new_artist link=new_link, name=new_name)
        session.add(friend)
        session.commit()

        return redirect(url_for('music.html'))



if __name__ == '__main__':
    app.run(debug=True, port=5003)
