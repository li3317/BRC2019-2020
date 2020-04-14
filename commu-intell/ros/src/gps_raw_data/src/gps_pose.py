import serial 
import time
import string
import pynmea2

class gps:
	
	_latitude
	_longitude
	_altitude

	def __init__():
		self._latitude = 0
		self._longitude = 0
		self._altitude = 0

	def get_latitude() {
		return self._latitude
	}

	def get_longitude() {
		return self._longitude
	}

	def get_altitude() {
		return self._altitude
	}

	def set_latitude_longitude():
		while (True):
			port = "/dev/ttyAMA0"
			ser = serial.Serial(port, baudrate=9600, timeout=0.5)
			dataout = pynmea2.NMEAStreamReader()
			newdata = ser.readline()

			if newdata[0:6] == "$GPRMC":
				newmsg = pynmea2.parse(newdata)
				self.latitude = newmsg.latitude
				self.longitude = newmsg.longitude
				coordinates = [self.latitude, self.longitude]  #return terminates loop right?