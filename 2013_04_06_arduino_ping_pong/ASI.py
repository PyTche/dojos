#!/usr/bin/env python
# encoding: utf-8
"""
ASI.py

Created by Filipe Cifali Stangler on 2013-04-06.
"""

import serial
import sys

def main():
	if sys.argv is Null:
		print "No data input.\n Input data for the Arduino"
	else:
		baud_rate = 9600
		s = serial.Serial('/dev/tts.usbmodem1411',baud_rate)
		s.write(sys.argv[1])
		print "Data inputed!!\n Data: ->",sys.argv[1],"\nCheck your Arduino!!"
		s.close()

if __name__ == '__main__':
	main()

