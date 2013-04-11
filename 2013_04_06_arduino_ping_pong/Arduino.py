#!/usr/bin/env python
# encoding: utf-8
"""
Arduino.py

Created by Filipe Cifali Stangler on 2013-04-06.
"""

import serial

class Arduino():
	def __init__(self, path='', baud_rate=''):
		self.arduino = arduino
		self.path = path
		self.baud_rate = baud_rate
	
	def start(self):
		self.s = serial.Serial(self.path, self.baud_rate)
	
	def send(self, data):
		self.s.send(data)
		
	def write(self, write_data):
		self.s.write(write_data)
	
	def read(self, bytes):
		while(1):
			if (self.s.inWaiting() > bytes-1):
				return self.s.read()
	
	def flush():
		self.s.flushInput()
