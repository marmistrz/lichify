#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To kick off the script, run the following from the python directory:
#   PYTHONPATH=`pwd` python testdaemon.py start

import time
import common
import logging
import settings
import client

logger = logging.getLogger(__name__)
logger.setLevel(settings.LOGGING_LEVEL)

startmsg = "Starting the {} daemon...".format(common.APPNAME_HUMAN)

logger.info(startmsg)
while True:
    client.run()
    logger.info("Sleeping for {} minutes".format(settings.CHECK_INTERVAL))
    time.sleep(settings.CHECK_INTERVAL * 60)
