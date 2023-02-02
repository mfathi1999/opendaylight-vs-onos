"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )        
      
      
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )

      
        # Add links
        self.addLink( Host1, Switch2 )
        self.addLink( Host2, Switch3 )
        self.addLink( Host3, Switch4 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch1, Switch4 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
