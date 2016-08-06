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
	article = session.query(News).first()
	return render_template('news.html', article=article)

@app.route('/food' , methods=['GET', 'POST'])
def food():
	if request.method == 'GET':
		food_list = session.query(Food).all()
		return render_template('food.html' , food = food_list)
	else:
		new_ing = request.form['Ingredients']
		new_steps = request.form['Steps']
		new_name = request.form['Name']
		new_nat = request.form['Nationality']
		newf = Food( ingredients = new_ing ,steps = new_steps , name = new_steps , nationality = new_nat )
		session.add(newf)
		session.commit()
		return redirect(url_for('food'))

@app.route('/food/edit/<int:food_id>/', methods=['GET', 'POST'])
def food_edit(food_id):
	item = session.query(Food).filter_by(id=food_id).first()
	if request.method == 'GET':
		return render_template('food_edit.html', item=item)
	else:
		new_ing = request.form['Ingredients']
		new_steps = request.form['Steps']
		new_name = request.form['Name']
		new_nat = request.form['Nationality']
		item.ingredients = new_ing
		item.steps = new_steps
		item.name = new_name
		item.nationality = new_nat
		session.commit()
		return redirect(url_for('food'))


@app.route('/food/delete/<int:food_id>/', methods=['GET', 'POST'])
def food_delete(food_id):
	item = session.query(Food).filter_by(id=food_id).first()
	if request.method == 'GET':
		return render_template('food_delete.html', item=item)
	else:
		session.delete(item)
		session.commit()
		return redirect(url_for('food'))





@app.route('/music', methods=['GET', 'POST'])
def music():
	if request.method == 'GET':
		music_list = session.query(Music).all()
		return render_template('music.html' , music = music_list)
	else:
		new_song = request.form['song']
		new_artist = request.form['artist']
		new_link = request.form['link']
		new_nationality = request.form['nationality']
		newf = Music( song = new_song ,artist = new_artist , link = new_link , nationality = new_nationality )
		session.add(newf)
		session.commit()
		return redirect(url_for('music'))


if __name__ == '__main__':
    app.run(debug=True, port=5003)
