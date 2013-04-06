#!/usr/bin/env python
# encoding: utf-8
"""
ASI.py

Created by Filipe Cifali Stangler on 2013-04-06.
"""

import serial
import sys

def main(argv):
	if len(argv) < 2:
		print "No data input.\n Input data for the Arduino.\n Usage:",argv[0],"<argv[1]>"
		return 1
	else:
		baud_rate = 9600
		s = serial.Serial('/dev/tty.usbmodem1411',baud_rate)
		s.write(argv[1])
		print "Data inputed!!\nData: ->",argv[1],"\nCheck your Arduino!!"
		s.close()
		return 1

if __name__ == '__main__':
	main(sys.exit(main(sys.argv)))

