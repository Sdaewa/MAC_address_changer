#!/usr/bin/env python3
import subprocess

interface = input('interface > ')
new_mac = input('new MAC address > ')


print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
