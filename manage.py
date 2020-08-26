# -*- coding:utf-8 -*-
# @Author: YuYong
# @Date  : 2020/8/26 17:20

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
# 不能直接从文件夹app导入db,否则migrate的时候检测不到models中定义的db数据，无法创建迁移版本
from app.models import db


# 实例化一个manage对象，用来管理APP
manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()