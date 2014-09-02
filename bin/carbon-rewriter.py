#!/usr/bin/env python

import sys
import os.path

# Figure out where we're installed
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BIN_DIR)


# Make sure that carbon's 'lib' dir is in the $PYTHONPATH if we're running from
# source.
LIB_DIR = os.path.join(ROOT_DIR, "lib")
sys.path.insert(0, LIB_DIR)

from carbon.util import run_twistd_plugin
from carbon.exceptions import CarbonConfigException

try:
    run_twistd_plugin(__file__)
except CarbonConfigException, exc:
    raise SystemExit(str(exc))

