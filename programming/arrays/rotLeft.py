#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    start = a[:d]
    end = a[d:]
    return end + start
