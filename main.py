# Streamdeck-ETC_EOS
# Main program
# Author: S. Pauthner
# Date:   16.02.2026


from streamdeck_stuff import *
from data import *
from osc import *



sd = CustomStreamDeck()

open_config_full(sd)

client = EOSClient("192.168.1.50", 8000)
client.connect()


input("ENTER to Quit…")

client.close()
sd.exit()