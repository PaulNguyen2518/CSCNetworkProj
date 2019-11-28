import socket, optparse, threading

#parser = optparse.OptionParser()
#parser.add_option('-i', dest='ip', default='')
#parser.add_option('-p', dest='port', type='int', default=12345)
#(options, args) = parser.parse_args()

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((options.ip, options.port))

#f.write("WRITING!")
#f.close()

#while True:
#	f = open('foo.txt', 'w')
#	data, addr = s.recvfrom(512)
#	f.write("%s: %s\n" % (addr, data))
#	f.flush()
#	f.close()
print('Running Server')

TCPIP = '127.0.0.1'
TCPPORT = 5005
BUFFERSIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCPIP, TCPPORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

t = threading.Thread(target=server)
t.start()

def server():
	while 1:
		data = conn.recv(BUFFERSIZE)
		if not data: break
		print "received data:", data
		conn.send(data)  # echo
	conn.close()