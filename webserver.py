import socket
from socket import AF_INET, SOCK_STREAM
import os
import sys

#Socket()
serverPort = 12000
#ip address of the local host
host=socket.gethostbyname(socket.gethostname())
#AF_INET is address family use to designate type of address socket can communicate
#Communicate using stream socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind my host with serverPort
serverSocket.bind((host,serverPort))
print("hostIpAddress: "+str(host))
print("portNumber: "+str(serverPort))

#start, handle new connection and distribute where to go
serverSocket.listen(1)
print("ready to receive request...")
while True:
    #conn=actual object to send back to client
    #addr=what port and what ip address
    clientConn,addr=serverSocket.accept()
    #parse the request\
    request=clientConn.recv(1024).decode('utf-8')
    request=request.split("\r\n")[0]
    parsedUrl=request.split(" ")[1:2]
    # . describes the current directory u are in, and parsedUrl is /file    
    urlInString="".join(parsedUrl)
    newUrlInString="."+urlInString  

    if(os.path.isfile(newUrlInString)):
        statusLine="HTTP/1.1 200 OK\r\n"
        f=open(newUrlInString,"rb")
        r=f.read()
        #another \r\n signify the end of header line
        statusLine=statusLine+"\r\n"
        clientConn.send(statusLine.encode("utf-8")+r)
        print("file found, send back")
    else:
        statusLine="HTTP/1.1 404 Not Found\r\n"
        clientConn.send(statusLine.encode("utf-8"))
        print("file not found, send 404")
    clientConn.close()
    sys.exit(0)

    

    
        
    
