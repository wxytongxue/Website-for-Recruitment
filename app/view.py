#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,url_for,render_template,request,Blueprint,flash,session,redirect
from db import *
from form import *
from models import User,Item,Category
from ext import db

main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index_p():
    return render_template('index.html',employment=employment,company=company,school=school)
@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        u = User.query.filter_by(email=form.email.data).first()
        if u.password == form.password.data:
            session['login']=True
            session['user']=u.username
            print u.username
            return render_template('index.html',employment=employment,company=company,school=school)

    session['login']=False
    return render_template('login.html',form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    flash(u'登录成功，欢迎回来!')
    if request.method=='POST' and form.validate_on_submit():
        user=User(form.name.data,form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)
@main.route('/quit')
def quit():
    session['login']=False
    session['user']=''
    return render_template('index.html',employment=employment,company=company,school=school)

# test

@main.route('/manage/', methods=['GET', 'POST'])
def index():
    return render_template('manage.html',count=count)
    #return redirect(url_for('main.complete'))
    # if request.method == 'POST':
    #     body = request.form.get('item')
    #     id = request.form.get('category')
    #     category = Category.query.get_or_404(id)
    #     item = Item(body=body, category=category)
    #     db.session.add(item)
    #     return redirect(url_for('main.category',id))
    #
    # return redirect(url_for('main.category', id=1))
@main.route('/manage/complete/', methods=['GET', 'POST'])
def complete():
    return render_template('manage.html',count=count)

# @main.route('/manage/verify/', methods=['GET','POST'])
# def verify():
#     g['verify']=True
#     return  render_template('manage_t.html',count=count)
