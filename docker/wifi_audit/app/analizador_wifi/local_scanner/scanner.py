import json
import socket as s

import nmap3
from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether, ARP
from modo_monitor import utils

result = []
nuevalista = []
mac_list = []


# Decelera muchísimo la busqueda así que mirar como mejorarlo
def manf2(mac):
    with open('mac-vendors-export.json') as f:
        vendor = json.load(f)

    for p in vendor:
        if p['macPrefix'] == mac:
            return p['vendorName']

    return "Unknown"


# syn scan
def os_detection(target):
    nm = nmap3.Nmap()
    os_results = nm.nmap_os_detection(target)
    for key in os_results:
        if 'osmatch' in os_results[key] and os_results[key]['osmatch'] != []:
            os_name = os_results[key]['osmatch'][0]['name']
            os_type = os_results[key]['osmatch'][0]['osclass']['type']
            os_family = os_results[key]['osmatch'][0]['osclass']['osfamily']
            os_scan = {"name": os_name, "type": os_type, "osfamily": os_family}
            return os_scan
        else:
            os_scan = {"name": "Unknown", "type": "Unknown", "osfamily": "Unknown"}
            return os_scan

def arp_scan(ip):

    time = str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))


    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=1, verbose=0, retry=1)

    for sent, received in ans:
        device_name = s.getfqdn(received.psrc)
        if device_name == received.psrc:
            device_name = ""
        if received.hwsrc in mac_list:
            received.hwsrc = received.hwsrc
        else:
            mac_list.append(received.hwsrc)
        result.append({'IP': received.psrc, 'MAC': received.hwsrc.upper(), 'name': device_name, 'last_seen': time,
                       'vendor': utils.manf2(received.hwsrc.upper()[:8])})

        nuevalista.append(received.psrc)  # esto para guardar los dispositivos anteriores

    newlist = sorted(result, key=lambda k: int(k['IP'].split('.')[3]))

    return newlist


def get_connected_bssid():

    try:
        actual_bssid = subprocess.check_output("iwgetid --ap -r", shell=True).decode('utf-8').rstrip('\n')
    except:
        actual_bssid = "None"

    return actual_bssid


def get_connected_ssid():

    try:
        actual_ssid = subprocess.check_output("iwgetid -r", shell=True).decode('utf-8').rstrip('\n')
    except:
        actual_ssid = "None"

    return actual_ssid

