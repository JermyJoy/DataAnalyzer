def min_remove(length_of_movie):
    for index in range(1,len(length_of_movie)):
        length_of_movie[index] = length_of_movie[index].strip(' min')
