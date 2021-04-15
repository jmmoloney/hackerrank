#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -63 # maximum negative value possible
    for i in [0, 1, 2, 3]:
        first_row = arr[i]
        second_row = arr[i + 1]
        third_row = arr[i + 2]
        for j in [0, 1, 2, 3]:
            first_sum = first_row[j] + first_row[j+1] + first_row[j+2]
            second_sum = second_row[j+1]
            third_sum = third_row[j] + third_row[j+1] + third_row[j+2]
            total = first_sum + second_sum + third_sum
            if total > max_sum:
                max_sum = total
    return max_sum
