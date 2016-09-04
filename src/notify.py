# -*- coding: utf-8 -*-
"Notifications for new games"

import notify2
import common


def show_notification(msg):
    "a notify2 wrapper"
    notify2.init(common.APPNAME_HUMAN)  # REVIEW maybe call init once?
    notification = notify2.Notification(
        common.APPNAME_HUMAN,
        msg,
        "lichess")
    notification.show()


def notify_games(count, total):
    "Show a notification about new games"
    msg = "You have {} new games awaiting a move, {} total"
    show_notification(msg.format(count, total))
