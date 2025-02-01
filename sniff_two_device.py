from scapy.all import sniff

interface = "\\Device\\NPF_{73FAF752-D0DE-4CCE-9F52-A75607E1EA82}"
packet_count = 0
def packet_handler(pkt):
    global packet_count
    packet_count += 1
    print(f"Captured Packet #{packet_count} : {pkt.summary()}")

print(f"Starting capture on {interface}... (Capturing only packets from Mac)")
sniff(iface=interface, prn=packet_handler, store=False, promisc=True)
