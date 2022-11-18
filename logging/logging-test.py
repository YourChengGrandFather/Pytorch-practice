#!/usr/bin/env python
# coding: utf-8

import logging

# 使用baseConfig()来制定日志输出级别
logging.basicConfig(filename='demo.log',filemode='w', level=logging.DEBUG)
logging.debug("this is debug")

logging.info("this is info")

logging.warning("this is warning")

logging.error("this is error")

logging.critical("this is critical")

