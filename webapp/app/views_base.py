from app import app
from flask import render_template

@app.route('/')
@app.route('/index_base')
def index():
    user = {'nickname':'monburan'}
    posts = [
            {
                'author':{'nickname':'mazaiku'},
                'body':'fake user 1 in base html'
                },
            {
                'author':{'nickname':'lake2'},
                'body':'fake user 2 in base html'
                },
            {
                'author':{'nickname':'evilcos'},
                'body':'fake user 3 in base html'
                }
            ]
    return render_template(
            "index.html",
            title = "Home",
            user = user,
            posts = posts)
    #return "Hello World! flask"
