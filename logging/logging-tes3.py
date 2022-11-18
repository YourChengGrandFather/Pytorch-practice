#!/usr/bin/env python
# coding: utf-8

import logging
import logging.config
logging.config.fileConfig('loggin.conf')

logger = logging.getLogger('applogger')
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")

