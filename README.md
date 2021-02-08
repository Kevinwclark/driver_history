## Code by Kevin Clark
______________________

First, thank you for this opportunity to present code. 

Language of choice: Python

For this program I chose to accept input via command line. 

```python driver_report.py input.txt```

Upon receiving the namespace argument, the file was sent to cammand_finder() for further processing. 

```command_finder()```
Within this function the file is opened on line 50 and closed on line 52 with a dedent and the TextIOWrapper object stored as f. Line 51 reads and splits on lines. At this point I thought it best to loop through each line searching for commands. After splitting on space I wanted two conditions for command names. If the Driver command was found then line 56 passed the sliced name from the list.  




```We're interested in the thought process behind your choices, so please take some time to capture that in your README. For example, you can represent your data using primitives, structs, or objects. We don't consider any one of those options better than the others. However, we expect you to make an intentional choice, implement it consistently, and communicate why you chose that approach.```

