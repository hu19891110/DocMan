#!/usr/bin/env python
# encoding:utf-8
import sys
from db.DBHelper import DBMysql
from sqlalchemy.orm import sessionmaker
from model.usersModel import UsersModel

reload(sys)
sys.setdefaultencoding('utf-8')

DBSession = sessionmaker(bind=DBMysql().getEngine())
