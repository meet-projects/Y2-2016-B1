from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, News, News_Comments
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/news/<int:news_id>/', methods =['GET', 'POST'])
def news(news_id):
	if request.method == 'GET':
		article= session.query(News).filter_by(id=news_id).first()
		return render_template('news.html', article=article)
	else:
		comment= request.form['comment']
		name= request.form['name']
		nationality=request.form['nationality']
		post= News_Comments(name=name, text=comment, nationality=nationality, news_id=news_id)
		session.add(post)
		session.commit()

		return redirect(url_for('news',news_id=news_id))

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
