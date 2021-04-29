#!/usr/bin/env python3

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
# change < 00: 11: 33: 44: 55: 66 > for new address
subprocess.call("ifconfig wlan0 hw ether 00:11:33:44:55:66", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
