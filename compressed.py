import os
import sys
import csv 
import matplotlib.pyplot as plt
        #####################################################################
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
        #####################################################################
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
        Jans = [index for index in range(1,len(month)) if month[index] == 'Jan']
        Febs = [index for index in range(1,len(month)) if month[index] == 'Feb']
        Mar = [index for index in range(1,len(month)) if month[index] == 'Mar']
        Apr = [index for index in range(1,len(month)) if month[index] == 'Apr']
        May  = [index for index in range(1,len(month)) if month[index] == 'May']
        June = [index for index in range(1,len(month)) if month[index] == 'Jun']
        July = [index for index in range(1,len(month)) if month[index] == 'Jul']
        Aug = [index for index in range(1,len(month)) if month[index] == 'Aug']
        Sep = [index for index in range(1,len(month)) if month[index] == 'Sep']
        Oct = [index for index in range(1,len(month)) if month[index] == 'Oct']
        Nov = [index for index in range(1,len(month)) if month[index] == 'Nov']
        Dec = [index for index in range(1,len(month)) if month[index] == 'Dec']
        NONE = [index for index in range(1,len(month)) if month[index] == 'N/A']
        # There are over 200 entries that are N/A !
        #####################################################################
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
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        avg_months = [];
        #### Averages for the months and their respective multipliers #####
        avg_months.append(sum(multiplier_Jans)/ (len(multiplier_Jans)))
        avg_months.append(sum(multiplier_Feb)/ (len(multiplier_Feb)))
        avg_months.append(sum(multiplier_Mar)/ (len(multiplier_Mar)))
        avg_months.append(sum(multiplier_Apr)/ (len(multiplier_Apr)))
        avg_months.append(sum(multiplier_May)/ (len(multiplier_May)))
        avg_months.append(sum(multiplier_June)/ (len(multiplier_June)))
        avg_months.append(sum(multiplier_July)/ (len(multiplier_July)))
        avg_months.append(sum(multiplier_Aug)/ (len(multiplier_Aug)))
        avg_months.append(sum(multiplier_Sep)/ (len(multiplier_Sep)))
        avg_months.append(sum(multiplier_Oct)/ (len(multiplier_Oct)))
        avg_months.append(sum(multiplier_Nov)/ (len(multiplier_Nov)))
        avg_months.append(sum(multiplier_Dec)/ (len(multiplier_Dec)))
        ###################################################################
        plt.figure(1)
        plt.clf
        plt.plot(months,avg_months)
        plt.ylabel('Multiplier (Budget/Box Office)')
        plt.xlabel('Month [Jan-Dec]')
        plt.title('Multiplier V.S. Month')
        plt.show()
        #####################################################################
        avg_seasons = []
        avg_seasons.append((avg_months[5]+avg_months[6]+avg_months[7]) / 3) # Summer
        avg_seasons.append((avg_months[8]+avg_months[9]+avg_months[10]) / 3) # Fall
        avg_seasons.append((avg_months[2]+avg_months[3]+avg_months[4]) / 3) # Spring
        avg_seasons.append((avg_months[0]+avg_months[1]+avg_months[11]) / 3) # Winter
        avg_seasons.append((avg_months[5]+avg_months[6]+avg_months[7]) / 3) # Summer
        season = [1,2,3,4,5] # Summer -> Fall -> Spring -> Winter
        #####################################################################
        plt.figure(2)
        plt.clf
        plt.plot(season,avg_seasons)
        plt.ylabel('Multiplier (Budget/Box Office)')
        plt.xlabel('Month [Summer -> Fall -> Winter -> Spring]')
        plt.title('Multiplier V.S. Season')
        plt.show(