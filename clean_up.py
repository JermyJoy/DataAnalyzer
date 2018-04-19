#!/usr/bin/env python


import os
import sys
import pandas as pd
import csv
from string import *


class clean_up():
    def __init__(self):
            # initialize columns
            #
            self.name_of_movie = []
            self.length_of_movie = []
            self.release_date = []
            self.production = []
            self.imbd_rating = []
            self.meta_rating = []
            self.age_rating = []
            self.num_votes = []
            self.budget = []
            self.Box_office = []

            month = []
            day = []
            year = []

    def collect_data(self, csv_file):
            with open(csv_file, 'r') as csv_file:
                reading = csv.reader(csv_file)
                for lines in reading:
                    # Depending on the column can append more data into an arry
                    # movie name is in the 1st index
                    self.name_of_movie.append(lines[1])
                    # length of movie in mins is in the 13th index
                    #
                    self.length_of_movie.append(lines[13])
                    # release date of movie in the 12th index
                    #
                    self.release_date.append(lines[12])
                    # production company in 7th index
                    #
                    self.production.append(lines[7])
                    # imbd rating in the 4th index
                    #
                    self.imbd_rating.append(lines[4])
                    # meta critic rating in the 5th index
                    #
                    self.meta_rating.append(lines[5])
                    # movie rating in the 3rd index
                    #
                    self.age_rating.append(lines[3])
                    # number of votes in the 9th index
                    #
                    self.num_votes.append(lines[9])
                    # budget in the 17th index
                    #
                    self.budget.append(lines[17])
                    # profites in the 18th index
                    #
                    self.Box_office.append(lines[18])

                csv_file.close()

    def clean_vals(self, column):
        clean = []
        for rating in column:
            if rating == ('N/A' or 'UNRATED' or 'NOT RATED'):
                rating = None

            if rating == (0 or '0'):
                rating = None
            clean.append(rating)
        return clean

    def min_remove(self, length_of_movie):
        for index in range(1, len(length_of_movie)):
            length_of_movie[index] = length_of_movie[index].strip(' min')
        return length_of_movie

    def clean_date(release_date):

            for date in range(1, len(release_date)):
                val = release_date[date].split('-')
                day.append(val[0])
                try:
                    if (val[0] == 'N/A'):
                        month.append('N/A')
                        year.append('N/A')
                    else:
                        month.append(val[1])
                        year.append(val[2])
                except IndexError:
                    month.append('N/A')
                    year.append('N/A')
                    day.append('N/A')

    def clean_budget(budgetlist):
        '''
        This function removes all non-digits from a list.
        It was designed for the film budgets. It will also remove
        strings longer than 20 chars in length.
        '''
        # Open new list
        new_budget = []
        for i in budgetlist:
            if (len(i) > 20):
                new_budget.append('None')
            else:
                new_budget.append(''.join(c for c in i if c in digits))
        return new_budget


def main(argv):
    print "this compiled.."

    clean = clean_up()
    clean.collect_data('NBCU_data.csv')
    clean.clean_vals()


if __name__ == '__main__':
    main(sys.argv[1:])
