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
  # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputswhile True:
  while True: 
          city = input("Which city would you like to filter by? Washington, Chicago or New York City?") 
          city = city.lower() 
          if city in ['washington', 'new york city', 'chicago']: 
              break 
          else: 
              print("Sorry, invalid data")
      # TO DO: get user input for month (all, january, february, ... , june)
  while True:
          month = input("Filter by specific month. Input month name from within first 6 months or else type 'all'")
          month = month.lower()
          if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
              break 
          else: 
              print("Sorry, invalid data")
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
  while True: 
          day = input("Do you want data extracted for a specific day? If yes, type the name of the day or else type 'all'") 
          day = day.lower() 
          if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'Sunday', 'all']: 
              break 
          else: 
              print("Sorry, invalid data")
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

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of the week if possible
    if day != 'all':
        # filter by day of the week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0] 
    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0] 
    print('Most popular day of the week:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    popular_hour = df['hour'].mode()[0] 
    print('Most Popular Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax() 
    print('Most frequently used start station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax() 
    print('Most frequently used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station'] 
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time", df['Trip Duration'].sum(), "\n")


    # TO DO: display mean travel time
    print("Total mean time", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type, "\n")
    

    # TO DO: Display counts of gender
    try: 
      gender_type = df['Gender'].value_counts() 
      print('\nGender Type:\n', gender_type) 
    except KeyError: 
      print("\nGender Type:\nNo data available")


    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
      Earliest_Year = df['Birth Year'].min() 
      print('\nEarliest Year:', Earliest_Year) 
    except KeyError: 
      print("\nEarliest Year:\nNo data available")
    
    try: 
      Most_Recent_Year = df['Birth Year'].max() 
      print('\nMost Recent Year:', Most_Recent_Year) 
    except KeyError: 
      print("\nMost Recent Year:\nNo data available.")
    
    try: 
      Most_Common_Year = df['Birth Year'].value_counts().idxmax() 
      print('\nMost Common Year:', Most_Common_Year) 
    except KeyError: 
      print("\nMost Common Year:\nNo data available")


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
    #TO DO: Set index to select the first five rows
    while True:
        print("\n")
        print(df.iloc[start_idx:end_idx].to_string())
        print("\n")

        start_idx = end_idx + 1
        end_idx = end_idx + 5

        raw_data = str(input("\nDo you want to print data? Type 'YES' to continue. Press any other key to proceed: ")).lower()
        if raw_data == 'yes':
            display_data(df, start_idx, end_idx)
        else:
            break
        break

        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
