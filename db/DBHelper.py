#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


class DBMysql:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'
        self.dbName = 'docker_db'
        self.charset = 'utf8'

    def getEngine(self):
        return create_engine('mysql+mysqldb://' + self.user + ':' + self.passwd + '@' + self.host + ':' + str(
            self.port) + '/' + self.dbName + '?charset=' + self.charset + '', poolclass=NullPool, echo=True)
