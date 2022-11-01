import pandas as pd
from datetime import datetime
from datetime import timedelta

# Helper function to create a new dataframe with unconfigured bins
def initialize_bins(
        bin_size_mins, 
        start_date, 
        start_time, 
        end_date, 
        end_time
    ):
    # initialize empty dataframe
    bins = pd.DataFrame(columns=["date","time","total"])

    # Read in the start and end arguments as a datetime objects
    start_datetime = datetime.strptime(f'{start_date} {start_time}', '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(f'{end_date} {end_time}', '%Y-%m-%d %H:%M:%S')

    

    # For clarity, create a new datetime object with the minutes to the lowest divider of the start time
    start_bin = datetime(
        year = start_datetime.year,
        month = start_datetime.month,
        day = start_datetime.day,
        hour = start_datetime.hour,
        minute = start_datetime.minute - start_datetime.minute % bin_size_mins,
        second = 0
    ) 

    # Set the end bin
    end_bin = datetime(
        year = end_datetime.year,
        month = end_datetime.month,
        day = end_datetime.day,
        hour = end_datetime.hour,
        minute = end_datetime.minute - end_datetime.minute % bin_size_mins,
        second = 0
    )

    # Create a time delta the with the binsize
    delta = timedelta(minutes=bin_size_mins)

    # Iterate through the range of dates
    current_bin = start_bin
    while current_bin != end_bin:
        # Add datetime row to the bins if end is not reached
        bins.loc[len(bins.index)] = [current_bin.strftime('%Y-%m-%d'), current_bin.strftime('%H:%M:%S'), -1]

        # Increase the current bin with the time delta
        current_bin += delta

    return bins

# Helper function to fill the bins with the raw data
def occupy_bins(raw_data, empty_bins):
    # Create a new colmun in the bins dataframe that contains both the date and time and set it as index
    empty_bins['datetime'] = empty_bins['date'] + ' ' + empty_bins['time']
    empty_bins.set_index('datetime', drop=True, inplace=True)

    # Convert the dataframe to a dict for O(1) indexing
    empty_bins_dict = empty_bins.to_dict(orient = 'index')

# Helper function to create a new dataframe with unconfigured bins
def define_bins(
        bin_size_mins, 
        start_date, 
        start_time, 
        end_date, 
        end_time
    ):
    # initialize empty dataframe
    bins = pd.DataFrame(columns=["date","time","total"])

    # Read in the start and end arguments as a datetime objects
    start_datetime = datetime.strptime(f'{start_date} {start_time}', '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(f'{end_date} {end_time}', '%Y-%m-%d %H:%M:%S')

    # For clarity, create a new datetime object with the minutes to the lowest divider of the start time
    start_bin = datetime(
        year = start_datetime.year,
        month = start_datetime.month,
        day = start_datetime.day,
        hour = start_datetime.hour,
        minute = start_datetime.minute - start_datetime.minute % bin_size_mins,
        second = 0
    ) 

    # Set the end bin
    end_bin = datetime(
        year = end_datetime.year,
        month = end_datetime.month,
        day = end_datetime.day,
        hour = end_datetime.hour,
        minute = end_datetime.minute - end_datetime.minute % bin_size_mins,
        second = 0
    )

    # Create a time delta the with the binsize
    delta = timedelta(minutes=bin_size_mins)

    # Iterate through the range of dates
    current_bin = start_bin
    while current_bin != end_bin:
        # Add datetime row to the bins if end is not reached
        bins.loc[len(bins.index)] = [current_bin.strftime('%Y-%m-%d'), current_bin.strftime('%H:%M:%S'), -1]

        # Increase the current bin with the time delta
        current_bin += delta

    return bins