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
    city=()
    check=True
    while check:
        city=input('Would you like to see data for Chicago, New York City or Washington?')

        if city.lower()=='chicago':
            check=False
        elif city.lower()=='new york city':
            check=False
        elif city.lower()=='washington':
            check=False
    if city.lower()=='chicago':
        city_info=pd.read_csv('chicago.csv')
    elif city.lower()=='new york city':
        city_info=pd.read_csv('new_york_city.csv')
    elif city.lower()=='washington':
        city_info=pd.read_csv('washington.csv')


    # TO DO: get user input for month (all, january, february, ... , june)

    df=city_info
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    month=()
    check=True
    while check:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=input('Would you like to filter data by month? If yes choose month. If no type "all". ')
        month=month.lower()
        if month in months:
           month = months.index(month) +1
           df=df[df['month']==month]
           check=False
        elif month=='all':
           check=False




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    day=()
    check=True
    while check:
        day=input('Would you like to filter data by day?. if yes pleas specify the day. If no please type "all". ')
        day=day.title()
        print(day)
        if day != 'All':
            df = df[df['day_of_week']==day]
            check=False
        elif day=='All':
            check=False

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month!='all':
        df=df[df['month']==month]
    if day!='All':
        df=df[df['day_of_week']==day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print('most common month is ',common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.weekday_name
    common_day=df['day'].mode()[0]
    print('most common day is ',common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation=df['Start Station'].mode()[0]
    print('most common start station is',common_sstation)
    # TO DO: display most commonly used end station
    common_estation=df['End Station'].mode()[0]
    print('most common end station is',common_estation)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination=(df['Start Station']+ " to " + df['End Station']).mode()[0]
    print ('most frequent comination of start and end station trip is ',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time is ',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time is ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user types: ',user_types)



    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('count of gender: ',gender)
    except KeyError:
        print('Gender column does not exist')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        print('earliest birth year is ',earliest)
        recent=df['Birth Year'].max()
        print('most recent birth year is ',recent)
        common=df['Birth Year'].mode()[0]
        print('most common birth year is ',common)
    except KeyError:
        print('Birth year column does not exist')

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

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while view_data.lower()!='no':
            print(df.iloc[0:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ")


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
