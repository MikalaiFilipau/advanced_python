###############
# Script causes segmentation fault
# example from faulthandler documentation
# https://faulthandler.readthedocs.io/
###############

import ctypes

ctypes.string_at(0) # try to access unreachable region of memory
