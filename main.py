#!/usr/bin/env python

import csv
import os
import sys
from string import *


def collect_data(csv_file):
        with open(csv_file, 'r') as csv_file:
            reading = csv.reader(csv_file)
            for lines in reading:
                # Depending on the column can append more data into an array
                # movie name is in the 1st index

                name_of_movie.append(lines[1])
                # length of movie in mins is in the 13th index
                #
                length_of_movie.append(lines[13])
                # release date of movie in the 12th index
                #
                release_date.append(lines[12])
                # production company in 7th index
                #
                production.append(lines[7])
                # imbd rating in the 4th index
                #
                imbd_rating.append(lines[4])
                # meta critic rating in the 5th index
                #
                meta_rating.append(lines[5])
                # movie rating in the 3rd index
                #
                age_rating.append(lines[3])
                # number of votes in the 9th index
                #
                num_votes.append(lines[9])
                # budget in the 17th index
                #
                budget.append(lines[17])
                # profites in the 18th index
                #
                Box_office.append(lines[18])

            csv_file.close()


def clean_vals(column):
    clean = []
    for rating in column:
        if rating == ('N/A' or 'UNRATED' or 'NOT RATED'):
            rating = None

        if rating == (0 or '0'):
            rating = None
        clean.append(rating)
    return clean


def min_remove(length_of_movie):
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


def main():
    print ('starting to analyze...')
    # initialize new clean vars
    #
    clean_name = []
    clean_length = []
    clean_release = []
    clean_productoin = []
    clean_imdb = []
    clean_meta = []
    clean_age = []
    clean_votes = []
    clean_INITbudget = []
    clean_box = []

    # TODO: change to argv[0]
    #
    collect_data('NBCU_data.csv')

    clean_release = clean_date(release_date)
    print clean_release

    clean_length = min_remove(length_of_movie)

    clean_box = clean_budget(Box_office)
    clean_INITbudget = clean_budget(budget)

    clean_name = clean_vals(name_of_movie)
    clean_length = clean_vals(clean_length)
    # clean_release = clean_vals(clean_release)
    clean_productoin = clean_vals(production)
    clean_imdb = clean_vals(imbd_rating)
    clean_meta = clean_vals(meta_rating)
    clean_age = clean_vals(age_rating)
    clean_votes = clean_vals(num_votes)
    clean_INITbudget = clean_vals(clean_INITbudget)
    clean_box = clean_vals(clean_box)



if __name__ == '__main__':
    # initialize columns
    #
    name_of_movie = []
    length_of_movie = []
    release_date = []
    production = []
    imbd_rating = []
    meta_rating = []
    age_rating = []
    num_votes = []
    budget = []
    Box_office = []

    month = []
    day = []
    year = []

    main()
