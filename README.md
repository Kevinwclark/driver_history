## Code by Kevin Clark
______________________

First, thank you for this opportunity to present code. 

Language of choice: Python

For this program I chose to accept input via command line. 

```python driver_report.py input.txt```

Upon receiving the namespace argument in main(), the file was sent to cammand_finder() for further processing. 

```command_finder()```
Within this function the file is opened on line 47 and closed on line 49 with a dedent and the TextIOWrapper object stored as f. Line 48 reads and splits on lines. At this point I thought it best to loop through each line searching for commands. After splitting on space I wanted two conditions for command names. If the "Driver" command was found then line 53 passed the sliced string from the list to initialize_driver(). On the flip, if "Trip" was found all the following data was processed and sent to driver_data(). 

```initialize_driver()```
I decided it would be best to utilize a class for instantiating a driver. I wanted a driver to have certain properties and methods to call later after all driving data had been processed. Then placing the driver object into a dictionary would make it easy to loop through and recall properties and call the average() method.

```driver_data()```
This function dove into processing the start and stop times. I decided to use the strptime() method to create a datetime object. Once I converted that to hours I could check the average speed and let my condition process it on line 39. If both conditions were met the driver instance would update miles and hours. If the conditions were not met, the miles and hours would remain at zero when set with __init__(). 

```sorted_drivers```
Since sorting by most miles driven I thought it best to dig into the dictionary driver instances and sort with a lambda. This is the quickest and most efficient way to sort. 

After I have sorted all drivers by miles. I jump into a loop with a ternary. I wanted the average to equate to zero if in fact the hours were zero else call the driver instance average(). With avg pointing at the drivers average I could build a string with the default sentence to print. But if the average was greater then 0 I could simply tack onto the string originally constructed. 



```We're interested in the thought process behind your choices, so please take some time to capture that in your README. For example, you can represent your data using primitives, structs, or objects. We don't consider any one of those options better than the others. However, we expect you to make an intentional choice, implement it consistently, and communicate why you chose that approach.```

