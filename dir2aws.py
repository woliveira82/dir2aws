#!/usr/bin/python3

import sys, os, getopt
from classes import *


def main(argv):
   try:
      opts, args = getopt.getopt(argv, 'hd:', ['directory='])
   except getopt.GetoptError:
      print('dir2aws.py -h')
      sys.exit(2)

   if len(opts) is 0:
      print('dir2aws.py -h')
      sys.exit(2)
      
   for opt, arg in opts:
      if opt == '-h':
         print('Help me!')
      elif opt in ('-d', '--dir'):
         if os.path.isdir(arg):
            return Aws().uploadDir(arg)
         else:
            print('Error: "{0}" is not a directory.'.format(arg))
            return 1


if __name__ == '__main__':
   main(sys.argv[1:])
