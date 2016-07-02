from flask.ext.wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default = False)
    #import class with string and boolean,use DataRequired() check whether the data is empty 
