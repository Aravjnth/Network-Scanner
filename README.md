# Network Scanner

## Overview

The Network Scanner project is a Python-based tool designed to scan networks, discover devices, and gather information about them. This tool provides capabilities for network reconnaissance, port scanning, service identification, and operating system detection, aiding in network administration, security assessment, and troubleshooting.

## Features

- Scans specified IP ranges or targets for active hosts.
- Performs port scanning to identify open ports and services.
- Detects the operating system of discovered hosts.
- Generates detailed reports and visualizations of network topology.
- Supports customization of scan parameters and output formats.
- User-friendly command-line interface (CLI) for configuration and operation.

## Requirements

- Python 3.x
- `scapy` library for network packet crafting and sniffing
- `python-nmap` library for Nmap integration (optional)
- `matplotlib` library for generating network visualizations (optional)
- `pandas` library for data analysis (optional)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Network-Scanner.git
    cd network-scanner
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Perform a basic network scan:
    ```bash
    python network_scanner.py --ip <target-ip-range>
    ```

2. Perform a detailed port scan using Nmap:
    ```bash
    python port_scanner.py --ip <target-ip> --ports <port-range>
    ```

3. Visualize network topology and scan results:
    ```bash
    python visualize_network.py --ip <target-ip-range>
    ```

### Example

Perform a basic network scan:
```bash
python network_scanner.py --ip 192.168.1.0/24
```

Perform a port scan using Nmap:
```bash
python port_scanner.py --ip 192.168.1.100 --ports 1-1000
```

Visualize network topology:
```bash
python visualize_network.py --ip 192.168.1.0/24
```

## Options

- `--ip`: IP range or target IP address to scan.
- `--ports`: Port range or specific ports to scan (for port_scanner.py).
- Customize scan parameters and output formats in `config.py`.

## Legal Disclaimer

This Network Scanner tool is intended for network administration and security assessment purposes within authorized environments. Ensure compliance with legal regulations and obtain appropriate consent before scanning networks. The developers assume no liability for any misuse or damage caused by this application.

## Contributing

Contributions to this project are welcome! Fork the repository, add new features, improve scanning techniques, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact me at www.linkedin.com/in/aravinth-aj
