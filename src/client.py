#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"A simple listener notifying about new lichess.org games"

import requests
import notify
import database
import settings
import logging
import sys

__API_URL = 'https://en.lichess.org/api/user/{}/games?playing=1'
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOGGING_LEVEL)


def get_games(user):
    "Get the list of all games for a user"
    url = __API_URL.format(user)
    reply = requests.get(url)
    return reply.json()


def run():
    "Download the data from the API and show a notification (if needed)"

    if settings.USERNAME == "":
        logger.critical("You need to set up a username in settings.py."
                         "Quitting!!")
        sys.exit(1)

    rep = get_games(settings.USERNAME)
    curr_games = rep["currentPageResults"]
    game_dict = {game['id']: game['timestamp'] for game in curr_games}

    stats = database.new_games(game_dict)
    if stats.new > 0:
        notify.notify_games(stats.new)
    else:
        logger.info("We have {} games but no new ones...".format(stats.total))

if __name__ == '__main__':  # do a single request
    run()
