#!/usr/bin/env python
# coding: utf-8

import logging
# 记录器
logger = logging.getLogger('cn.aaplog')
logger.setLevel(logging.DEBUG)

# 处理器
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.WARNING)

fileHandler = logging.FileHandler(filename='demo')
fileHandler.setLevel(logging.INFO)

# formatter
formatter = logging.Formatter('%(asctime)s|10%(levelname)10s|%(lineno)4s|%(message)s')
consoleHandle.setFormatter(formatter)

logger.addHandler(consoleHandle)

# filter
filter = logging.Filter('cn.')
logger.addFilter(filter)

logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")
# print(logger)
# print(type(logger))

