import argparse
import sys
# from collections import defaultdict


def initialize_drivers(filename):
    with open(filename, 'r') as f:
        x = f.read().splitlines()
        for line in x:
            y = line.split(' ')
            if y[0] == "Driver":
                print('Found driver')
        
        


def main(args):
    parser = argparse.ArgumentParser(
        description="Receives driver data and creates report."
    )
    print(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    filename = args[0]
    initialize_drivers(filename)

    

if __name__ == "__main__":
    main(sys.argv[1:])

