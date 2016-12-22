#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from view import main
from flask import Flask,url_for,render_template,request
from flask_bootstrap import Bootstrap
from ext import db
from models import User

app=Flask(__name__)
app.config.from_object('magage')
bootstrap=Bootstrap(app)
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

app.register_blueprint(main,url_prefix='')

if __name__=='__main__':
    app.run(host='0.0.0.0')
