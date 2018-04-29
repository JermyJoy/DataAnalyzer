#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string
import csv
import matplotlib.pyplot as plt
import numpy as np


def processyearlydata(years):
    # pass to this function a list of years
    # will return years as 1900s and 2000s
    #
    newyears = []
    for i in years:

        try:
            k = ''.join(i.split())
            j = int(k)
            if (j >= 0 and j <= 18):
                j += 2000
            else:
                j += 1900
            newyears.append(j)
        except ValueError:
            newyears.append(0)
    return newyears


# generate dictionary with all possible years as keys, if year matches
# a key, store the index as a value in the dictionar
#
def getindexforyear(year):
    # generate list of years to match
    #
    possibleyears = []
    for i in range(1901, 2019):
        possibleyears.append(i)

    # store years as keys in dict and store list as value to keep
    # indices of year matches
    #
    yeardict = dict((el, []) for el in possibleyears)

    # place index of the year in the dictionary according to year key
    #
    for i in range(len(year)):
        if year[i] in yeardict:
            yeardict[year[i]].append(i)

    return yeardict


# main function
#
def main(argv):

    print "starting..."

    # initializing the colunms
    #
    month = []  # 7
    meta = []  # 4
    name = []  # 0
    prod = []  # 1
    age = []  # 2
    imdb = []  # 3
    num_votes = []  # 5
    day = []  # 6
    year = []  # 8
    budget = []  # 9
    box_office = []  # 10
    multiplier = []  # 11

#####################################################################
    # reading the clean dataset and fill the colunms
    #
    with open('full_dataset_cleaned.csv') as csv_file:
        val = csv.reader(csv_file)
        for row in val:
            name.append(row[0])
            prod.append(row[1])
            age.append(row[2])
            imdb.append(row[3])
            meta.append(row[4])
            num_votes.append(row[5])
            day.append(row[6])
            month.append(row[7])
            year.append(row[8])
            budget.append(row[9])
            box_office.append(row[10])
            multiplier.append(row[11])

#####################################################################
    # adding the 1900s and the 2000s to the years column
    #
    newyears = processyearlydata(year[1:])

    # getting the indexes of as dictionary
    # { year: [indexes,...], year2: [indexes,...],...}
    #
    index_val = getindexforyear(newyears)

    # getting the multipliers of each year as nested list
    #
    newmult = multiplier[1:]
    mult_vals = []
    for key in index_val:
        mult_deep = []
        for i in index_val[key]:
            mult_deep.append(float(newmult[i]))

        mult_vals.append(mult_deep)

    print len(mult_vals)

    # getting the average multiplier of each year
    #
    mult_avg = []
    for i in mult_vals:
        try:
            mult_avg.append(float(sum(i))/float(len(i)))

        except ZeroDivisionError:
            mult_avg.append(0.0)

        except TypeError:
            mult_avg.append(0.0)

    print mult_avg
    print len(mult_avg)

    # Exit gracefully
    #
    return


# Begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

# End of file
