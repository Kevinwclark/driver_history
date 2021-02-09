# Code Challenge For Root

A program to process driver data from a txt file. The output will represent driver miles and average speed. 
Example input:

```
Driver Dan
Driver Lauren
Driver Kumi
Trip Dan 07:15 07:45 17.3
Trip Dan 06:12 06:32 21.8
Trip Lauren 12:01 13:16 42.0
```

Expected output:

```
Lauren: 42 miles @ 34 mph
Dan: 39 miles @ 47 mph
Kumi: 0 miles
```

## Getting Started

Clone [driver_history](https://github.com/Kevinwclark/driver_history) repo and cd into driver_history. Run the following command:
```
python driver_report.py input.txt
```

## Prerequisites

* [Python](https://www.python.org/) - Version 3.9.0


## Thought Process

Upon receiving the namespace argument in main(), the file was sent to cammand_finder() for further processing. 

```command_finder()```
Within this function the file is opened on line 47 and closed on line 49 with a dedent and the TextIOWrapper object stored as f. Line 48 reads and splits on lines. At this point I thought it best to loop through each line searching for commands. After splitting on space I wanted two conditions for command names. If the "Driver" command was found then line 53 passed the sliced string from the list to initialize_driver(). On the flip, if "Trip" was found all the following data was processed and sent to driver_data(). 

```initialize_driver()```
I decided it would be best to utilize a class for instantiating a driver. I wanted a driver to have certain properties and methods to call later after all driving data had been processed. Then placing the driver object into a dictionary would make it easy to loop through and recall properties and call the average() method.

```driver_data()```
This function dove into processing the start and stop times. I decided to use the strptime() method to create a datetime object. Once I converted that to hours I could check the average speed and let my condition process it on line 39. If both conditions were met the driver instance would update miles and hours. If the conditions were not met, the miles and hours would remain at zero when set with __init__(). 

```sorted_drivers```
Since sorting by most miles driven I thought it best to dig into the dictionary driver instances and sort with a lambda. This is the quickest and most efficient way to sort. 

After I have sorted all drivers by miles, I jumped into a loop on line 77. Starting with a ternary operator, I wanted the average to equate to zero if in fact the hours were zero else call the driver instance average(). With avg pointing at the drivers average I could build a string with the default sentence to print. But if the average was greater then 0 I could simply tack onto the string originally constructed. 

## And coding style tests

The tests I decided on are as follows: 

```
test_command_finder: Testing commands coming in.
test_initialize_driver: Checks for Driver initialization.
test_driver_data_discard_fast: Checks if data is discarded if average > 100.
test_driver_data_discard_slow: Checks if data is discarded if average < 5.
test_driver_data_times: Checks the driver times.
test_input_file: Test end to end functionality.
test_flake8: Checking for PEP8/flake8 compliance.
```

## Built With

* [Python](https://www.python.org/) - Version 3.9.0

## Author

* **Kevin Clark** - [GitHub](https://github.com/Kevinwclark)
Thank you for this opportunity to present code. 
