#!/usr/bin/env python
import socket
import struct
from threading import Thread 
from SocketServer import ThreadingMixIn 
import copy
import sys

class ClientThread(Thread):
	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip 
        	self.port = port 
       	 	print ("New server socket thread started for " + ip + ":" + str(port))
	
	def run(self):
		while True:
			data = str(conn.recv(100))
			#print("Server received data (comp name): " + str(data)) 
			try:
				answer = (socket.gethostbyname(data))
				print("A = " + answer + '\n')
				arr = copy.deepcopy(answer)
				arr = arr.split('.')
				
				if len(arr) != 4:
					answer = "The hostname doesn't correspond to a valid ip address! \n"
			
				conn.send(str(answer))
			except socket.error as se:
				conn.send("Error occured, can not give ip. \n" )

if __name__ == '__main__':
	ip = '127.0.0.1'
	port = 1234
	buffsize = 100
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((ip, port))
	threads = []
	
	while True:
		server.listen(4)
		print("multithreaded server, waiting for clients ... \n")
		(conn, (ip, port)) = server.accept()
		newThread = ClientThread(ip, port)
		newThread.start()
		threads.append(newThread)
	
	for t in threads:
		t.join()
		

