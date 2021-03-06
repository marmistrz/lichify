# -*- coding: utf-8 -*-

import common
import xdg.BaseDirectory
import os.path
import json


__datadir = xdg.BaseDirectory.save_data_path(common.APPNAME)
__jsonname = "games.json"
__path = os.path.join(__datadir, __jsonname)


class GameDelta:
    def __init__(self, new, total):
        self.new = new
        "New games awaiting move"
        self.total = total
        "Total games awaiting move"


def new_games(games):
    """Record new games in persistent storage and return GameDelta
    informing about the new games"""
    new_games_cnt = 0
    try:
        with open(__path) as jsonfile:
            old_games = json.load(jsonfile)
    except FileNotFoundError:
        old_games = dict()

    for (game_id, new_timestamp) in games.items():
        # None is always different from new_timestamp; get default to None
        old_timestamp = old_games.get(game_id)
        if new_timestamp != old_timestamp:  # something has changed
            new_games_cnt += 1

    old_games.update(games)

    with open(__path, 'w') as jsonfile:
        json.dump(old_games, jsonfile)

    return GameDelta(new_games_cnt, len(games))
