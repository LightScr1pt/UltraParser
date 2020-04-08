"""
 CODE BY LightScript
 My GitHub https://github.com/LightScr1pt/
"""

import os

line = "---------------------------------------------------------------"
print(line)
try:  
    print('[!] Installing a Tor')
    os.system('apt-get install tor -y')
except:
    print('[ERROR] Error to install Tor')
try:      # Connecting to tor services (only on linux)
    os.system('systemctl start tor.service')
except:
    print('[ERROR] Error to start Tor')
print(line)
try:
    os.system('systemctl status tor.service')
except:
    print('[ERROR] Error to get Tor status')
        # INSTALLING ALL NEEDS LIBARYS
try:
    from bs4 import BeautifulSoup
    print('[OK] BeautifulSoup installed')
except:
    print('[-] BeautifulSoup not found')
    os.system('pip3 install bs4')
try:
    import requests
    print('[OK] Requests installed')
except:
    print('[-] Requests not found')
    os.system('pip3 install requests')
try:
    import fake_useragent
    print('[OK] FakeUseragent installed')
except:
    print('[-] FakeUseragent not found')
    os.system('pip3 install fake_useragent')
try:
    import colorama
    print('[OK] Colorama installed')
except:
    print('[-] Colorama not found')
    os.system('pip3 install colorama')
print(line)