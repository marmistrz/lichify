#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import common
import logging
import settings
import client

startmsg = "Starting the {} daemon...".format(common.APPNAME_HUMAN)

logger = logging.getLogger(__name__)
logger.setLevel(settings.LOGGING_LEVEL)

logging.basicConfig()
logging.info(startmsg)

while True:
    client.run()
    logger.info("Sleeping for {} minutes".format(settings.CHECK_INTERVAL))
    time.sleep(settings.CHECK_INTERVAL * 60)
