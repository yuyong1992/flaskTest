# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/25 15:04


class BaseConfig(object):
    # config for boot
    DEBUG = False
    HOST = '127.0.0.1'
    PORT = 8080

    # config for WTF
    CSRF_ENABLE = True
    SECRET_KEY = 'you-will-never-guess'

    # config for login page html
    OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
    ]

    # config for mysql database
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

