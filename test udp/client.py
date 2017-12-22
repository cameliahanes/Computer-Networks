#!/usr/bin/env python
import socket
import struct
import time
import calendar

if __name__ == '__main__':
	server_ip = 'localhost'
	server_port = 1234
	try: 
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	message = "Current date and time"
	message = str(raw_input("Enter question for server: "))
	server.sendto(bytes(str(message)), (server_ip, server_port))
	seconds = server.recvfrom(100)
	print("The number of seconds is: " + str(seconds[0]))
	seconds = int(seconds[0])
	#print((time.gmtime((seconds))))
	print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime((seconds)))))
	#print(str(time.gmtime((seconds))))
