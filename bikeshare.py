import time
import pandas as pd
import numpy as np
import sys

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
        print("Please select the city")
        choise=input("""    
 Chicago
 New York City
 Washington:\n """)
          
        if 'chicago' in choise.lower() :
            city= CITY_DATA['chicago']
            break
        elif 'new york' in choise.lower() :
            city= CITY_DATA['new york city']
            break
        elif 'washington' in choise.lower() :
            city= CITY_DATA['washington']
            break
        print("Your choise is not in the list. Please select again!\n")           
        
      
 # TO DO: get user input for month (all, january, february, ... , june)     
    while True:
        print("\n")
        print("Please select mounth for filtering\n")
        choise2 = input("""
January
February
March
April
May
June 
All:\n """)
              
        if choise2.lower() in ['january', 'february', 'march', 'april', 'may', 'june',"all"]:
            month= choise2.lower()
            break
        print("Your choise is not in the list. Please select again!\n")
       
 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)            
    
    while True:
        print("\n")
        print("Please select weekday for filtering\n")
        choise3 = input("""
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday 
Sunday
All :\n """)
        if choise3.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',"sunday","all"]:
            day= choise3.lower()
            break
        print("Your choise is not in the list. Please select again!\n")
        
    print("\n\n")
    print(""" Data will be displayed for below criterias,
    {}
    {}
    {}""".format(choise,month,day))
    print('-'*40)
    return city,month,day

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print("Most Common Month:", common_month)

    # display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("Most Common day:", common_day)

    # display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Common Start Station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Common End Station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    
    
    
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_travel_combination = df['combination'].mode()[0]
    
    #frequent_travel_combination = df['Start Station'].mode()[0] and df['End Station'].mode()[0]
    print('Frequent Start & End Station: ', frequent_travel_combination)
    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time: {} minutes'.format(Total_Travel_Time))

    
    

    # display mean travel time
    print('Mean Travel Time: {} minutes'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('#'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Types:", user_types)
   
    # Display counts of gender
    while True:
        try:
            print('Gender Count: ',df['Gender'].value_counts())
            break
        except KeyError:
            print('Gender: NaN')
            break
     # Display earliest, most recent, and most common year of birth
    
    if str('Birth Year') in df:
        print('Earliest Birth Year: ', df['Birth Year'].min())
        print('Recent Birth Year:t', df['Birth Year'].max())
        print('Most Common Birth Year: ', df['Birth Year'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('#'*40)

def getdata(df):
    rawdata = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No\n").lower()
        if answer not in ['yes', 'no']:
            print("\nChoise is unclear. Please try again")
            answer = input("Do you want to see the raw data? Yes or No\n").lower()
        elif answer == 'yes':
            rawdata += 5
            print(df.iloc[rawdata : rawdata + 5])
            again = input("Do you want to see more? Yes or No\n").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return
        
def main():
    while True:
        try:
            city,month,day = get_filters()
            df = load_data(city,month,day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            getdata(df)
            
        except KeyboardInterrupt:
            print("\n")
            print ('Program has terminated by user!')
            sys.exit()
        except ValueError:
            print("\n\n")
            print('Wrong character executed, please try from beginning!')
            continue
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#new comment added