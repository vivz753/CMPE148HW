#AUTHOR: VIVIAN LEUNG
#OCTOBER 24, 2017
#CMPE148, PROF: ROD FATOOHI

#TESTING INSTRUCTIONS:
#!RUN THE SERVER BEFORE THE CLIENT!
#IN TERMINAL, TYPE "python UDPserver.py" FOLLOWED BY "python UDPclient.py"
#ENJOY!
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #unlike TCP, uses SOCK_DGRAM not SOCK_STREAM


address = ('localhost', 12345) #unlike TCP, UDP puts host & port together in 1 variable instead of separately
s.bind(address) #same as TCP as in it needs to bind

#unlike TCP, doesn't have to listen(int)
print ('The UDP server is ready to receive on {} port {}'.format(*address)) 

while True:
	#unlike TCP, does NOT have to accept()
	incomingMessage, address = s.recvfrom(4096) #same as TCP
	incomingMessage = incomingMessage.decode('ascii') #same as TCP
	
	if incomingMessage == 'quit': 
		print ("Closing socket")
		break


	amtChars = len(incomingMessage) #same as TCP, calculate length of message
	print ("Got message: '%s' with %d characters from connection %s" % (str(incomingMessage), amtChars, str(address)))
	outgoingMsg = "Thank you for connecting. \n You typed '%s' \n Your message was %d characters long" % (incomingMessage, amtChars) + "\r\n"
	s.sendto(outgoingMsg.encode('ascii'), address) #unlike TCP, uses sendto(msg, address) instead of send(message)
	

s.close() 