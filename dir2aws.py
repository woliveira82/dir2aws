#!/usr/bin/python3

import sys, getopt


def main(argv):
   try:
      opts, args = getopt.getopt(argv, 'hd:', ['directory='])
   except getopt.GetoptError:
      print('dir2aws.py -h')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Help me!')
      elif opt in ('-d', '--dir'):
         print('Sending file: {}'.format(arg))


if __name__ == '__main__':
   main(sys.argv[1:])
