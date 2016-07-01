from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'monburan'}
    return render_template("index.html",title = "Home",user = user)
    #return "Hello World! flask"
