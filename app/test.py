#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask,url_for,render_template
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email,Required

app=Flask(__name__)

class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(message= u'邮箱不能为空'), Length(1, 64),Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
    password = PasswordField(u'密码',validators=[Required(message= u'密码不能为空')])
    submit = SubmitField(u'登录')

class RegisterForm(Form):
    name = StringField(u'用户名',validators=[Required()])
    email = StringField(u'邮箱', validators=[DataRequired(message= u'邮箱不能为空'), Length(1, 64),Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
    password = PasswordField(u'密码',validators=[Required(message= u'密码不能为空')])
    password_q=PasswordField(u'确认密码',validators=[Required(message= u'密码不能为空')])
    submit = SubmitField(u'登录')


app.config['SECRET_KEY']='wx'
bootstrap=Bootstrap(app)
@app.route('/')
def index():
    dic1={"name":"java工程师","company":"腾讯","salary":"20k-30k","coom":"一年以上工作经验"}
    dic2={"name":"java工程师","company":"腾讯","salary":"20k-30k","coom":"一年以上工作经验"}
    jobs=[]
    jobs.append(dic1)
    jobs.append(dic2)
    return render_template('test2.html',name='wx',jobs=jobs,sign=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # if form.validate_on_submit():
    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(host='0.0.0.0')
