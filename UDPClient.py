from socket import *
	serverName = 'localhost' 
	serverPort = 12000
	clientSocket = socket(socket.AF_INET .SOCK_DGRAM)
		message = raw_input("texte ?")
	clientSocket.sendto(message,(serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
	clientSocket.close()

