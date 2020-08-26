# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/26 16:05
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(20), unique=True, nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True)
    real_name = db.Column(db.String(20))
    # 定义一个user 和 posts 的关系，一对多的关系，通常定义在“一”这一边
    posts = db.relationship('post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Users {0}>'.format(self.nick_name)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String(1000))
    create_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Posts {0}>'.format(self.title)