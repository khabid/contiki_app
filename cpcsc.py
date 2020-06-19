#!/usr/bin/python
"""Contiki csc parser."""
import xml.etree.ElementTree as ET
import re
# ----------------------------------------------------------------------------#
def get_node_count(file):
    """Get the number of nodes in the csc."""
    # Open the .csc file in ET
    tree = ET.parse(file)
    root = tree.getroot()

    # Get all the motes
    el_motes = root.findall('.simulation/mote')
    # Return the number of motes in the simulation
    return len(el_motes)


# ----------------------------------------------------------------------------#
def append_make(file, append):
    """Append the make command in the csc."""
    # Open the .csc file in ET
    tree = ET.parse(file)
    root = tree.getroot()

    # Get the makefile commands
    el_commands = root.findall('.simulation/motetype/commands')
    # Print tags, attribs, and text
    for el in el_commands:
        print('> ' +  el.text)

    tree.write(file)


# ----------------------------------------------------------------------------#
def test():
    """Test this script."""
    # appendmake('/home/mike/Repos/usdn/examples/ipv6/sdn-udp/'
    #            'sdn-udp-3-node_exp5438.csc', 'RUN_CONF_WITH_SDN=1')
    x=get_node_count('../Last project/'
                   'test.csc')
    print(x)
    append_make('../Last project/'
                   'test.csc', '')


# ----------------------------------------------------------------------------#
if __name__ == "__main__":
    test()
