import socket, threading, sys, SocketServer, logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )
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
#print('Running Server')
#TCPIP = '127.0.0.1'
#TCPIP = sys.argv[0]
#TCPPORT = 5005
#BUFFERSIZE = 20  # Normally 1024, but we want fast response
# 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCPIP, TCPPORT))
#s.listen(1)
#t = threading.Thread(target=server)
#t.start()
#def server():
#while True:
#	conn, addr = s.accept()
#	print('Connection address: %s' % addr)
#	data = conn.recv(BUFFERSIZE)
#	if not data: break
#	print("received data:", data)
#	conn.send(data)  # echo
#conn.close()
#print('stopping server: EOF')

class EchoRequestHandler(SocketServer.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        self.logger.debug('setup')
        return SocketServer.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        # Echo the back to the client
        data = self.request.recv(1024)
        self.logger.debug('recv()->"%s"', data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug('finish')
        return SocketServer.BaseRequestHandler.finish(self)

class EchoServer(SocketServer.TCPServer):
    
    def __init__(self, server_address, handler_class=EchoRequestHandler):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        SocketServer.TCPServer.server_activate(self)
        return

    def serve_forever(self):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return SocketServer.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return SocketServer.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return SocketServer.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        self.logger.debug('server_close')
        return SocketServer.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return SocketServer.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return SocketServer.TCPServer.close_request(self, request_address)

if __name__ == '__main__':
	#setLogLevel('info')
	#simpleTest()
	address = ('117.0.0.1', 55555) # let the kernel give us a port
	server = EchoServer(address, EchoRequestHandler)
	ip, port = server.server_address # find out what port we were given

	print("getting there")
	t = threading.Thread(target=server.serve_forever)
	t.setDaemon(True) # don't hang on exit
	t.start()

	logger = logging.getLogger('client')
	logger.info('Server on %s:%s', ip, port)