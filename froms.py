# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/25 15:09

from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remeber_me = BooleanField('remeber_me', default=False)
