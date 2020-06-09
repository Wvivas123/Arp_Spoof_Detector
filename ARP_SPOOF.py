import os
from datetime import datetime

now = datetime.now()

ip_addr = []
mac_addr = []


def get_lines():
    with os.popen('arp -a') as f:
        data = f.read()
        for i in data.split('\n')[:-1]:
            a = i.split()[1]
            ip_addr.append(a)
        for i in data.split('\n')[:-1]:
            b = i.split()[3]
            mac_addr.append(b)

def check_mac(mac_addr):
    for elem in mac_addr:
        if mac_addr.count(elem) > 1:
            print("There Is a spoofed Mac")
            filename = "LOG " + str(now) + ".txt"
            file = open(filename, 'w')

            file.write("LOG INFO:")
            file.write("ARP TABLE :")
            file.write(str(ip_addr))
            file.write(str(mac_addr))
            file.write("[+]---OUTPUT---[+]")
            file.write("-- Spoofed Mac Address on Network --")
    else:
        filename = "LOG " + str(now) + ".txt"
        file = open(filename, 'w')

        file.write("LOG INFO:")
        file.write("ARP TABLE :")
        file.write(str(ip_addr))
        file.write(str(mac_addr))
        file.write("[+]---OUTPUT---[+]")
        file.write("--No Duplicate Macs on Network-- ")









get_lines()
check_mac(mac_addr)