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
            self.month = []
            self.year = []
            self.day = []
            self.production = []
            self.imbd_rating = []
            self.meta_rating = []
            self.age_rating = []
            self.num_votes = []
            self.budget = []
            self.Box_office = []
            self.gross_multiplier = []

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

    # checked
    def clean_vals(self, myarg):
        clean = []
        for rating in myarg:
            if rating == ('N/A' or 'UNRATED' or 'NOT RATED'):
                rating = None

            if rating == (0 or '0'):
                rating = None
            clean.append(rating)

        return clean

    # checked
    def min_remove(self):
        for index in range(1, len(self.length_of_movie)):
            self.length_of_movie[index] = self.length_of_movie[index].strip(' min')
        return

    # checked
    def clean_date(self):

        for date in range(0, len(self.release_date)):
            val = self.release_date[date].split('-')
            self.day.append(val[0])
            try:
                if (val[0] == 'N/A'):
                    self.month.append('N/A')
                    self.year.append('N/A')
                else:
                    self.month.append(val[1])
                    self.year.append(val[2])
            except IndexError:
                self.month.append('N/A')
                self.year.append('N/A')
                self.day.append('N/A')
        return

    def clean_budget(self, budgetarg):
        '''
        This function removes all non-digits from a list.
        It was designed for the film budgets. It will also remove
        strings longer than 20 chars in length.
        '''
        # Open new list
        new_budget = []
        for i in budgetarg:
            if (len(i) > 20):
                new_budget.append(0)
            else:
                new_budget.append(''.join(c for c in i if c in digits))

        return new_budget

    def add_multiplier(self, box, budget):

        multiplier = []

        for i in range(len(box)):

            try:
                multiplier.append(float(box[i])/float(budget[i]))
            except TypeError:
                multiplier.append(0.0)
            except ValueError:
                multiplier.append(0.0)
            except ZeroDivisionError:
                multiplier.append(0.0)

        return multiplier

def main(argv):
    print "program executing..."

    clean = clean_up()
    clean.collect_data('NBCU_data.csv')
    '''    
    clean.name_of_movie = clean.clean_vals(clean.name_of_movie)
    clean.age_rating = clean.clean_vals(clean.age_rating)
    clean.production = clean.clean_vals(clean.production)
    clean.imbd_rating = clean.clean_vals(clean.imbd_rating)
    clean.meta_rating = clean.clean_vals(clean.meta_rating)
    clean.num_votes = clean.clean_vals(clean.num_votes)
    '''
    print len(clean.production)
    print len(clean.imbd_rating)
    print len(clean.meta_rating)
    print len(clean.age_rating)

    clean.min_remove()
    print len(clean.length_of_movie)

    clean.clean_date()
    print len(clean.month)

    clean.budget = clean.clean_budget(clean.budget)
    print len(clean.budget)

    clean.Box_office = clean.clean_budget(clean.Box_office)
    print len(clean.Box_office)

    clean.gross_multiplier = clean.add_multiplier(clean.Box_office, clean.budget)
    print len(clean.gross_multiplier)

    # remove existing header
    #
    clean.name_of_movie.pop(0)
    clean.production.pop(0)
    clean.age_rating.pop(0)
    clean.imbd_rating.pop(0)
    clean.meta_rating.pop(0)
    clean.num_votes.pop(0)
    clean.day.pop(0)
    clean.month.pop(0)
    clean.year.pop(0)
    clean.budget.pop(0)
    clean.Box_office.pop(0)
    clean.gross_multiplier.pop(0)

    # insert column headers
    #
    clean.name_of_movie.insert(0, 'name')
    clean.production.insert(0, 'production')
    clean.age_rating.insert(0, 'age_rating')
    clean.imbd_rating.insert(0, 'imbd_rating')
    clean.meta_rating.insert(0, 'meta_rating')
    clean.num_votes.insert(0, 'num_votes')
    clean.day.insert(0, 'day')
    clean.month.insert(0, 'month')
    clean.year.insert(0, 'year')
    clean.budget.insert(0, 'budget')
    clean.Box_office.insert(0, 'box_office')
    clean.gross_multiplier.insert(0, 'multiplier')

    # cleaning the data
    #
    clean.name_of_movie = clean.clean_vals(clean.name_of_movie)
    clean.age_rating = clean.clean_vals(clean.age_rating)
    clean.production = clean.clean_vals(clean.production)
    clean.imbd_rating = clean.clean_vals(clean.imbd_rating)
    clean.meta_rating = clean.clean_vals(clean.meta_rating)
    clean.num_votes = clean.clean_vals(clean.num_votes)
    clean.year = clean.clean_vals(clean.year)
    clean.month = clean.clean_vals(clean.month)
    clean.day = clean.clean_vals(clean.day)


    # zip columns together and write to .csv file
    #
    with open("full_dataset_cleaned.csv", 'wb') as myfile:
        wr = csv.writer(myfile, dialect='excel')
        for i in zip(clean.name_of_movie, clean.production, clean.age_rating, clean.imbd_rating, clean.meta_rating, clean.num_votes, clean.day, clean.month, clean.year, clean.budget, clean.Box_office, clean.gross_multiplier):
            wr.writerow(i)

if __name__ == '__main__':
    main(sys.argv[1:])
