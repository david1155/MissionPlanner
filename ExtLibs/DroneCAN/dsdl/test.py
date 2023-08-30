#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(stream=sys.stderr, level='DEBUG', format='%(levelname)s: %(message)s')

from uavcan import dsdl

if parsed := dsdl.parse_namespaces(['uavcan', 'com', 'ardupilot', 'dronecan']):
    logging.info('%d data types parsed successfully', len(parsed))
