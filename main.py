# Streamdeck-ETC_EOS
# Main program
# Author: S. Pauthner
# Date:   16.02.2026


from streamdeck_stuff import *
from data import *



sd = CustomStreamDeck()


sd.keys[0].set_callback(lambda f : print("Hallo Welt, Taste ", f))

sd.set_keyset(PAGE_CONFIG)
sd.update_all_keys()



input("ENTER to Quit…")


sd.exit()