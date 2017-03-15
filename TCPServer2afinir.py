from socket import *
serverPort = 12003
serverSocket = socket(AF_INET,SOCK_STREAM) #
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

serveurPort2 = 120002
serverSocket2 = socket(AF_INET,SOCK_STREAM2)

print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept() #client se connect serveur accept
	sentence = connectionSocket.recv(1024)  # recoit les données 
	capitalizedSentence = sentence.upper()  # passe en majuscule 
	print "From Server:", capitalizedSentence 
	connectionSocket.close() # fermeture connection socket 
	connectionSocket.send(capitalizedSentence) #envoie donne 
	print "From Server:", capitalizedSentence 
	print addr[0]  # sort ladresse de lexpediteur 
	connectionSocket.close() # fermeture connection socket 