#!/usr/bin/env python3
import subprocess
import optparse


parser = optparse.OptionParser()

# options
parser.add_option('-i', '--interface', dest='interface',
                  help='Interface to change MAC address')

parser.add_option('-m', '--interface', dest='interface',
                  help='Interface to change MAC address')


parser.parse_args()


interface = input('interface > ')
new_mac = input('new MAC address > ')


print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
