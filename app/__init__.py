# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/26 16:08

from flask import Flask
from app.froms import LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)