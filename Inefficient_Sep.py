import csv
import os
import sys

def main():
    print ('starting to analyze...')
######### A VERY INEFFICIENT NUMBER OF ARRAYS ###########
    name_of_movie = [];
    length_of_movie = [];
    release_date = [];
    production  = [];
    imbd_rating = [];
    meta_rating = [];
    age_rating = [];
    num_votes = [];
    budget = [];
    Box_office = [];
#########################################################

    with open('NBCU_data.csv','r') as csv_file:
        reading = csv.reader(csv_file);
        for lines in reading:
            # Depending on the column can append more data into an array
            name_of_movie.append(lines[1]); # movie name is in the 1st index
            length_of_movie.append(lines[13]); # length of movie in mins is in the 13th index
            release_date.append(lines[12]); # release date of movie in the 12th index
            production.append(lines[7]) # production company in 7th index
            imbd_rating.append(lines[4]) # imbd rating in the 4th index
            meta_rating.append(lines[5]) # meta critic rating in the 5th index
            age_rating.append(lines[3]) # movie rating in the 3rd index 
            num_votes.append(lines[9]) # number of votes in the 9th index 
            budget.append(lines[17]) # budget in the 17th index 
            Box_office.append(lines[18]) # profites in the 18th index 


########### TEMP PRINT STATEMENTS #############
        print(name_of_movie[1]) 
        print(length_of_movie[1]) 
        print(release_date[1])
        print(production[1])
        print(imbd_rating[1])
        print(meta_rating[1])
        print(age_rating[1])
        print(num_votes[1])
        print(budget[1])
        print(Box_office[1])

if __name__ == '__main__':
    main();
