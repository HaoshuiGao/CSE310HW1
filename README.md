# CSE310HW1 
Any external libraries used.<br />
  Part1<br />
    import socket<br />
    from socket import AF_INET, SOCK_STREAM<br />
    import os<br />
    import sys<br />
  Part2<br />
    from http import server<br />
    import socket<br />
    from socket import AF_INET, SOCK_STREAM<br />
    import os<br />
    from time import time<br />
    import sys<br />

Tools:<br />
  Window OS<br />
  Chrome Browser<br />
  Python 3.7.9<br />
  VScode python ide<br />
  
Picture Order in PDF<br />
1.Part 1 hello world success<br />
2.Part 1 error 404 proof<br />
3.Part 2 test case file 2<br />
4.Part 2 test case file 3<br />
5.Part 2 test case file 4<br />
6.Part 2 test case file 5<br />
7.Cache data proof<br />

Instructions on how to run your programs:<br />
  -kill terminal before run a terminal to test it<br />
  -after run one url, the terminal will kill itself,  please run terminal again if need to test next terminal<br />
  Part1<br />
  1.Open webserver.py and run<br />
  2.Terminal will print hostIpAddress, portNumber,and ready to receive request...<br />
  3.Open Chrome Browser and enter the url(hostIpAddress:portNumber/helloworld.html), example: 172.25.52.85:12000/helloworld.html<br />
  4.It will show the pages in helloworld.html in picture 1 in pdf and print "file found, send back" in terminal<br />
  5.Change the helloworld.html to other random address.  172.25.52.85:12000/qwkdqwkd0kdl.html<br />
  6.It should print 404 error page same as picture 2 in the pdf and "file not found, send 404" in terminal <br />
  
  Part2<br />
  1.Open proxyserver.py and run<br />
  2.Terminal will print proxyHostIpAddress, proxyPortNumber,and proxy ready to receive request...<br />
  3.Open Chrome Browser and enter the url(proxyHostIpAddress:proxyPortNumber/website.html), example: 172.25.52.85:13000/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html<br />
  4.It will print target url in the terminal <br />
  5.If not cache, terminal will print "H T T P / 1 . 1   2 0 0   O K", "save in cache...", and "send over from webserver"<br />
  6.Then the folder will get a new html as cache page, browser should display corresponding page<br />
  7.If cache, terminal will print "found in cache, send from cache" <br />
  8.Browser display corresponding page<br />
  9.If it is not a valid website, then the error page will not be cache and print "not 200 response, no cache"<br />
  10.If it shows "favicon.ico" in target url and "socket.gaierror: [Errno 11001] getaddrinfo failed", rerun the terminal again<br />
  11.The banner in gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html will not display the image because its src doesn't have a full url that tells the browser to where to load the image. This is not in scope of this hw.<br />
  
Webpages that your code successfully works for<br />
  1.helloworld.html<br />
  2.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html<br />
  3.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html<br />
  4.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html<br />
  5.gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html<br />

