from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
import threading, time, socket, logging, SocketServer, sys

#tree4 = TreeTopo(depth=2, fanout=2)
##net = Mininet(topo=tree4)
#net.start()
#h1, h4 = net.hosts[0], net.hosts[3]
#print(h1.cmd('ping -c1 %s' % h4.IP()))
#net.stop()
		
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )
	
class SingleSwitchTopo(Topo):
	def build(self, n=2):
		self.addSwitch('s1')
		self.addSwitch('s2')
		self.addSwitch('s3')
		self.addLink('s1','s2')
		self.addLink('s1','s3')
		self.addSwitch('s4')
		self.addSwitch('s5')
		self.addSwitch('s6')
		self.addSwitch('s7')
		self.addLink('s2','s4')
		self.addLink('s2','s5')
		self.addLink('s3','s6')
		self.addLink('s3','s7')
		self.addHost('h1')
		self.addHost('h2')
		self.addHost('h3')
		self.addHost('h4')
		self.addHost('h5')
		self.addHost('h6')
		self.addHost('h7')
		self.addHost('h8')
		self.addLink('s4', 'h1')
		self.addLink('s4', 'h2')
		self.addLink('s5', 'h3')
		self.addLink('s5', 'h4')
		self.addLink('s6', 'h5')
		self.addLink('s6', 'h6')
		self.addLink('s7', 'h7')
		self.addLink('s7', 'h8')
		#switch = self.addSwitch('s')
		#for h in range(n):
		#	host = self.addHost('h%s' % (h+1))
		#	self.addLink(host, switch)
		#	print('added link')
	
def simpleTest():
	topo1 = SingleSwitchTopo(n=2)
	net = Mininet(topo1)
	net.start()
	print("Dumping")
	dumpNodeConnections(net.hosts)
	print("Testing")
	net.pingAll()
	
	global h1
	global h2
	
	print('get h1')
	h1 = net.get('h1')
	print('get h2')
	h2 = net.get('h2')
	thread1 = threading.Thread(target=startH1)
	thread2 = threading.Thread(target=startH2)
	thread1.start()
	thread2.start()
	#print h1.cmd('python myServer.py', h1.IP())
	#print h2.cmd('python myClient.py', h1.IP())
	#p1 = h1.popen('python myServer.py &')
	CLI(net)
	#p1.terminate()
	net.stop()
	
def startH1():
	print("doing startH1")
	h1.cmd('python myServer.py')
	
def startH2():
	h2.cmd('python myClient.py')
	
if __name__ == '__main__':
	#setLogLevel('info')
	simpleTest()
	
#	address = ('localhost', 0) # let the kernel give us a port
#	server = EchoServer(address, EchoRequestHandler)
#	ip, port = server.server_address # find out what port we were given

#	t = threading.Thread(target=server.serve_forever)
#	t.setDaemon(True) # don't hang on exit
#	t.start()

#	logger = logging.getLogger('client')
#	logger.info('Server on %s:%s', ip, port)

    # Connect to the server
#	logger.debug('creating socket')
#	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	logger.debug('connecting to server')
#	s.connect((ip, port))

    # Send the data
#	message = 'Hello, world'
#	logger.debug('sending data: "%s"', message)
#	len_sent = s.send(message)

    # Receive a response
#	logger.debug('waiting for response')
#	response = s.recv(len_sent)
#	logger.debug('response from server: "%s"', response)

    # Clean up
#	logger.debug('closing socket')
#	s.close()
#	logger.debug('done')
#	server.socket.close()
	