from socket import *
def main():
        serverPort=9314 #Assigning a port to the server
        serverSocket = socket(AF_INET, SOCK_STREAM)#Creating an INET, STREAMing socket
        #Preparing a server socket
        serverSocket.bind(('',serverPort))# Binding the socket to server address and server port
        serverSocket.listen(1)# Listening to at most 1 connection at a time
        print 'the web server is up on port:',serverPort
        while True:
        #Establishing the connection
                print 'Ready to server. . .'
                connectionSocket, addr = serverSocket.accept()# Setting up a new connection from the client
                try:
                        message=connectionSocket.recv(1024)# Receiving the request message from the client
                        #Extracting the path of the requested object from the message
                        #The path is the second part of HTTP header, identified by [1]
                        print message,'::',message.split()[0],':',message.split()[1]
                        filename = message.split()[1]
                        print filename,'||',filename[1:]
                        #The extracted path of the HTTP request includes a character '/',hence we read the path from the second character 
                        f = open(filename[1:])
                        outputdata = f.read()# Storing the entire contenet of the requested file in a temporary buffer
                        print outputdata
                        #Send one HTTP header line into socket
                        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
                        connectionSocket.send(outputdata)
                        connectionSocket.close()

                except IOError:
                    pass

                    print "404 Not Found"# Sending HTTP response message if file not found
                    connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')

                #TEMP BREAK
                break
        pass

if __name__ == '__main__':
    main()
