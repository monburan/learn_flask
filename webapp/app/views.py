from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'monburan'}
    posts = [
            {
                'author':{'nickname':'mazaiku'},
                'body':'fake user 1'
                },
            {
                'author':{'nickname':'lake2'},
                'body':'fake user 2'
                },
            {
                'author':{'nickname':'evilcos'},
                'body':'fake user 3'
                }
            ]
    return render_template(
            "index.html",
            title = "Home",
            user = user,
            posts = posts)
    #return "Hello World! flask"
