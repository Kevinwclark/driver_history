import argparse
import sys
import datetime
import operator
from datetime import timedelta
from collections import defaultdict


d = defaultdict(dict)
class Driver:
    def __init__(self, name, miles=0, hours=0):
        self.name = name
        self.miles = miles
        self.hours = hours
    
    def average(self):
        return "%s: %s miles @ %s." % (self.name, self.miles, round(self.miles / self.hours))


def initialize_driver(driver):
    d[driver] = Driver(driver)


def driver_data(driver, start, stop, miles):
    x = datetime.datetime.strptime(start, '%H:%M')
    y = datetime.datetime.strptime(stop, '%H:%M')
    td = timedelta(hours=y.hour, minutes=y.minute) - timedelta(hours=x.hour, minutes=x.minute)
    hours = td.seconds / 3600
    mile = round(float(miles))
    d[driver].miles += mile
    d[driver].hours += hours
    

def command_finder(filename):
    """Open file and parse line commands"""
    with open(filename, 'r') as f:
        x = f.read().splitlines()
        for line in x:
            y = line.split(' ')
            if y[0] == "Driver":
                driver = y[1]
                initialize_driver(driver)
            elif y[0] == 'Trip':
                driver = y[1]
                start = y[2]
                stop = y[3]
                miles = y[4]
                driver_data(driver, start, stop, miles)
        

def main(args):
    """Parse terminal command"""
    parser = argparse.ArgumentParser(
        description="Receives driver data and creates report."
    )
    if not args:
        parser.print_usage()
        sys.exit(1)

    filename = args[0]
    command_finder(filename)
    
    sorting = sorted(d, key=lambda name: d[name].miles, reverse=True)

    for driver in sorting:
        if d[driver].miles == 0:
            print("%s: 0 miles" % d[driver].name)
        else:
            print(d[driver].average())

if __name__ == "__main__":
    main(sys.argv[1:])

