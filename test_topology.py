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
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' ) 
        Host7 = self.addHost( 'h7' )
        Host8 = self.addHost( 'h8' )
        Host9 = self.addHost( 'h9' ) 
         
      
      
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )

      
        # Add links
        self.addLink( Host1, Switch2 )
        self.addLink( Host2, Switch2 )
        self.addLink( Host3, Switch2 )
      
        self.addLink( Host4, Switch3 )
        self.addLink( Host5, Switch3 )
        self.addLink( Host6, Switch3 )
        
        self.addLink( Host7, Switch4 )
        self.addLink( Host8, Switch4 )
        self.addLink( Host9, Switch4 )

        
         
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch1, Switch4 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
