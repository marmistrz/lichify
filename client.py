#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"A simple listener notifying about new lichess.org games"
import requests
import notify
import database
import sys

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
game_dict = {game['id']: game['timestamp'] for game in curr_games}

stats = database.new_games(game_dict)
if stats.new > 0:
    notify.notify_games(stats.new)
else:
    print("We have {} games but no new ones...".format(stats.total),
          file=sys.stderr)
