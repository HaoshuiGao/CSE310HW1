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
  
Picture Order in PDF
1.Part 1 hello world success
2.Part 1 error 404 proof
3.Part 2 test case file 2
4.Part 2 test case file 3
5.Part 2 test case file 4
6.Part 2 test case file 5
7.Cache data proof

Instructions on how to run your programs:
  -kill terminal before run a terminal to test it
  -after run one url, the terminal will kill itself,  please run terminal again if need to test next terminal
  Part1
  1.Open webserver.py and run
  2.Terminal will print hostIpAddress, portNumber,and ready to receive request...
  3.Open Chrome Browser and enter the url(hostIpAddress:portNumber/helloworld.html), example: 172.25.52.85:12000/helloworld.html
  4.It will show the pages in helloworld.html in picture 1 in pdf and print "file found, send back" in terminal
  5.Change the helloworld.html to other random address.  172.25.52.85:12000/qwkdqwkd0kdl.html
  6.It should print 404 error page same as picture 2 in the pdf and "file not found, send 404" in terminal 
  
  Part2
  1.Open proxyserver.py and run
  2.Terminal will print proxyHostIpAddress, proxyPortNumber,and proxy ready to receive request...
  3.Open Chrome Browser and enter the url(proxyHostIpAddress:proxyPortNumber/website.html), example: 172.25.52.85:13000/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
  4.It will print target url in the terminal 
  5.If not cache, terminal will print "H T T P / 1 . 1   2 0 0   O K", "save in cache...", and "send over from webserver"
  6.Then the folder will get a new html as cache page, browser should display corresponding page
  7.If cache, terminal will print "found in cache, send from cache" 
  8.Browser display corresponding page
  9.If it is not a valid website, then the error page will not be cache and print "not 200 response, no cache"
  10.If it shows "favicon.ico" in target url and "socket.gaierror: [Errno 11001] getaddrinfo failed", rerun the terminal again
  
  
Webpages that your code successfully works for
  1.helloworld.html
  2.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
  3.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
  4.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
  5.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html

