# Computer Networks (CS-331) - Assignment 1

## Authors
Daksh Jain (22110066), Harshit (22110095)

## Overview
This repository includes scripts for analyzing network traffic through packet sniffing and processing techniques. These scripts enable users to:  

- Analyze packet sizes and transfer statistics from a `.pcap` file  
- Identify and save unique source-destination pairs  
- Capture network packets in real time using a packet sniffer  
- Extract and process metadata from captured packets  

## Setup
Before running any script, ensure you have Python installed along with the required dependencies. You may need to install `scapy`, `tcpreplay`, `numpy`, and `matplotlib`
```sh
pip install scapy numpy matplotlib
```

For tcpreplay:

### Ubuntu/Debian:  
```sh
sudo apt update && sudo apt install tcpreplay
```

### macOS:  
```sh
brew install tcpreplay
```

## Running the Scripts

### 1. Packet Analysis (part1.py)
This script analyzes a `.pcap` file.

#### Steps to Run:
1. Ensure you have a `.pcap` file downloaded and placed in the same directory as the script.  
2. Run the script with:  
   ```sh
   python3 part1.py
   ```

3. The script outputs:
   - Total data transferred
   - Total packets transferred
   - Min, max, and average packet sizes
   - Unique source-destination pairs (saved in `part1_b.txt`)
   - Source and destination IP flows (saved in `part1_c_source.txt` and `part1_c_dest.txt`)
   - Top data-transferring pair
   
### 1.d. Packet Sniffing (sniff.py)
This script captures packets replayed using `tcpreplay`.

### On the same machine: 
#### Steps to Run:
1. Start the packet sniffer in a terminal:  
   ```sh
   sudo python sniff.py
   ```
   This will capture packets on the `bridge100` interface.
   
3. In another terminal, replay packets from a .pcap file using tcpreplay:

  By packets per second (pps):
   ```sh
   sudo tcpreplay -i bridge100 --pps=1300 path/to/pcap/file
   ```

   By Mbps:
   ```sh
   sudo tcpreplay -i bridge100 --mbps=4.7 path/to/pcap/file
   ```

4. The script captures packets without loss at a maximum rate of ~1300 pps or 4.7 Mbps.

### 2. Catch Me If You Can (part2.py)

#### Steps to Run:
1. Run the script with:
   ```sh
   python part2.py
   ```
