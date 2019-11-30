import socket, optparse, sys, time, logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

#parser = optparse.OptionParser()
#parser.add_option('-i', dest='ip', default='127.0.0.1')
#parser.add_option('-p', dest='port' , type'int', default=12345)
#parser.add_option('-m', dest='msg')
#(options, args) = parser.parse_args()

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.sendto(options.msg, (options.ip, options.port))
#global s
#global TCPIP
#global TCPPORT
#
#def sConnect():
#	try:
#		s.connect((TCPIP, TCPPORT))
#	except:
#		sConnect()

#print('Running Client')

#TCPIP='127.0.0.1'
#TCPIP = sys.argv[0]
##TCPPORT = 5005
#BUFFERSIZE = 1024
#MESSAGE = "Hello, World!"
#time.sleep(3)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sConnect()

#s.send(MESSAGE)
#data = s.recv(BUFFERSIZE)
#s.close()
 
#print("received data:", data)

if __name__ == '__main__':
	logger = logging.getLogger('client')
	
	# Connect to the server
	logger.debug('creating socket')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	logger.debug('connecting to server')
	s.connect(('117.0.0.1', 55555))

    # Send the data
	message = 'Hello, world'
	logger.debug('sending data: "%s"', message)
	len_sent = s.send(message)

    # Receive a response
	logger.debug('waiting for response')
	response = s.recv(len_sent)
	logger.debug('response from server: "%s"', response)

    # Clean up
	logger.debug('closing socket')
	s.close()
	logger.debug('done')
	server.socket.close()
	