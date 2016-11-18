#!/usr/bin/env python
# encoding:utf-8
from db.DBHelper import DBMysql
from sqlalchemy.orm import sessionmaker
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

DBSession = sessionmaker(bind=DBMysql().getEngine())
