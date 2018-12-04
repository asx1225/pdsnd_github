import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list={'all':0,'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6}
day_list={'everyday':7,'mon':0,'tue':1,'wed':2,'thr':3,'fri':4,'sat':5,'sun':6}
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
        try:
            city_input=str(input("please enter a city:(chicago, new york city,washington) "))
            city=city_input.lower()
            CITY_DATA[city]
            break
        except KeyError:
            print("OOPS! You must have a typo, please enter one more time!")

    filter_selection=input("Do you need filter for month and day ? (yes/no)")
    if filter_selection.lower()=='yes':
        while True:
            try:
                month_input=str(input("Please input a month from Jan to Jun with 3 letters or all :"))

                month=month_list[month_input.lower()]
                break
            except KeyError:
                print("please enter valid month !")
        while True:
            try:
                day_input=str(input("Please input a day from mon to sun with 3 letters or everyday :"))

                day=day_list[day_input.lower()]
                break
            except KeyError:
                print("please enter valid day !")
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sund
        city=city_input.lower()
        month=month_list[month_input.lower()]
        day=day_list[day_input.lower()]
    if filter_selection.lower()=='no':
        city=city_input.lower()
        month=month_list['all']
        day=day_list['everyday']

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
    df =pd.read_csv('./{}'.format(CITY_DATA[city]))
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    if month!=0:
        df=df[df['month']==month]
    if day!=7:
        df=df[df['day_of_week']==day]
    if (month==0 and day==7):
        df=df
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour']=df['Start Time'].dt.hour
    # TO DO: display the most common month

    for month_name,number in month_list.items():
        if number==df['month'].mode()[0]:
            most_common_month=month_name
    # TO DO: display the most common day of week

    for day_name,number in day_list.items():
        if number==df['day_of_week'].mode()[0]:
            most_common_day=day_name
    # TO DO: display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return print("most common month is {}".format(most_common_month),
                 "\n"
                 "most common day is {}".format(most_common_day),
                 '\n'
                 "most common hour is {}".format(most_common_hour))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    df["Start_to_end"]=df['Start Station']+" to "+df['End Station']
    most_common_combiunation_station=df["Start_to_end"].mode()[0]



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(print("most common start station is:{}".format(most_common_start_station),"\n",
                 "most common end station is:{}".format(most_common_end_station),"\n",
                 "most combination station is:{}".format(most_common_combiunation_station)))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return print("total travel time is:{} minutes and {} seconds".format(total_travel_time//60,total_travel_time%60),"\n",
                 "mean travel time is:{} minutes and {} seconds".format(mean_travel_time//60,mean_travel_time%60),"\n")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    try:
        gender=df['Gender'].value_counts()
        a=df.sort_values('Birth Year').head(1).index.tolist()[0]
        earliest_year=df.sort_values('Birth Year').head(1)['Birth Year'][a]
        b=df.sort_values('Birth Year',ascending=False).head(1).index.tolist()[0]
        most_recent_year=df.sort_values('Birth Year',ascending=False).head(1)['Birth Year'][b]
        most_common_year=df['Birth Year'].mode()[0]
        return print("user type summary is \n {}".format(user_type),"\n",
                         "gender summary is \n {}".format(gender),"\n",
                         "earliest year of birth is \n {}".format(earliest_year),"\n",
                         "most recent year of birth is \n {}".format(most_recent_year),"\n",
                         "most common year of birth is \n {}".format(most_common_year),"\n")


    except KeyError:
        print("No gender, birth year data for Washington! Sorry! ")

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Raw_data(df):
    question=input("would you like raw data ? (yes or no)")
    if question =='yes':
        print(df)


def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
