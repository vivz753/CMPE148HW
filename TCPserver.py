#AUTHOR: VIVIAN LEUNG
#OCTOBER 24, 2017
#CMPE148, PROF: ROD FATOOHI

#TESTING INSTRUCTIONS:
#!RUN THE SERVER BEFORE THE CLIENT!
#IN TERMINAL, TYPE "python TCPserver.py" FOLLOWED BY "python TCPclient.py"
#ENJOY!
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #unlike UDP, uses SOCK_STREAM, not SOCK_DGRAM

host = socket.gethostname() #unlike UDP, stores host & port separately
port = 12345
s.bind((host,port)) #same as UDP as in it needs to bind

s.listen(5) #unlike UDP, listens up to 5 queue requests
print ("The TCP server is ready to receive on %s port %s" %(host, port)) 

while True:
	client, address = s.accept() #unlike UDP, TCP must accept 
	incomingMessage = client.recv(1024) #same as UDP
	incomingMessage = incomingMessage.decode('ascii') #same as UDP
	
	if incomingMessage == 'quit':
		print ("Closing socket")
		client.close()
		break

	amtChars = len(incomingMessage) #same as UDP, calculate length of message
	print ("Got message: '%s' with %d characters from connection %s" % (str(incomingMessage), amtChars, str(address)))
	msg = "Thank you for connecting. \n You typed '%s' \n Your message was %d characters long" % (incomingMessage, amtChars) + "\r\n"
	client.send(msg.encode('ascii')) #unlike UDP, uses send(msg) instead of sendto(msg, address)
	client.close() #same as UDP, close socket

s.close()