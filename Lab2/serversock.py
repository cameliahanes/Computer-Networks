#!/usr/bin/env python

import socket
from threading import Thread
from SocketServer import *

# multithreaded python server : TCP server socket thread pool

class ClientThread(Thread):
	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print("[+] New server socket thread started for " + ip + ":" + str(port))

	def run(self):
		while True:
			data = conn.recv(2048)
			print("Server received data: " + data)
			message = raw_input("Multithreaded Python server : Enter Response from Server / Enter exit: ")
			if message == 'exit':
				break
			conn.send(message) # echo

# multithreaded python server : TCP Server Socket

TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
	tcpServer.listen(4)
	print("Multithreaded Python server: Waiting for connections from TCP clients ...")
	(conn, (ip, port)) = tcpServer.accept()
	newThread = ClientThread(ip, port)
	newThread.start()
	threads.append(newThread)

for t in threads:
	t.join()
