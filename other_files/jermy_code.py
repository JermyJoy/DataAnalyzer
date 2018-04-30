import os
import sys
import csv
import matplotlib.pyplot as plt

def season_determine(val):
        month_seasons = {"Jan" : "Winter", "Feb" : "Winter", "Dec" : "Winter", "Mar" : "Spring", "Apr" : "Spring", "May" : "Spring", "Jun" : "Summer", "Jul" : "Summer", "Aug" : "Summer", "Sep" : "Fall", "Oct" : "Fall", "Nov" : "Fall" };
        for i in range(1,len(val)):
                if val[i] in month_seasons:
                        val[i] = month_seasons[val[i]]
        return val

def main():
        month = []; # 7
        meta = []; # 4
        name = []; # 0
        prod = []; # 1
        age = []; # 2
        imdb = []; # 3
        num_votes = []; # 5
        day = []; # 6
        year = []; # 8
        budget = []; # 9
        box_office = []; # 10
        multiplier = []; # 11

        print "starting..."
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

        ######################################################################
        Jans = []
        Febs = []
        Mar = []
        Apr = []
        May  = []
        June = []
        July = []
        Aug = []
        Sep = []
        Oct = []
        Nov = []
        Dec = []
        NONE = []
        for index in range(1,len(month)):
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

        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        avg_months = []
        #### Averages for the months and their respective multipliers #####
        for val in Jans:
                multiplier_Jans.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Jans)/ (len(multiplier_Jans) -1))
        for val in Febs:
                multiplier_Feb.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Feb)/ (len(multiplier_Feb) - 1))
        for val in Mar:
                multiplier_Mar.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Mar)/ (len(multiplier_Mar) - 1))
        for val in Apr:
                multiplier_Apr.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Apr)/ (len(multiplier_Apr) - 1))
        for val in May:
                multiplier_May.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_May)/ (len(multiplier_May) - 1))
        for val in June:
                multiplier_June.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_June)/ (len(multiplier_June) - 1))
        for val in July:
                multiplier_July.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_July)/ (len(multiplier_July) - 1))
        for val in Aug:
                multiplier_Aug.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Aug)/ (len(multiplier_Aug) - 1))
        for val in Sep:
                multiplier_Sep.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Sep)/ (len(multiplier_Sep) - 1))
        for val in Oct:
                multiplier_Oct.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Oct)/ (len(multiplier_Oct) - 1))
        for val in Nov:
                multiplier_Nov.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Nov)/ (len(multiplier_Nov) - 1))
        for val in Dec:
                multiplier_Dec.append(float(multiplier[val]))
        avg_months.append(sum(multiplier_Dec)/ (len(multiplier_Dec) - 1))
        ###################################################################

        plt.plot(months,avg_months)
        plt.yticks()
        plt.show()

        #####################################################################

        season = season_determine(month) # changing all the months to seasons !
        # will remove months from the original array so do this later
        #remove the header
        name = name[1:]
        prod = prod[1:]
        age = age[1:]
        imdb = imdb[1:]
        meta = meta[1:]
        num_votes = num_votes[1:]
        day = day[1:]
        month = month[1:]
        year = year[1:]
        budget = budget[1:]
        box_office = box_office[1:]
        multiplier = multiplier[1:]



if __name__ == '__main__':
        main()
