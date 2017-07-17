from network import LoRa
import socket
import binascii
import struct
import time

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params. Copy this from the TTN Device you created

dev_addr = struct.unpack(">l", binascii.unhexlify('26 04 10 18'.replace(' ','')))[0]#Device Address
nwk_swkey = binascii.unhexlify('DA 94 E4 99 81 B8 52 30 43 09 53 F7 A2 6B 4F B6'.replace(' ',''))# Network Session Key
app_swkey = binascii.unhexlify('40 55 C3 1E F6 0C 85 78 AD A1 18 A8 7D 81 19 B9'.replace(' ',''))# App Session Key

for channel in range(0, 72):
    lora.remove_channel(channel)

# set the  channels  frequency
lora.add_channel(0, frequency=923200000, dr_min=0, dr_max=4)
# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# remove all the non-default channels
for i in range(1, 16):
    lora.remove_channel(i)


# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)# parameter changed from the original Code

# make the socket blocking
s.setblocking(False)

while True:
    #s.send(b'Hola LORAWAN')
    s.send(bytes([0xFF,0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]))#Send some sample Bytes
    print("packet send")
    time.sleep(4)
    time.sleep(4)
    time.sleep(4)
    time.sleep(4)

# """ OTAA Node example compatible with the LoPy Nano Gateway """
#
# from network import LoRa
# import socket
# import binascii
# import struct
# import time
#
# # Initialize LoRa in LORAWAN mode.
# lora = LoRa(mode=LoRa.LORAWAN, public=True, adr=False)
#
# # create an OTA authentication params
# dev_eui = binascii.unhexlify('70 B3 D5 49 9D E0 B9 63'.replace(' ',''))
# app_eui = binascii.unhexlify('70 B3 D5 7E F0 00 63 C1'.replace(' ',''))
# app_key = binascii.unhexlify('8E AE EC 76 42 85 74 50 D3 00 3D 67 75 E5 84 14'.replace(' ',''))
#
# # auth = (bytes([0x70, 0xB3, 0xD5, 0x7E, 0xF0, 0x00, 0x63, 0xC1]),
#         # bytes([0x8E, 0xAE, 0xEC, 0x76, 0x42, 0x85, 0x74, 0x50, 0xD3, 0x00, 0x3D, 0x67, 0x75, 0xE5, 0x84, 0x14]))
#
# # for channel in range(0, 72):
# #     lora.remove_channel(channel)
#
# # for index in range(0, 72):
#     # lora.add_channel(index, frequency=923200000, dr_min=0, dr_max=3)
#
# # set the 3 default channels to the same frequency (must be before sending the OTAA join request)
# lora.add_channel(0, frequency=923200000, dr_min=0, dr_max=3)
# lora.add_channel(1, frequency=923400000, dr_min=0, dr_max=3)
# lora.add_channel(2, frequency=923400000, dr_min=0, dr_max=3)
#
# # join a network using OTAA
# lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
# # lora.join(activation=LoRa.OTAA, auth=auth, timeout=0)
#
# # wait until the module has joined the network
# while not lora.has_joined():
#     time.sleep(2.5)
#     print('Not joined yet...')
#
# # # remove all the non-default channels
# # for i in range(3, 16):
# #     lora.remove_channel(i)
#
# # create a LoRa socket
# s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#
# # set the LoRaWAN data rate
# s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
#
# # make the socket blocking
# s.setblocking(False)
#
# time.sleep(5.0)
#
# for i in range (200):
#     s.send(b'PKT #' + bytes([i]))
#     time.sleep(4)
#     rx = s.recv(256)
#     if rx:
#         print(rx)
#     time.sleep(6)

# from network import LoRa
# import binascii
# lora = LoRa(mode=LoRa.LORAWAN)
# print("Lora MAC is: ")
# print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
