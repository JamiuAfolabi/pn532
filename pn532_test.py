from py532lib.i2c import *
from py532lib.frame import *

Pn532 = Pn532_i2c()
Pn532.SAMconfigure()

card_data = Pn532.read_mifare().get_data()

print(card_data)

print(card_data.decode())