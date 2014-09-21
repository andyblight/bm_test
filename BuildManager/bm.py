#!/usr/bin/python

import sys, getopt

def print_help_and_exit(retval):
    print 'bm.py -i <inputfile> -o <outputfile>'
    sys.exit(retval)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
        print_help_and_exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help_and_exit(0)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', inputfile, '"'
    print 'Output file is "', outputfile, '"'

if __name__ == "__main__":
    main(sys.argv[1:])
