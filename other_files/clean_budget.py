#!/usr/bin/env python

import csv
import os
import sys
from string import *

def clean_budget(budgetlist):
    '''
    This function removes all non-digits from a list.
    It was designed for the film budgets. It will also remove
    strings longer than 20 chars in length.
    '''
    # Open new list
    newlist = []
    for i in budgetlist:
        if (len(i) > 20):
            newlist.append('None')
        else:
            newlist.append(''.join(c for c in i if c in digits))
    return newlist
