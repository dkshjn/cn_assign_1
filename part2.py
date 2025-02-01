from scapy.all import rdpcap, TCP, IP, Raw

pcap_file = "5.pcap"
packets = rdpcap(pcap_file)

"""Q1"""

file_name = None
tcp_checksum = None
source_ip = None

for pkt in packets:
    if IP in pkt and TCP in pkt and pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors="ignore")
        if "The name of file is =" in payload:
            file_name = payload.split("The name of file is =")[-1].strip() # Extract the file name
            tcp_checksum = pkt[TCP].chksum  # TCP checksum
            source_ip = pkt[IP].src  # source IP
            break

print(f"File Name Found: {file_name}")
print(f"TCP Checksum: {tcp_checksum}")
print(f"Source IP: {source_ip}")

"""Q2"""
packet_count = sum(1 for pkt in packets if IP in pkt and pkt[IP].src == source_ip)

print(f"\nTotal Packets from {source_ip}: {packet_count}")


"""Q3"""
localhost_ip = "127.0.0.1"
phone_company = None
localhost_port = None

for pkt in packets:
    if IP in pkt and TCP in pkt and pkt[IP].src == localhost_ip and pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors="ignore")
        if "Company of phone is =" in payload:
            phone_company = payload.split("Company of phone is =")[-1].strip()
            localhost_port = pkt[TCP].sport
            break

print(f"\nPhone Company Found: {phone_company}")
print(f"Port Used by Localhost: {localhost_port}")

localhost_packet_count = sum(1 for pkt in packets if IP in pkt and pkt[IP].src == localhost_ip)

print(f"\nTotal Packets from Localhost: {localhost_packet_count}")