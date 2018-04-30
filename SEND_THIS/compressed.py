#!/usr/bin/env python

import os
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

#####################################################################


def main():
        print "starting..."
    
        # initializing the colunms
        #
        name = []
        prod = []
        age = []
        imdb = []
        day = []
        month = []
        year = []
        multiplier = []

        # initializing constants
        #
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Summer -> Fall -> Spring -> Winter
        #
        season = [1, 2, 3, 4, 5]
        season_divison = 12/4

        # initializing variables
        #
        avg_months = []
        avg_seasons = []
        avg_rating = []


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
                        day.append(row[6])
                        month.append(row[7])
                        year.append(row[8])
                        multiplier.append(row[11])


#####################################################################

        # store the row indeces of each month in a separate list
        # There are over 200 entries that are N/A !
        #
        Jans = [index for index in range(1, len(month)) if month[index] == 'Jan']
        Febs = [index for index in range(1, len(month)) if month[index] == 'Feb']
        Mar = [index for index in range(1, len(month)) if month[index] == 'Mar']
        Apr = [index for index in range(1, len(month)) if month[index] == 'Apr']
        May = [index for index in range(1, len(month)) if month[index] == 'May']
        June = [index for index in range(1, len(month)) if month[index] == 'Jun']
        July = [index for index in range(1, len(month)) if month[index] == 'Jul']
        Aug = [index for index in range(1, len(month)) if month[index] == 'Aug']
        Sep = [index for index in range(1, len(month)) if month[index] == 'Sep']
        Oct = [index for index in range(1, len(month)) if month[index] == 'Oct']
        Nov = [index for index in range(1, len(month)) if month[index] == 'Nov']
        Dec = [index for index in range(1, len(month)) if month[index] == 'Dec']

        NONE = [index for index in range(1, len(month)) if month[index] == 'N/A']

        # get the movie multiplier of each month indices
        #
        multiplier_Jans = [float(multiplier[val]) for val in Jans]
        multiplier_Feb = [float(multiplier[val]) for val in Febs]
        multiplier_Mar = [float(multiplier[val]) for val in Mar]
        multiplier_Apr = [float(multiplier[val]) for val in Apr]
        multiplier_May = [float(multiplier[val]) for val in May]
        multiplier_June = [float(multiplier[val]) for val in June]
        multiplier_July = [float(multiplier[val]) for val in July]
        multiplier_Aug = [float(multiplier[val]) for val in Aug]
        multiplier_Sep = [float(multiplier[val]) for val in Sep]
        multiplier_Oct = [float(multiplier[val]) for val in Oct]
        multiplier_Nov = [float(multiplier[val]) for val in Nov]
        multiplier_Dec = [float(multiplier[val]) for val in Dec]

        # getting the average of each month multiplier
        # and store then in avg_months
        #
        avg_months.append(sum(multiplier_Jans) / (len(multiplier_Jans)))
        avg_months.append(sum(multiplier_Feb) / (len(multiplier_Feb)))
        avg_months.append(sum(multiplier_Mar) / (len(multiplier_Mar)))
        avg_months.append(sum(multiplier_Apr) / (len(multiplier_Apr)))
        avg_months.append(sum(multiplier_May) / (len(multiplier_May)))
        avg_months.append(sum(multiplier_June) / (len(multiplier_June)))
        avg_months.append(sum(multiplier_July) / (len(multiplier_July)))
        avg_months.append(sum(multiplier_Aug) / (len(multiplier_Aug)))
        avg_months.append(sum(multiplier_Sep) / (len(multiplier_Sep)))
        avg_months.append(sum(multiplier_Oct) / (len(multiplier_Oct)))
        avg_months.append(sum(multiplier_Nov) / (len(multiplier_Nov)))
        avg_months.append(sum(multiplier_Dec) / (len(multiplier_Dec)))

        # getting the average multiplier of each season
        # Summer = [May, June, July]
        # Fall = [Aug, Sep, Oct]
        # Winter = [Nov, Dec, Jan]
        # Spring = [Feb, Mar, Apr]
        #
        avg_seasons.append((avg_months[5] + avg_months[6]+avg_months[7]) / season_divison)
        avg_seasons.append((avg_months[8] + avg_months[9]+avg_months[10]) / season_divison)
        avg_seasons.append((avg_months[2] + avg_months[3]+avg_months[4]) / season_divison)
        avg_seasons.append((avg_months[0] + avg_months[1]+avg_months[11]) / season_divison)
        avg_seasons.append((avg_months[5] + avg_months[6]+avg_months[7]) / season_divison)

        # getting the ratings of the movies in each month
        #
        rating_Jan = [float(imdb[val]) for val in Jans if imdb[val] != '']
        rating_Feb = [float(imdb[val]) for val in Febs if imdb[val] != '']
        rating_Mar = [float(imdb[val]) for val in Mar if imdb[val] != '']
        rating_Apr = [float(imdb[val]) for val in Apr if imdb[val] != '']
        rating_May = [float(imdb[val]) for val in May if imdb[val] != '']
        rating_June = [float(imdb[val]) for val in June if imdb[val] != '']
        rating_July = [float(imdb[val]) for val in July if imdb[val] != '']
        rating_Aug = [float(imdb[val]) for val in Aug if imdb[val] != '']
        rating_Sep = [float(imdb[val]) for val in Sep if imdb[val] != '']
        rating_Oct = [float(imdb[val]) for val in Oct if imdb[val] != '']
        rating_Nov = [float(imdb[val]) for val in Nov if imdb[val] != '']
        rating_Dec = [float(imdb[val]) for val in Dec if imdb[val] != '']

        # getting the average rating of each month
        #
        avg_rating.append(sum(rating_Jan)/len(rating_Jan))
        avg_rating.append(sum(rating_Feb)/len(rating_Jan))
        avg_rating.append(sum(rating_Mar)/len(rating_Feb))
        avg_rating.append(sum(rating_Apr)/len(rating_Mar))
        avg_rating.append(sum(rating_May)/len(rating_May))
        avg_rating.append(sum(rating_June)/len(rating_June))
        avg_rating.append(sum(rating_July)/len(rating_July))
        avg_rating.append(sum(rating_Aug)/len(rating_Aug))
        avg_rating.append(sum(rating_Sep)/len(rating_Sep))
        avg_rating.append(sum(rating_Oct)/len(rating_Oct))
        avg_rating.append(sum(rating_Nov)/len(rating_Nov))
        avg_rating.append(sum(rating_Dec)/len(rating_Dec))
#
        # dividing the ratings into five parts according to the imd rating
        # and getting the multiplier of each part.
        #
        ratings = [float(imdb[val]) for val in range(1,len(imdb)) if imdb[val] != '']

        lowest_rating = [val for val in range(1,len(ratings)) if ratings[val] <= 2]
        budget_lowest_rating = [float(multiplier[val]) for val in lowest_rating]

        lower_rating = [val for val in range(1,len(ratings)) if ratings[val] > 2 and ratings[val] <= 4]
        budget_lower_rating = [float(multiplier[val]) for val in lower_rating]

        mid_rating = [val for val in range(1,len(ratings)) if ratings[val] > 4 and ratings[val] <= 6]
        budget_mid_rating = [float(multiplier[val]) for val in mid_rating]

        higher_rating = [val for val in range(1,len(ratings)) if ratings[val] > 6 and ratings[val] <= 8]
        budget_higher_rating  = [float(multiplier[val]) for val in higher_rating]

        highest_rating = [val for val in range(1,len(ratings)) if ratings[val] > 8 and ratings[val]<= 10]
        budget_highest_rating = [float(multiplier[val]) for val in highest_rating]

        # geting the average multiplier of each rating part
        #
        avg_budget = [np.mean(budget_lowest_rating), np.mean(budget_lower_rating), np.mean(budget_mid_rating),
                    np.mean(budget_higher_rating), np.mean(budget_highest_rating)]


        # getting the rating by season
        #  and geting the average rating of each season
        #
        winter = (rating_Jan + rating_Dec + rating_Feb)
        winter_rating = np.mean([val for val in winter])

        spring = (rating_Mar + rating_Apr + rating_May)
        spring_rating = np.mean([val for val in spring])

        fall   = (rating_Sep + rating_Oct + rating_Nov)
        fall_rating = np.mean([val for val in fall])

        summer = (rating_June + rating_July + rating_Aug)
        summer_rating = np.mean([val for val in summer])

        avg_season_rating = [summer_rating, fall_rating, winter_rating, spring_rating]


#####################################################################
        # PLOTING THE GRAPHS
        #

        # ploting the average multiplier of each month VS the month
        #
        plt.figure(1)
        plt.clf
        plt.plot(months, avg_months)
        plt.ylabel('Multiplier (Budget/Box Office)')
        plt.xlabel('Month [Jan-Dec]')
        plt.title('Multiplier V.S. Month')

        # ploting the average multiplier of each season VS the season
        #
        plt.figure(2)
        plt.clf
        plt.plot(season, avg_seasons)
        plt.ylabel('Multiplier (Budget/Box Office)')
        plt.xlabel('Month [Summer -> Fall -> Winter -> Spring]')
        plt.title('Multiplier V.S. Season')

        # ploting the average rating each month VS the month
        #
        plt.figure(3)
        plt.clf
        plt.plot(months, avg_rating)
        plt.ylabel('Multiplier (Budget/Box Office)')
        plt.xlabel('Month [Jan-Dec]')
        plt.title('Rating V.S. Month')

        # ploting the Average multiplier of each rating part and the ratings
        #
        plt.figure(4)
        plt.clf
        plt.plot([1, 2, 3, 4, 5], avg_budget)
        plt.title('Movie rating V.S. Average Multiplier')
        plt.xlabel('Rating {(0-2)=1, (2-4)=2, (4-6)=3, (6-8)=4, (8-10)=5})')
        plt.ylabel('Average Multiplier (Budget / Box Office)')

        # ploting the average season ratings VS season
        #
        plt.figure(5)
        plt.clf
        plt.plot([1, 2, 3, 4], avg_season_rating)
        plt.xlabel('Seasons {1=Summer, 2=Fall, 3=Winter, 4=Spring}')
        plt.ylabel('Average IMDB Rating [0-10]')
        plt.title('Season V.S. IMDB Rating')
        plt.show()


if __name__ == '__main__':
        main()
