""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import binascii

GATEWAY_ID = '70b3d549980818c7'

SERVER = 'router.as2.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

# WIFI_SSID = 'TOT-Home92/215_2.4G_plus'
# WIFI_PASS = '0894541262'
WIFI_SSID = 'mixen-ap-f2'
WIFI_PASS = 'mixensensagri'

LORA_FREQUENCY = 923200000
LORA_DR = "SF7BW125" # DR_5
