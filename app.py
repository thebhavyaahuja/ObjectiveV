import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openvpn_api import Client

user='a'
pass_decrypted='b'

# VPN configuration
vpn_config = {
    'host': 'your-vpn-host',
    'port': 1194,
    'config': 'windows.ovpn',
    'username': user,
    'password': pass_decrypted,
}

# Connect to VPN
vpn_client = Client()
vpn_client.connect(**vpn_config)

# Wait for VPN connection to be established
time.sleep(10)

# Open browser
driver = webdriver.Firefox()
driver.get("")