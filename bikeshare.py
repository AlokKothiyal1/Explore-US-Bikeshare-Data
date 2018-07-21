import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n**********Hello! Let\'s explore some US bikeshare data!**********')
    city =''

    # get user input for city (chicago, new york city, washington).
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\n\nWhich City\'s Bikeshare Data would you like to analyze? \'Chicago\', \'New York \', or \'Washington\'?-->\n')
        if city.lower() not in ['chicago', 'new york', 'washington']:
            print('\n----------Invalid City..Please Try Again----------')
        else:
            print('\n_______________Alright, {} it is!________________'.format(city.title()))



    user_filter =''
    while user_filter.lower() not in ['month','day','all']:
        user_filter= input('\nHow would you like to Filter the Data: By--> Month , Day, or Not at all. Type \"all\" for no Time Filter\n')
        if user_filter.lower() not in ['month','day','all']:
            print('\n----------Invalid Filter Type..Please Try Again!----------\n')
        else:
            print('\n_______________{} Filter applied!!!!_______________\n'.format(user_filter.title()))

    # get user input for month (all, january, february, ... , june)
    if user_filter.lower() == 'month':
        day ='all'
        month_list = ['january','february','march','april','may', 'june']
        month =''
        while month.lower() not in month_list:
            month =input('\nWhich Month? Like:- \'January\',\'February\',\'March\',\'April\',\'May\', or\'June?\n')
            if month.lower() not in month_list:
                print('----------Invalid month name..Please Try again----------')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif user_filter.lower() == 'day':
        month ='all'
        day_list =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=''
        while day.lower() not in day_list:
            day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
            if day.lower() not in day_list:
                print('\n----------Invalid Day Name....Please Try again----------')
    elif user_filter.lower() =='all':
        month ='all'
        day   ='all'



    print('-'*40)
    #just print some bike figures
    print('      __o'*10)
    print('     -\<,'*10)
    print('.....O/ O'*10)

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month_index = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = months[common_month_index-1]
    print('Most Common Month:--->',common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day Of Week:--->',common_day_of_week)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:--->', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip:...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Common Start Station:--->',common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common End Station:--->',common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip']=df.apply(lambda x:'%s TO %s' % (x['Start Station'],x['End Station']),axis=1)
    print('The most frequent combination of start station & end station trip:--->',df['Trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration:...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:--->',df['Trip Duration'].sum())


    # display mean travel time
    print('Mean Travel Time:--->',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#calculates user_stats for 'chicago' & 'new york' cities
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User types:--->\n',df['User Type'].value_counts())

    # Display counts of gender
    print('Counts of gender:--->\n',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('Earliest Year Of Birth:--->\n',df['Birth Year'].min())
    print('Most Recent Year Of Birth:--->\n',df['Birth Year'].max())
    print('Most Common Year Of Birth:--->\n',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#calculates user_stats for washington city
def user_stats_washington(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('Counts of User types:--->\n',df['User Type'].value_counts())
    print('----------Gender and Year of Birth Details not available----------')







    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#Display Raw Data
def raw_data(df_2):
    """Displays Raw Data to USer."""
    #counter is variable to calcuate next 5 rows of raw data
    counter=5
    show_data =input('\nWould You Like To See Raw Data?-->Yes or Stop\n')

    if show_data.lower() =='yes':
        print(df_2.head(5))
        print('-'*40)
    elif show_data.lower()=='stop':
        show_data = 'stop'
        return show_data
    else:
        print('-----Invalid Input...Please try Again-----')
        raw_data(df_2)

    while show_data.lower() != 'stop':
        show_data = input('\nWould You Like To See 5 more Raw Data?-->Yes or Stop\n')
        if show_data.lower() not in ['yes','stop']:
            print("-----Invalid input!..Please Try Again-----")
        elif show_data.lower() =='stop':
            return

        else:
            print(df_2.iloc[counter:counter+5,:])
            print('-'*40)
            counter+=5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df_2 = pd.read_csv(CITY_DATA[city.lower()])

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city.lower() !='washington':
            user_stats(df)
        else:
            user_stats_washington(df)
        raw_data(df_2)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
