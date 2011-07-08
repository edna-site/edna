#!/usr/bin/env python
"""
Very simple program that mimics the behavour of cat under unix but written in python
Written by Jerome Kieffer, october 2010 
"""
import sys, os

def stdin3stdout():
    "Copy stdin to stdout"
    sys.stdout.write(sys.stdin.read())

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for filename in sys.argv[1:]:
            if os.path.isfile(filename):
                sys.stdout.write(open(filename, "rb").read())
            elif filename == "-":
                stdin3stdout()
            else:
                sys.stderr.write("cat: %s: No such file or directory" % filename)
    else:
        stdin3stdout()
