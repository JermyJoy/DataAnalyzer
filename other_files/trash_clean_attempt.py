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

        ######################################################################
        Jans = []
        Febs = []
        Mar = []
        Apr = []
        May = []
        June = []
        July = []
        Aug = []
        Sep = []
        Oct = []
        Nov = []
        Dec = []
        NONE = []

        for index in range(1, len(month)):
                if month[index] == 'Jan':
                        Jans.append(index)
                elif month[index] == 'Feb':
                        Febs.append(index)
                elif month[index] == 'Mar':
                        Mar.append(index)
                elif month[index] == 'Apr':
                        Apr.append(index)
                elif month[index] == 'May':
                        May.append(index)
                elif month[index] == 'Jun':
                        June.append(index)
                elif month[index] == 'Jul':
                        July.append(index)
                elif month[index] == 'Aug':
                        Aug.append(index)
                elif month[index] == 'Sep':
                        Sep.append(index)
                elif month[index] == 'Oct':
                        Oct.append(index)
                elif month[index] == 'Nov':
                        Nov.append(index)
                elif month[index] == 'Dec':
                        Dec.append(index)
                elif month[index] == 'N/A':
                        NONE.append(index)
        #print len(Jans)+len(Febs)+len(Mar)+len(Apr)+len(May)+len(June)+len(July)+len(Aug)+len(Sep)+len(Nov)+len(Oct)+len(Dec)+len(NONE)
        # There are over 200 entries that are N/A !

        multiplier_Jans = []
        multiplier_Feb = []
        multiplier_Mar = []
        multiplier_Apr = []
        multiplier_May = []
        multiplier_June = []
        multiplier_July = []
        multiplier_Aug = []
        multiplier_Sep = []
        multiplier_Oct = []
        multiplier_Nov = []
        multiplier_Dec = []

        multipliers = [multiplier_Jans, multiplier_Feb, multiplier_Mar, multiplier_Apr, multiplier_May, multiplier_June,\
        multiplier_July, multiplier_Aug, multiplier_Sep, multiplier_Oct, multiplier_Nov, multiplier_Dec]

        mult_months = [Jans, Febs, Mar, Apr, May, June, July, Aug, Sep, Oct, Nov, Dec]

        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        avg_months = []

        #### Averages for the months and their respective multipliers #####
        i = 0
        for val in multipliers: # take all the Indexing values from January
            for index in mult_months:
                val.append(index)
                #print sum(val)

        print len(multiplier_Jans)

        ###################################################################

        #plt.plot(months, avg_months)
        #plt.yticks()
        #plt.show()

        #####################################################################




        season = season_determine(month)

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
        boffice = []
        names = []

        for col in year_sort:
            #print col[0], ': ', col[8]

            if z == 0:
                z += 1
                continue


            names.append(col[0])
            boffice.append(float(col[10]))


            # print 'name: ', col[0], '\nbudget:', col[9], '-->', 'multiplier: ', col[11]
            z += 1

        print len(boffice)
        #print boffice
        print len(names)
        #plt.plot(boffice)
        #plt.yticks(boffice, names)
        #plt.grid()
        #lt.show()


if __name__ == '__main__':
        main()
