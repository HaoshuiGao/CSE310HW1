from http import server
import socket
from socket import AF_INET, SOCK_STREAM
import os
from time import time
import sys

#Socket()
proxyPort = 13000
#ip address of the local host
proxyHost=socket.gethostbyname(socket.gethostname())
#AF_INET is address family use to designate type of address socket can communicate
#Communicate using stream socket
proxySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind my host with serverPort
proxySocket.bind((proxyHost,proxyPort))
print("proxyIpAddress: "+str(proxyHost))
print("proxyportNumber: "+str(proxyPort))

#start, handle new connection and distribute where to go
proxySocket.listen(1)
print("proxy ready to receive request...")

while True:
    #create a socket object and addr for client
    clientConn,clientAddr=proxySocket.accept()
    #get the client request
    clientRequest=clientConn.recv(1024).decode('utf-8')
    #parse the client request
    clientRequest=clientRequest.split("\r\n")[0]
    parsedUrl=clientRequest.split(" ")[1:2]
    
    # . describes the current directory u are in, and parsedUrl is /file    
    urlInString="".join(parsedUrl)
    #remove /
    urlInString=urlInString[1:]

    #remove http:// if exist, then advance that replaced blank space
    if("http://" in urlInString):
        urlInString=urlInString.replace("http://"," ")
        urlInString=urlInString[1:]
    
    print("target url is: "+urlInString)
    #check if file is in cache
    loadFileStringCheck=urlInString.replace("/"," ")
    if(os.path.isfile(loadFileStringCheck)):
        statusLine="HTTP/1.1 200 OK\r\n"
        f=open(loadFileStringCheck)
        r=f.read().encode()
        #another \r\n signify the end of header line
        statusLine=statusLine+"\r\n"
        clientConn.send(r)
        print("found in cache, send from cache")
        clientConn.close()
        sys.exit(0)

    else:
        #if not found in cache
        if "/" in urlInString:
            indexOfSlash=urlInString.index("/")
            host=urlInString[0:indexOfSlash]
            newUrl=urlInString[indexOfSlash+1:]
        else:
            host=urlInString
            newUrl=""
        
        #create a http request message
        proxyRequest="GET /"+newUrl+" HTTP/1.1\r\nHost:"+ host+"\r\n\r\n"
        #create a socket for server and connect to it
        serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverSocket.connect((socket.gethostbyname(host),80))
        #send the request to server for response
        serverSocket.send(proxyRequest.encode('utf-8'))
        #collect the response
        serverResponse=serverSocket.recv(4096)
        newResponse=serverResponse
        #timeout is used to prevent from stuck in while loop since it is blocking code
        serverSocket.settimeout(2.5)
        while len(serverResponse)>0:
            try:
                serverResponse=serverSocket.recv(4096)
                newResponse+=serverResponse
            except socket.timeout:
                break
        #take all the / away to store in as filename
        cacheFileString=urlInString.replace("/"," ")
        newFile=open(cacheFileString,"wb")
        newFile.write(newResponse)
        newFile.close()
        print("save in cache...")
        clientConn.sendall(newResponse)
        print("send over from webserver")
        #close the socket and end the sys
        clientConn.close()
        serverSocket.close()
        sys.exit(0)

