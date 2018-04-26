import os
import sys
import csv

import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from operator import itemgetter, attrgetter


def season_determine(val):
        val2 = val
        month_seasons = {"Jan": "Winter", "Feb": "Winter", "Dec": "Winter",
                         "Mar": "Spring", "Apr": "Spring", "May": "Spring", "Jun": "Summer",
                         "Jul": "Summer", "Aug": "Summer", "Sep": "Fall",
                         "Oct": "Fall", "Nov": "Fall"}

        for month in range(1, len(val)):
                if val2[month] in month_seasons:
                        val2[month] = month_seasons[val2[month]]
        return val2


def main():

        print "starting..."

        # initializing  the columns
        #
        name = []
        prod = []
        age = []
        imdb = []
        meta = []
        num_votes = []
        day = []
        month = []
        year = []
        budget = []
        box_office = []
        multiplier = []

        # filing the columns from the csv file
        # DEBUG: find a way to fix the year 'cuz its showing (ex: 21 for 1921)
        # DEBUG: fix the clean_up class cuz data are not clean clean
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

        # for the months to store to dict....
        # DEBUG: this is overwriting the months with seasons
        #
        # season = season_determine(month)

        # set te columns in rows so we can work on becomes a list of tuples
        # usage: final_data[row, column]
        #
        final_data = zip(name, prod, age, imdb, meta, num_votes, day, month, year,
                        budget, box_office, multiplier)

        final_np = np.array(final_data)

        # Sorting by column
        #
        multiplier_sort = final_np[np.argsort(final_np[:, 11])[::-1]]
        month_sort = final_np[np.argsort(final_np[:, 7])[::-1]]
        year_sort = final_np[np.argsort(final_np[:, 8])[::-1]]

        # this is just to test the sorting
        #
        z = 0
        seasons = [[], [], [], []]
        fall = seasons[0]
        winter = seasons[1]
        spring = seasons[2]
        summer = seasons[3]

        for col in multiplier_sort:
            # print col[0], ': ', col[11]

            if z == 0:
                z += 1
                continue
            if col[7] == 'Dec' or col[7] == 'Jan' or col[7] == 'Feb':
                winter.append(col[7])

            if col[7] == 'Mar' or col[7] == 'Apr' or col[7] == 'May':
                spring.append(col[7])

            if col[7] == 'Jun' or col[7] == 'Jul' or col[7] == 'Aug':
                fall.append(col[7])

            if col[7] == 'Sep' or col[7] == 'Oct' or col[7] == 'Nov':
                summer.append(col[7])



            # print 'name: ', col[0], '\nbudget:', col[9], '-->', 'multiplier: ', col[11]
            z += 1


        #print boffice


        y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
        N = len(seasons)
        x = range(N)
        width = 1/1.9
        plt.bar(x, seasons[0], width, color="blue")


        fig = plt.gcf()
        plt.show()
        #plot_url = plt.plot_mpl(fig, filename='mpl-basic-bar')

        '''plt.plot(boffice)
        plt.yticks(boffice, names)
        plt.grid()
        plt.show()
'''

if __name__ == '__main__':
        main()
