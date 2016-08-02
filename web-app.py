from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
#from database_setup import Base, Person
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#engine = create_engine('sqlite:///crudlab.db')
#Base.metadata.bind = engine
#DBSession = sessionmaker(bind=engine)
#session = DBSession()


@app.route('/')
def show_homepage():
	 return render_template("homepage.html")



@app.route('/music')
def show_music():
	 return render_template("music.html")




@app.route('/food')
def show_food():
	 return render_template("food.html")






@app.route('/news')
def show_news():
	 return render_template("news.html")

@app.route('/news/<int:pid>' , methods=['GET','POST'])




if __name__ == "__main__":
 app.run(debug=True)