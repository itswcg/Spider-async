# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : db.py
# @Time    : 19-2-13 下午2:28
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient


class MotorBase:
    _db = {}
    _collection = {}

    def __init__(self, loop=None):
        self.motor_uri = ''
        self.loop = loop or asyncio.get_event_loop()

    def client(self, db):
        self.motor_uri = f'mongodb://wcg:itswcg@212.64.50.167:2225/{db}'
        return AsyncIOMotorClient(self.motor_uri, io_loop=self.loop)

    def get_db(self, db):
        if db not in self._db:
            self._db[db] = self.client(db)[db]

        return self._db[db]
