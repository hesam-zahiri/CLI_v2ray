import subprocess
import logging

# Log settings
logging.basicConfig(
    filename='tunnel.log',  # Log file name
    level=logging.DEBUG,  # Log level 
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Get vmess config from user
vmess_config = input("Please enter vmess/vless/trojan/shadowsockss config: ")

# v2ray command to tunnel the system
command = f"v2ray -config {vmess_config}"

try:
    # Command execution and system tunneling
    subprocess.run(command, shell=True)
except Exception as e:
    logging.error(f'Error executing the command: {e}')
else:
    logging.info('The connection to the server was established and the system was tunneled')
