# CSE310HW1 
Any external libraries used.
  Part1
    import socket
    from socket import AF_INET, SOCK_STREAM
    import os
    import sys
  Part2
    from http import server
    import socket
    from socket import AF_INET, SOCK_STREAM
    import os
    from time import time
    import sys

Tools:
  Window OS
  Chrome Browser
  Python 3.7.9
  VScode python ide
  
Instructions on how to run your programs:
  -kill terminal before run a terminal to test it
  -after run one url, the terminal will kill itself,  please run terminal again if need to test next terminal
  Part1
  1.Open webserver.py and run
  2.Terminal will print hostIpAddress, portNumber,and ready to receive request...
  3.Open Chrome Browser and enter the url(hostIpAddress:portNumber/helloworld.html), example: 172.25.52.85:12000/helloworld.html
  4.It will show the pages in helloworld.html in picture 1 in pdf and print "file found, send back" in terminal
  5.Change the helloworld.html to other random address.  172.25.52.85:12000/qwkdqwkd0kdl.html
  6.It should print 404 error page same as picture 2 in the pdf
  7.
Webpages that your code successfully works for
  1.helloworld.html
  2.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
  3.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
  4.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
  5.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html

