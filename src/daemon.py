#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To kick off the script, run the following from the python directory:
#   PYTHONPATH=`pwd` python testdaemon.py start

import time
import common
import logging
import settings
import client

logging.basicConfig(level=settings.LOGGING_LEVEL)
startmsg = "Starting the {} daemon...".format(common.APPNAME_HUMAN)

logging.info(startmsg)
while True:
    client.run()
    logging.warn("Sleeping for {} minutes".format(settings.CHECK_INTERVAL))
    time.sleep(settings.CHECK_INTERVAL * 60)
