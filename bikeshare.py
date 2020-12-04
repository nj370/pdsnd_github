import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('type the city that you would like to analyse. new york city, chicago or washington?\n')
        if city in CITY_DATA:
          break
        else:
            print("error\n")
            continue
        

    # TO DO: get user input for month (all, january, february, ... , june)
    
    
    while True:
        month = input("would you like to filter the data by month? January, February, March, April, May, June. Type 'all' if you do not have any preference?\n")
        if month in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
          break
        else:
            print("error\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('what day? (all, monday, tuesday, ... sunday\n')
        if day in ('all', 'monday', 'tuesday',' wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
          break
        else:
           print("error\n")
           continue



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
    df['day'] = df['Start Time'].dt.weekday_name
   

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
      

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('common month:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('common day of the week:', df['day'].mode()[0])

    # TO DO: display the most common start hour
    
    print('common start hour', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('common start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('common end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combi'] = df['Start Station'] + ': ' + df['End Station']
    print('most frequent combination of start station and end station trip:', df['combi'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time (in minutes):', df['Trip Duration'].sum()/ 60)
        
    # TO DO: display mean travel time
    print('mean travel time (in minutes):', df['Trip Duration'].mean()/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
      print('counts of gender:', df['Gender'].value_counts())
    except KeyError:
      print('Keyerror')
    # TO DO: Display earliest, most recent, and most common year of birth
     # TO DO: Display counts of gender
    try:
      print('earliest year of birth:', df['Birth Year'].min())
    except KeyError:
      print('data does not exist')
   
    try:
      print('most recent year of birth:', df['Birth Year'].max())
    except KeyError:
      print('data does not exist')
      
    try:
      print('most recent year of birth:', df['Birth Year'].mode()[0])
    except KeyError:
      print('data does not exist')

  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        i=0
        while True:
            rawdata= input('yes or no')
            if rawdata == 'yes':
             rows=df.iloc[:i+5]
             print(rows)
             i+=5
            else:
                break
      
                
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

