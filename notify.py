# -*- coding: utf-8 -*-
"Notifications for new games"

import common
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify


def notify_games(count):
    "Show a notification in a cross-platform way"
    msg = "You have {} games awaiting a move".format(count)
    Notify.init(common.APPNAME_HUMAN)
    Hello = Notify.Notification.new(common.APPNAME_HUMAN,
                                    msg,
                                    "dialog-information")
    Hello.show()
