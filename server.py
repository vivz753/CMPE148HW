import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 12345
s.bind((host,port))


print ("The server is ready to receive")

while True:
	incomingMessage, host, port = s.recv(1024)
	incomingMessage = incomingMessage.decode('ascii')
	amtChars = len(incomingMessage)
	print ("Got message with %d characters from connection %s" % (amtChars, str(addr)))
	outgoingMsg = 'Thank you for connecting. Your message was %d characters long' % int(amtChars) + "\r\n"
	client.send(outgoingMsg.encode('ascii'), address)
	client.close()