import argparse
import sys
import datetime
from datetime import timedelta
from collections import defaultdict


d = defaultdict(list)

def initialize_driver(driver):
    d[driver]
    return d


def driver_data(driver, start, stop, miles):
    x = datetime.datetime.strptime(start, '%H:%M')
    y = datetime.datetime.strptime(stop, '%H:%M')
    td = timedelta(hours=y.hour, minutes=y.minute) - timedelta(hours=x.hour, minutes=x.minute)
    hours = td.seconds / 3600
    print('hours', hours)
    print('average speed', float(miles) / hours)
    
    

def command_finder(filename):
    with open(filename, 'r') as f:
        x = f.read().splitlines()
        for line in x:
            y = line.split(' ')
            if y[0] == "Driver":
                driver = y[1]
                initialize_driver(driver)
            elif y[0] == 'Trip':
                print("here is the line",line)
                driver = y[1]
                start = y[2]
                stop = y[3]
                miles = y[4]
                driver_data(driver, start, stop, miles)
        
        


def main(args):
    parser = argparse.ArgumentParser(
        description="Receives driver data and creates report."
    )
    print(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    filename = args[0]
    command_finder(filename)

    print(d)
    

if __name__ == "__main__":
    main(sys.argv[1:])

