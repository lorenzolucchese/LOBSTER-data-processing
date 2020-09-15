# LOBSTER-data-processing

Pre-processing code for data downloaded from LOBSTER (https://lobsterdata.com/). The data from the orderbook and message files (for a specific ticker) is merged in order to create an equispaced time series of log returns. 

## Input: 	

The data downloaded from LOBSTER needs to be stored in the repository 'current_path/data/TICKER/TICKER_extracted_data' and possibly subdivided per month.
In each folder a trading day is represented by two .csv files, the message and orderbook files as downloaded from LOBSTER.
In the 'TICKER' folder 'TICKER_equidistant_log_returns' and 'TICKER_supplementary_files' folders need to be created.
The variable 'nmin', the time delta at which data is required, needs to be selected (for example 1-min spaced data).

## Code:

data_to_equidistant_timeseries.py reads all .csv files in the 'TICKER_extracted_data' folder and loops through them:

1. For each trading day the orderbook file is read as a dataframe (with columns 'ASKp1', 'ASKs1', 'BIDp1', 'BIDs1') and the corresponding times are read off the message file (in datetime form).

2. The orderbook is reduced to only the rows corresponding to the equispaced time points (more specifically the last orderbook row before each time point is selected, except for the opening price). 

3. The prices at the equispaced time points are computed using a weighted average of the BID-ASK prices and the correct time-indexing is assigned.

4. The log-returns are then computed by logarithmic differencing and stored in the 'TICKER_equidistant_log_returns' folder as .csv files named 'nmin_date.csv'.

merge_csv.py then merges all the .csv files in the 'TICKER_equidistant_log_returns' into one named 'TICKER_preprocessed_data.csv'. (note that .csv files can be removed/added before merging).

## Output: 

The data is hence returned in both the 'TICKER_equidistant_log_returns' folder as one .csv file per day and in a single merged file named 'TICKER_preprocessed_data.csv'.

Supplementary files produced, to check before using the data, are:
	
	'nmin_skipped_messages': message files which pandas didn't manage read
	
	'nmin_skipped_orderbook': orderbook files which pandas didn't manage read

	'nmin_empty_time_intervals': trading days where data is scarse (i.e. there are time-intervals without transactions and the price is henced assumed to not change).

	'nmin_opening_closing_times': trading days with "strange" opening and closing times (i.e. which are not 9:30-16:00)
