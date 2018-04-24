import os
import sys
import csv 


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
        with open('full_dataset.csv') as csv_file:
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
        season = season_determine(month)
        # for the months to store to dict....
        
if __name__ == '__main__':
        main();
