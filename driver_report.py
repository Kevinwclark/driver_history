import argparse
import sys
from collections import defaultdict


d = defaultdict(list)


def initialize_driver(driver):
    d[driver] = []
    return d



def driver_data():
    pass


def command_finder(filename):
    with open(filename, 'r') as f:
        x = f.read().splitlines()
        for line in x:
            y = line.split(' ')
            if y[0] == "Driver":
                driver = y[1]
                initialize_driver(driver)
            elif y[0] == 'Trip':
                driver_data()
        
        


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

