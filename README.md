# time_filter
you have a csv with a timestamp in? you can filter rows vs time with this tool!

Examples:

./time_filter.py -h
usage: time_filter.py [-h] [--delimiter DELIMITER] [--column COLUMN] [--timestamp_format TIMESTAMP_FORMAT] [--show_errors] [--dont_show_output] [--exit_on_error] [--eq EQ]
                      [--ne NE] [--lt LT] [--gt GT]

Do comparisons in timestamps from STDIN

optional arguments:
  -h, --help            show this help message and exit
  --delimiter DELIMITER
  --column COLUMN
  --timestamp_format TIMESTAMP_FORMAT
  --show_errors
  --dont_show_output
  --exit_on_error
  --eq EQ
  --ne NE
  --lt LT
  --gt GT
  
  Defaults:
  * timestamp_format is %Y.%m.%d %H:%M:%S
  * column 0
  * delimiter ,

--show_errors: show errors
--exit_on_error: exit on first error, exit code = -1
--dont_show_output: dont show filtered output, but will print errors if show_errors is enabled
 
 --eq: show timestamps equal to
 --ne: show timestamps not equal to
 --lt: show timestamps lower than
 --gt: show timestamps greater than
 
 Example: Show rows equal to timestamp
 
 $ < example.csv ./time_filter.py --column 1 --eq "2021.08.13 04:14:07"
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14🈯

Example: show rows not equal to timestamp 

$ < example.csv ./time_filter.py --column 1 --ne "2021.08.13 04:14:07"
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07,sfsfdfdf
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:15:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:16:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07
Core.log.01.gz,2021.08.13 04:17:07

Example: show rows between specific timestamps:

$ < example.csv ./time_filter.py --column 1 --gt "2021.08.13 04:13:07" --lt "2021.08.13 04:15:07"
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:13:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07
Core.log.01.gz,2021.08.13 04:14:07

Example: dont show filtered output, show errors

$ < example.csv ./time_filter.py --column 1 --gt "2021.08.13 04:13:07" --show_errors --dont_show_output
ERROR in ts "2021.08.13 04:17:07.434" or in ts format "%Y.%m.%d %H:%M:%S"
