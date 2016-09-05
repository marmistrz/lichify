#!/usr/bin/env python
# -*- coding: utf-8 -*-
"The daemon checking for new games periodically"

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
    try:
        client.run()
        logger.info("Sleeping for {} minutes".format(settings.CHECK_INTERVAL))
        time.sleep(settings.CHECK_INTERVAL * 60)
    except client.ConnectionError:
        logger.warning(
            "Unable to connect to the API, probably the connection is down. "
            "Retrying in {} minutes".format(settings.RETRY_INTERVAL))
        time.sleep(settings.RETRY_INTERVAL * 60)
