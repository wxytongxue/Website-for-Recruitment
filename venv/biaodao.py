#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap

class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])   #Required 确保确认前输入不为空
    Submit=SubmitField('Submit')

app=Flask(__name__)
app.config['SECRET_KEY']='wx'

@app.route('/',methods=['GET','POST'])
def index():
    # name =None
    # form=NameForm()
    # if form.validate_on_submit():
    #     name=form.name.data
    #     form.name.data=''
    return render_template('test.html')
    #return render_template('index.html',form=form,name=name)

app.run()
