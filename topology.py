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

        # Add hosts
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )
        Host7 = self.addHost( 'h7' )
        Host8 = self.addHost( 'h8' )
        Host9 = self.addHost( 'h9' )
        Host10 = self.addHost( 'h10' )
        Host11 = self.addHost( 'h11' )
        Host12 = self.addHost( 'h12' )
        Host13 = self.addHost( 'h13' )
        Host14 = self.addHost( 'h14' )
        Host15 = self.addHost( 'h15' )
        Host16 = self.addHost( 'h16' )
        Host17 = self.addHost( 'h17' )
        Host18 = self.addHost( 'h18' )
        Host19 = self.addHost( 'h19' )
        Host20 = self.addHost( 'h20' )
        Host21 = self.addHost( 'h21' )
        Host22 = self.addHost( 'h22' )
        Host23 = self.addHost( 'h23' )
        Host24 = self.addHost( 'h24' )
        Host25 = self.addHost( 'h25' )
        Host26 = self.addHost( 'h26' )
        Host27 = self.addHost( 'h27' )
        
        
        # Add switches
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
        Switch5 = self.addSwitch( 's5' )
        Switch6 = self.addSwitch( 's6' )
        Switch7 = self.addSwitch( 's7' )
        Switch8 = self.addSwitch( 's8' )
        Switch9 = self.addSwitch( 's9' )
        Switch10 = self.addSwitch( 's10' )
        Switch11 = self.addSwitch( 's11' )
        Switch12 = self.addSwitch( 's12' )
        Switch13 = self.addSwitch( 's13' )
        
        # Add links
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch1, Switch4 )
        
        self.addLink( Switch2, Switch3 )
        self.addLink( Switch3, Switch4 )
        
        self.addLink( Switch2, Host1 )
        self.addLink( Switch2, Host2 )
        self.addLink( Switch2, Host3 )
        self.addLink( Switch2, Host4 )
        
        self.addLink( Switch3, Host4 )
        self.addLink( Switch3, Host5 )
        self.addLink( Switch3, Host6 )
        
        self.addLink( Switch4, Host7 )
        self.addLink( Switch4, Host8 )
        self.addLink( Switch4, Host9 )
        
        
        self.addLink( Host1, Host2 )
        self.addLink( Host2, Host3 )
        self.addLink( Host3, Host4 )
        self.addLink( Host4, Host5 )
        self.addLink( Host5, Host6 )
        self.addLink( Host6, Host7 )
        self.addLink( Host7, Host8 )
        self.addLink( Host8, Host9 )
        
        
        self.addLink( Host1, Switch5 )
        self.addLink( Host1, Switch6 )

        self.addLink( Host2, Switch5 )
        self.addLink( Host2, Switch6 )
        self.addLink( Host2, Switch7 )

        self.addLink( Host3, Switch6 )
        self.addLink( Host3, Switch7 )
        self.addLink( Host3, Switch8 )
        
        self.addLink( Host4, Switch7 )
        self.addLink( Host4, Switch8 )
        self.addLink( Host4, Switch9 )
        
        self.addLink( Host5, Switch8 )
        self.addLink( Host5, Switch9 )
        self.addLink( Host5, Switch10 )

        self.addLink( Host6, Switch9 )
        self.addLink( Host6, Switch10 )
        self.addLink( Host6, Switch11 )

        self.addLink( Host7, Switch10 )
        self.addLink( Host7, Switch11 )
        self.addLink( Host7, Switch12 )

        self.addLink( Host8, Switch11 )
        self.addLink( Host8, Switch12 )
        self.addLink( Host8, Switch13 )

        self.addLink( Host9, Switch12 )
        self.addLink( Host9, Switch13 )
        
        
        self.addLink( Switch5, Switch6 )
        self.addLink( Switch6, Switch7 )
        self.addLink( Switch7, Switch8 )
        self.addLink( Switch8, Switch9 )
        self.addLink( Switch9, Switch10 )
        self.addLink( Switch10, Switch11 )
        self.addLink( Switch11, Switch12 )
        self.addLink( Switch12, Switch13 )
        
        self.addLink( Switch5, Host10 )
        self.addLink( Switch5, Host11 )
        self.addLink( Switch5, Host12 )
        
        self.addLink( Switch6, Host12 )
        self.addLink( Switch6, Host13 )
        self.addLink( Switch6, Host14 )
        
        self.addLink( Switch7, Host14 )
        self.addLink( Switch7, Host15 )
        self.addLink( Switch7, Host16 )

        self.addLink( Switch8, Host17 )
        self.addLink( Switch8, Host18 )
        self.addLink( Switch8, Host19 )
        
        self.addLink( Switch9, Host19 )
        self.addLink( Switch9, Host20 )
        self.addLink( Switch9, Host21 )
        
        self.addLink( Switch10, Host21 )
        self.addLink( Switch10, Host22 )
        self.addLink( Switch10, Host23 )
        
        self.addLink( Switch11, Host22 )
        self.addLink( Switch11, Host23 )
        
        self.addLink( Switch12, Host23 )
        self.addLink( Switch12, Host24 )
        self.addLink( Switch12, Host25 )
        
        self.addLink( Switch13, Host25 )
        self.addLink( Switch13, Host26 )
        self.addLink( Switch13, Host27 )

        


topos = { 'mytopo': ( lambda: MyTopo() ) }
