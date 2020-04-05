"""
 CODE BY LightScript
 My GitHub https://github.com/LightScr1pt/python/
"""
from time import sleep
import platform
import os

line = "---------------------------------------------------------------"
print(line)
try:   # Connecting to tor services (only on linux)
    os.system('apt-get install tor')
except:
    Error = True 
try:   # Connecting to tor services (only on linux)
    os.system('systemctl start tor.service')
except:
    Error = True 

print(line)
# INSTALLING ALL NEEDS LIBARYS
try:
    from bs4 import BeautifulSoup
    print('[OK] BeautifulSoup installed')
except:
    print('[-] BeautifulSoup not found')
    os.system('pip3 install bs4')
    from bs4 import BeautifulSoup
try:
    import requests
    print('[OK] Requests installed')
except:
    print('[-] Requests not found')
    os.system('pip3 install requests')
    import requests
try:
    import fake_useragent
    print('[OK] FakeUseragent installed')
except:
    print('[-] FakeUseragent not found')
    os.system('pip3 install fake_useragent')
    import fake_useragent
try:
    print(line +'\n[!] Starting a program')
    print('[!] Your platform ' + platform.platform())
    
    # Random User-Agent
    ua = fake_useragent.UserAgent() 
    user = ua.random
    header = {'User-Agent':str(user)}
    
    # Connection to the ip-site
    ipSite='http://icanhazip.com'
    adress = requests.get(ipSite, headers = header)

    # Check your ip adress
    print(line)
    print("[*] IP network:\n" + '[!] ' + adress.text + line)
    print("[!] Connecting to the Tor network /", end = "")
    
    # Animation
    for _ in range(7): 
        sleep(0.4); print(end = '░', flush = True)

    # Proxie tor's 
    proxie = {
        'http': 'socks5h://127.0.0.1:9050', 
        'https': 'socks5h://127.0.0.1:9050'
    }

    # Connecting to the network tor
    try:
        adress = requests.get(ipSite, proxies = proxie, headers = header)
        
    # Not connected
    except:
        connection = False
        print("/\n[-] Stopping connect to the Tor network\n" + line)
        
    # Connected
    else:
        connection = True
        print("/\n[+] Connected to the Tor network\n" + line)
        print("[*] IP Tor network:\n" + adress.text + line)

    # Parse site
    finally:
        url = input("[!] Uniform Resource Locator:\n[?] http://")

        if connection == True:
            page = requests.get("http://"+url.split()[0], proxies = proxie, headers = header)
        else:
            page = requests.get("http://"+url.split()[0], headers = header)

        soup = BeautifulSoup(page.text, "html.parser")

        # Default parse - HTML 
        if url.split()[0] == url.split()[-1]:
            with open("index.html","w+") as html:
                for tag in soup.findAll('html'):
                    html.write(str(tag))
                print(line,"\n[!] File: 'index.html' created")
        else:
            # Parse tag
            if url.split()[1] == url.split()[-1]:
                for tag in soup.findAll(url.split()[1]):
                    print(tag)
            # Parse inside/attribute
            else:
                if url.split()[2] == "inside":
                    for tag in soup.findAll(url.split()[1]):
                        print(tag.text)
                else:
                    for tag in soup.findAll(url.split()[1]):
                        print(tag[url.split()[2]])
        print(line + '\n Thanks for using "FOR GOOD TARGET" (͠≖ ͜ʖ͠≖)')
        
except:
    print('\n[-] Check your internet')
    print(line)
