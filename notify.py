# -*- coding: utf-8 -*-
"Notifications for new games"

import notify2
import common


def show_notification(msg):
    notify2.init(common.APPNAME)  # REVIEW maybe call init once?
    notification = notify2.Notification(
        common.APPNAME,
        msg,
        "dialog-information")
    notification.show()


def notify_games(count):
    "Show a notification in a cross-platform way"
    msg = "You have {} games awaiting a move".format(count)
    show_notification(msg)
