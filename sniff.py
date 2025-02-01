from scapy.all import sniff

interface = "bridge100" # New bridge created so there is no interference

packet_count = 0
capture_limit = 805996  # Total packets in the PCAP

def packet_handler(pkt):
    global packet_count
    packet_count += 1
    print(f"Captured Packet #{packet_count}: {pkt.summary()}")

def stop_sniffing(pkt):
    global packet_count
    return packet_count >= capture_limit  # Stops when the limit is reached

print(f"Starting capture on {interface}...")
sniff(iface=interface, prn=packet_handler, store=False, stop_filter=stop_sniffing)

print("\nCapture complete.")
