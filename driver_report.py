import argparse
import sys


def main(args):
    parser = argparse.ArgumentParser(
        description="Receives driver data and creates report."
    )
    print(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    filename = args[0]

    with open(filename, 'r') as f:
        x = f.read()
        print(x)

if __name__ == "__main__":
    main(sys.argv[1:])

