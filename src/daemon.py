#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To kick off the script, run the following from the python directory:
#   PYTHONPATH=`pwd` python testdaemon.py start

import time
import common
import sys
import settings
import client

startmsg = "Starting the {} daemon...".format(common.APPNAME_HUMAN)


print(startmsg, file=sys.stderr)
while True:
    client.run()
    print("Sleeping for {} minutes".format(settings.CHECK_INTERVAL))
    time.sleep(settings.CHECK_INTERVAL * 60)
