from scapy.all import rdpcap, IP, TCP, UDP
import matplotlib.pyplot as plt
import numpy as np
import time
from collections import defaultdict

pcap_file = "5.pcap"

packets = rdpcap(pcap_file)

packet_sizes = [len(pkt) for pkt in packets]

total_bytes = sum(packet_sizes)
packet_count = len(packet_sizes)
min_size = min(packet_sizes)
max_size = max(packet_sizes)
avg_size = np.mean(packet_sizes)

"""(Part 1 a. part)"""
# Print the values
print(f"Total Data Transferred(Bytes): {total_bytes}")
print(f"Total Packets Transferred: {packet_count}")
print(f"Min Packet Size: {min_size} bytes")
print(f"Max Packet Size: {max_size} bytes")
print(f"Average Packet Size: {avg_size:.2f} bytes")

# Plot histogram
plt.figure(figsize=(12, 8))
plt.hist(packet_sizes, bins=60, edgecolor="black")
plt.xlabel("Packet Size (Bytes)")
plt.ylabel("Frequency")
plt.title("Packet Size Distribution")
plt.show()

"""(Part 1 b. part)"""
src_dst_pairs = set()

for pkt in packets:
    if IP in pkt and (TCP in pkt or UDP in pkt):
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        src_port = pkt[TCP].sport if TCP in pkt else pkt[UDP].sport if UDP in pkt else "N/A"
        dst_port = pkt[TCP].dport if TCP in pkt else pkt[UDP].dport if UDP in pkt else "N/A"
        src_dst_pairs.add(f"{src_ip}:{src_port} → {dst_ip}:{dst_port}")

print(f"\nNumber of unique source-destination pairs: {len(src_dst_pairs)}")

# Save in a txt file 
output_file = "part1_b.txt"

with open(output_file, "w") as f:
    for pair in src_dst_pairs:
        f.write(pair + "\n")

print(f"\nAll unique source-destination pairs saved to {output_file}")


"""(Part 1 c. Count Flows Per IP)"""
src_flows = defaultdict(int)
dst_flows = defaultdict(int)
data_transferred = defaultdict(int)

for pkt in packets:
    if IP in pkt and (TCP in pkt or UDP in pkt):
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        src_port = pkt[TCP].sport if TCP in pkt else pkt[UDP].sport if UDP in pkt else "N/A"
        dst_port = pkt[TCP].dport if TCP in pkt else pkt[UDP].dport if UDP in pkt else "N/A"

        src_flows[src_ip] += 1
        dst_flows[dst_ip] += 1
        flow_key = f"{src_ip}:{src_port} → {dst_ip}:{dst_port}"
        data_transferred[flow_key] += len(pkt)

# Save all source IP flows to a file
source_flows_file = "part1_c_source.txt"
with open(source_flows_file, "w") as f:
    for ip, count in sorted(src_flows.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{ip}: {count} flows\n")

print(f"\nAll source IP flows saved to {source_flows_file}")

# Save all destination IP flows to a file
destination_flows_file = "part1_c_dest.txt"
with open(destination_flows_file, "w") as f:
    for ip, count in sorted(dst_flows.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{ip}: {count} flows\n")

print(f"\nAll destination IP flows saved to {destination_flows_file}")

# Find the source-destination pair that transferred the most data
top_transfer = max(data_transferred.items(), key=lambda x: x[1])

print("\nTop Data Transferring Pair:")
print(f"{top_transfer[0]} transferred {top_transfer[1]} bytes")