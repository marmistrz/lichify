#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"A simple listener notifying about new lichess.org games"
import requests
import notify
import database

player = "marmistrz"
__API_URL = 'https://en.lichess.org/api/user/{}/games?playing=1'


def get_games(user):
    "Get the list of all games for a user"
    url = __API_URL.format(user)
    reply = requests.get(url)
    return reply.json()


rep = get_games(player)
curr_games = rep["currentPageResults"]
count = len(curr_games)

# if count > 0:
#    notify.notify_games(count)

conn = database.opendb()
with conn:
    mgr = database.Manager(conn)
