#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class NameForm(Form):
     name = StringField('What is you name?',validators=[Required()])
     submit=SubmitField('Submit')

app= Flask(__name__)
@app.route('/', methods=('GET', 'POST'))
def index():
    name=None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('index.html',form =form,name=name)

if __name__=='__main__':
 app.run()
