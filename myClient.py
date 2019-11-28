import socket, optparse

#parser = optparse.OptionParser()
#parser.add_option('-i', dest='ip', default='127.0.0.1')
#parser.add_option('-p', dest='port' , type'int', default=12345)
#parser.add_option('-m', dest='msg')
#(options, args) = parser.parse_args()

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.sendto(options.msg, (options.ip, options.port))
print('Running Client')

TCPIP='127.0.0.1'
TCPPORT = 5005
BUFFERSIZE = 1024
MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCPIP, TCPPORT))
s.send(MESSAGE)
data = s.recv(BUFFERSIZE)
s.close()
 
print "received data:", data