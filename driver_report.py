#!/usr/bin/env python3
import argparse
import sys
import datetime
from datetime import timedelta
from collections import defaultdict


drivers = defaultdict(dict)


class Driver:
    def __init__(self, name, miles=0, hours=0):
        self.name = name
        self.miles = miles
        self.hours = hours

    def __str__(self):
        return f'{self.name}, {self.miles}, {self.hours}'

    def average(self):
        return round(self.miles / self.hours)


def initialize_driver(driver):
    """Create driver object within a defaultdict"""
    drivers[driver] = Driver(driver)


def driver_data(driver, start, stop, miles):
    """
    Update driver class with miles and hours,
    discarding averages not needed.
    """
    start_time = datetime.datetime.strptime(start, '%H:%M')
    stop_time = datetime.datetime.strptime(stop, '%H:%M')
    start_delta = timedelta(hours=start_time.hour, minutes=start_time.minute)
    stop_delta = timedelta(hours=stop_time.hour, minutes=stop_time.minute)
    td = stop_delta - start_delta
    hours = td.seconds / 3600
    mile = round(float(miles))
    average = mile / hours
    if average >= 5 and average <= 100:
        person = drivers[driver]
        person.miles += mile
        person.hours += hours


# check for quotes
def command_finder(filename):
    """Open file and parse line commands"""
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        words = line.split(' ')
        if words[0] == 'Driver':
            driver = words[1]
            initialize_driver(driver)
        elif words[0] == 'Trip':
            driver = words[1]
            start = words[2]
            stop = words[3]
            miles = words[4]
            driver_data(driver, start, stop, miles)


def main(args):
    """Parse terminal command"""
    parser = argparse.ArgumentParser(
        description="Receives driver data and creates report."
    )
    parser.add_argument('filename', help='filename to dig into')
    ns = parser.parse_args(args)

    filename = ns.filename
    command_finder(filename)

    sorted_drivers = sorted(
                drivers,
                key=lambda name: drivers[name].miles,
                reverse=True
            )

    for driver in sorted_drivers:
        avg = 0 if drivers[driver].hours == 0 else drivers[driver].average()
        string = f"{drivers[driver].name}: {drivers[driver].miles} miles"
        if avg > 0:
            string += f" @ {avg} mph"
        print(string)


if __name__ == "__main__":
    main(sys.argv[1:])
