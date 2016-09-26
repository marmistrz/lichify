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


def notify_games(count, total, now_playing):
    "Show a notification about new games"
    msg = (
        "Chess games await your move: {new} new, {total} total\n"
        "You're currently have {now_playing} games in progress."
    )
    show_notification(
        msg.format(total=total, new=count, now_playing=now_playing)
    )
