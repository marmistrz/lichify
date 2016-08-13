# -*- coding: utf-8 -*-

import common
import sqlite3
import xdg.BaseDirectory
import os.path


__datadir = xdg.BaseDirectory.save_data_path(common.APPNAME)
__dbname = "games.db"
__dbpath = os.path.join(__datadir, __dbname)


def opendb():
    return sqlite3.connect(__dbpath)


class Manager:

    def __init__(self, db):
        self.db = db

    def is_new_game(id, timestamp):
        pass
