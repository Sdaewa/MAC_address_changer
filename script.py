#!/usr/bin/env python3
import subprocess

interface = input('interface > ')
# change < 00: 11: 33: 44: 55: 66 > for new address
new_mac = input('new MAC address > ')


print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
