#!/usr/bin/env python
import socket
import struct
import time
import calendar

def solve_client(client, string):
	if string != "Current date and time":
		rs.sendto(bytes("Can not provide date, you asked for something else ...\n"), client)
		return
	else:
		tp = time.gmtime()
		seconds = calendar.timegm(tp)
		print(str(seconds))
		rs.sendto(bytes(str(seconds)), client)


if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rs.bind(('0.0.0.0', 1234))
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	
	while True:
		#print(time.gmtime())
		print(calendar.timegm(time.gmtime()))
		string, addr = rs.recvfrom(100)
		print(addr, string)
		solve_client(addr, string)
