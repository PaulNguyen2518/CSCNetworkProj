from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

#tree4 = TreeTopo(depth=2, fanout=2)
##net = Mininet(topo=tree4)
#net.start()
#h1, h4 = net.hosts[0], net.hosts[3]
#print(h1.cmd('ping -c1 %s' % h4.IP()))
#net.stop()
			
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
	
	print('get h1')
	h1 = net.get('h1')
	h1.sendCmd('python myServer.py &')
	#p1 = h1.popen('python myServer.py &')
	
	print('get h2')
	h2 = net.get('h2')
	h2.sendCmd('python myClient.py &')
	
	CLI(net)
	#p1.terminate()
	net.stop()
	

if __name__ == '__main__':
	setLogLevel('info')
	simpleTest()
	