#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"A simple listener notifying about new lichess.org games"
# FIXME checks only for first 10 games

import requests
import notify
import database
import settings
import logging
import sys
import common

__API_URL = 'https://en.lichess.org/api/user/{}/games?playing=1'
logger = logging.getLogger(common.APPNAME)


class ConnectionError(Exception):
    pass


def get_games(user):
    "Get the list of all games for a user"
    try:
        url = __API_URL.format(user)
        reply = requests.get(url)
        return reply.json()
    except requests.exceptions.ConnectionError:
        raise ConnectionError


def run():
    "Download the data from the API and show a notification (if needed)"

    if settings.USERNAME == "":
        logger.critical("You need to set up a username in settings.py. "
                        "Quitting!!")
        sys.exit(1)

    rep = get_games(settings.USERNAME)
    logger.debug("Received reply from API:")
    logger.debug(rep)
    curr_games = rep["currentPageResults"]
    game_dict = {game['id']: game['lastMoveAt'] for game in curr_games}

    stats = database.new_games(game_dict)
    if stats.new > 0:
        notify.notify_games(stats.new, stats.total)
    else:
        logger.info("We have {} games but no new ones...".format(stats.total))

if __name__ == '__main__':  # do a single request
    logger.setLevel(settings.LOGGING_LEVEL)
    logging.basicConfig()
    run()
