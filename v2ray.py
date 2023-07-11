#!/usr/bin/env python3

import subprocess

# Get v2ray config from user
vmess_config = input("Please enter your vmess/vless/trojan/shadowsocks config: ")

# Setting the V2Ray configuration file
with open('/etc/v2ray/config.json', 'w') as config_file:
    config_file.write(vmess_config)

# Start the V2Ray service
subprocess.run(['systemctl', 'start', 'v2ray'])

# Show logs live
subprocess.run(['tail', '-f', '/var/log/v2ray/error.log'])
