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
            file.write("LOG INFO: \n")
            file.write("ARP TABLE : \n")
            file.write(str(ip_addr) + "\n")
            file.write(str(mac_addr) + "\n")
            file.write("[+]---OUTPUT---[+] \n")
            file.write("--There is a spoofed Mac on the network-- ")

    else:
        filename = "LOG - " + str(now) + ".txt"
        file = open(filename, 'w')

        file.write("LOG INFO: \n")
        file.write("--------- \n")
        file.write("ARP TABLE : \n")
        file.write(str(ip_addr) + "\n")
        file.write(str(mac_addr) + "\n")
        file.write("[+]---OUTPUT---[+] \n")
        file.write("--No Duplicate Macs on Network-- ")









get_lines()
check_mac(mac_addr)