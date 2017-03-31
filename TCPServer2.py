from socket import *
serverPort = 12003
serverSocket = socket(AF_INET,SOCK_STREAM) #
serverSocket.bind(("",serverPort))
serverSocket.listen(1)


serveurPort2 = 12002
serverSocket2 = socket(AF_INET,SOCK_STREAM)

print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept() #client se connect serveur accept
	sentence = connectionSocket.recv(1024)  # recoit les donnees 
	capitalizedSentence = sentence.upper()  # passe en majuscule 
	print "From Server:", capitalizedSentence 
	connectionSocket.close() # fermeture connection socket 
	connectionSocket.send(capitalizedSentence) #envoie donne 
	print "From Server:", capitalizedSentence 
	print addr[0]  # sort ladresse de lexpediteur 
	connectionSocket.close() # fermeture connection socket 
        serverSocket2.bind("",servertPort2)
        serveurSocket2.listen(1) 
        while 1:
		connectionSocket, addr = serverSocket2.accept()   #accepte connection client2
		connectionSocket.send(capitalizedSentence)	#renvoi les donnees au 2eme client
		print "From Server:", capitalizedSentence	
		connectionSocket.close()
		