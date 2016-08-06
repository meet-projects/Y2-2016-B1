from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/food' , methods=['GET', 'POST'])
def food():
	if request.method == 'GET':
		food_list = session.query(Food).all()
		return render_template('food.html' , food = food_list)
	else :
		flag = False 
		new_ing = request.form['Ingredients']
		new_steps = request.form['Steps']
		new_name = request.form['Name']
		new_nat = request.form['Nationality']
		newf = Food( ingredients = new_ing ,steps = new_steps , name = new_steps , nationality = new_nat )
		session.add(newf)
		session.commit()
		food_list = session.query(Food).all()
		if 	new_ing[0] == [""] or new_steps[0] == [""] or new_name[0] == [""] or new_nat[0] == [""]:
			flag = True

		return render_template('food.html' ,  food = food_list , flag = flag )

@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
