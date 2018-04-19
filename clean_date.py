def clean_date(release_date):
        month = [];
        day = [];
        year = [];
        
        for date in range(1,len(release_date)):
            val = release_date[date].split('-')
            day.append(val[0]);
            try:
                if (val[0] == 'N/A' ):
                    month.append('N/A')
                    year.append('N/A');
                else:
                    month.append(val[1]);
                    year.append(val[2]);
            except IndexError:
                month.append('N/A')
                year.append('N/A')
                day.append('N/A')

        print(month[1]) # for first movie
        print(day[1]) # for first movie
        print(year[1]) # for first movie
