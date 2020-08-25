# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/25 13:22

from flask import Flask
from flask import render_template, flash, redirect
from froms import LoginForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index():
    user = {'nickName': 'Yuyong'}
    posts = [
        {
            'author': {'nickname': 'Mr.Zhang', 'gender': 'F'},
            'title': '进化论剖析',
            'time': '2020-08-25 15:01:00'
         },
        {
            'author': {'nickname': 'Mrs.Wang', 'gender': 'M'},
            'title': '论物种起源',
            'time': '2020-08-20 12:01:00'
        },
        {
            'author': {'nickname': 'Dr.Zhao', 'gender': 'F'},
            'title': 'python基础教程',
            'time': '2020-08-22 10:01:00'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{0}",rember_me="{1}"'.format(form.openid.data, str(form.remeber_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign in',
                           form=form,
                           providers = app.config['OPENID_PROVIDERS']
                           )