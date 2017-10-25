#AUTHOR: VIVIAN LEUNG
#OCTOBER 24, 2017
#CMPE148, PROF: ROD FATOOHI

#TESTING INSTRUCTIONS:
#!RUN THE SERVER BEFORE THE CLIENT!
#IN TERMINAL, TYPE "python UDPserver.py" FOLLOWED BY "python UDPclient.py"
#ENJOY!
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #unlike TCP, uses SOCK_DGRAM

address = ('localhost', 12345) #unlike TCP, stores host & port in 1 variable

#unlike TCP, does NOT connect to host & port, just receives

outgoingMsg = input("Type something here: \n")
client.sendto(outgoingMsg.encode('ascii'), address) #unlike TCP, uses sendto(msg, address)

if outgoingMsg == 'quit':
	client.close()

else:	
	response = client.recv(4096) #same as TCP
	print (response.decode('ascii')) #same

	client.close() #same 

