import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city = input('Please, enter the city name you would like to explore (chicago, new york city, washington):').lower()
month = input('Please, enter the month name you would like to explore (all, january, february, ..., june), for all months enter (all):').lower()
day = input('Please, enter the day name you would like to explore (all, monday, tuesday, ... sunday), for popular day enter (all):').lower()


def get_filters(city, month, day):
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#     city = input('Please, enter the city name you would like to explore (chicago, new york city, washington):') 
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('The avaliable data are only for (chicago, new york city, washington):').lower() 


    # TO DO: get user input for month (all, january, february, ... , june)
#     month = input('Please, enter the city name you would like to explore (all, january, february, ..., june):') 
    while month not in ['all', 'january', 'february', 'march','april','may','june']:
        month = input('The valid month entry can be only (all, january, february, ..., june):').lower()
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
#     day = input('Please, enter the city name you would like to explore (all, monday, tuesday, ... sunday):') 
    while day not in ['all', 'sunday', 'monday', 'tuesday','wednesday','thursday','friday']:
        day = input('The valid day entry can be only (all, monday, tuesday, ... sunday):').lower() 
    
    
    
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) +1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    global    month
    months_dict = {1: 'January' , 2: 'February', 3:'March', 4:'April',5:'May',6:'June'}
    global day
    if month == 'all':
        popular_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month_name = months_dict[popular_month_num]
        print('most common month:', popular_month_name)
    else:
        print('To get most popular month please input -all- during the start')


    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['Start Time'].dt.weekday_name.mode()[0]
        print('most common day:', popular_day)
    else:
        print('To get most popular day please input -all- during the start')
    


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('most common hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('common start station is ', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('common end station is ', common_end_station)

    # display most frequent combination of start station and end station trip
    trips = 'from '+ df['Start Station'] + ' to ' + df['End Station']
    common_trip = trips.mode()[0]
    print('Frequent trip is' ,common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is :', total_travel_time )


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is :', mean_travel_time )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def user_stats(df):
    """Displays statistics on bikeshare users."""
    global city
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('user type counts are',  user_type_counts)


    # TO DO: Display counts of gender
    if  city == 'washington':
        print ('For washington No Data are available related to gender counts')
    else:
      
        print('user type counts are', df['Gender'].value_counts())        
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if  city == 'washington':
        print ('For Washington No Data are available related to year of birth')
    else:
  
        print('earliest year of birth is', df['Birth Year'].min())
        print('most recent year of birth is', df['Birth Year'].max()) 
        print('common year of birth is', df['Birth Year'].mode()[0]) 
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    
    


def main():
    global city
    global month
    global day
    
    while True:
        
        city,  month,  day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data = input('would you like to see 5 lines of the full data, press yes or no?').lower()
        if display_data == 'yes':
            row_num = 5
            print(df.iloc[:row_num])
            more_data = input ('for more data to be displayed enter yes otherwise press no: ').lower()
            while more_data == 'yes':
                row_num += 5
                print(df.iloc[:row_num])
                if more_data == 'yes':
                    more_data = input ('for more press yes otherwise press no: ').lower()
                    continue
                
                
                
            else:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
                
        

        


if __name__ == "__main__":
	main()
