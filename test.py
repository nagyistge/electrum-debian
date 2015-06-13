#!/usr/bin/python

import os
import argparse

# create common parser
parent_parser = argparse.ArgumentParser('parent', add_help=False)
parent_parser.add_argument('--version', action='version', version='%(prog)s 2.0')

# create the top-level parser
parser = argparse.ArgumentParser(parents=[parent_parser])
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo', parents=[parent_parser])



while True:
    with open('/dev/random','r') as f:
        s = f.read(16)
        print s.encode('hex')
