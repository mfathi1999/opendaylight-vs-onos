from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class FatTreeTopo(Topo):
    def __init__(self, k, **opts):
        super(FatTreeTopo, self).__init__(**opts)

        self.k = k
        self.pod = []
        self.core_switches = []
        self.aggregate_switches = []
        self.edge_switches = []
        self.hosts = []

        self.create_pods()
        self.create_core_switches()
        self.create_aggregate_switches()
        self.create_edge_switches()
        self.create_hosts()
        self.create_links()

    def create_pods(self):
        for i in range(self.k):
            self.pod.append([])

    def create_core_switches(self):
        for i in range(int((self.k/2)**2)):
            switch = self.addSwitch('c%s' % (i + 1))
            self.core_switches.append(switch)

    def create_aggregate_switches(self):
        for i in range(self.k**2 // 2):
            switch = self.addSwitch('a%s' % (i + 1))
            self.aggregate_switches.append(switch)

    def create_edge_switches(self):
        for i in range(self.k**2 // 2):
            switch = self.addSwitch('e%s' % (i + 1))
            self.edge_switches.append(switch)

    def create_hosts(self):
        for i in range(self.k**3 // 4):
            host = self.addHost('h%s' % (i + 1))
            self.hosts.append(host)

    def create_links(self):
        # Connect core switches to aggregate switches
        for i in range(int(self.k/2)):
            for j in range(int(self.k/2)):
                self.addLink(
                    self.core_switches[i*int(self.k/2)+j],
                    self.aggregate_switches[i*int(self.k/2)+j],
                    bw=10, delay='1ms', loss=1
                )

        # Connect aggregate switches to edge switches
        for i in range(int(self.k/2)):
            for j in range(int(self.k/2)):
                self.addLink(
                    self.aggregate_switches[i*int(self.k/2)+j],
                    self.edge_switches[i*int(self.k/2)+j],
                    bw=10, delay='2ms', loss=2
                )

        # Connect edge switches to hosts
        for i in range(int(self.k**2//4)):
            self.addLink(
                self.edge_switches[i],
                self.hosts[i],
                bw=10, delay='3ms', loss=3
            )

topos = { 'fattree' : ( lambda k : FatTree(k)) }
