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

@app.route('/delete/<int:comment_id>/',methods=['GET', 'POST'])
def delete(comment_id):
    comment = session.query(comment).filter_by(id=comment_id).first()
    if request.method=="GET":
        return render_template('delete.html', comment=comment)
    else:
        session.delete(comment)
        session.commit()
        return redirect(url_for('news'))

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

        comment=Music_Comments(song=new_song, artist= new_artist, link=new_link, name=new_name)
        session.add(comment)
        session.commit()

        return redirect(url_for('music.html'))



if __name__ == '__main__':
    app.run(debug=True, port=5003)
