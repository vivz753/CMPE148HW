import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)
print ("The server is ready to receive")

while True:
	client, addr = s.accept()
	incomingMessage = client.recv(1024)
	incomingMessage = incomingMessage.decode('ascii')
	amtChars = len(incomingMessage)
	print ("Got message with %d characters from connection %s" % (amtChars, str(addr)))
	msg = 'Thank you for connecting. \n You typed %s \n Your message was %d characters long' % (incomingMessage, amtChars) + "\r\n"
	client.send(msg.encode('ascii'))
	client.close()