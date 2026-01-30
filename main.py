# Streamdeck-ETC_EOS
# Main program
# Author: S. Pauthner
# Date:   30.01.2026

from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from PIL import Image, ImageDraw, ImageFont
from streamdeck_stuff import *
from config import *


def on_key_change(deck, key, state):
    """
    state == True  -> Taste gedrückt
    state == False -> Taste losgelassen
    """
    global keys
    if state:
        if STATUS.config:
            if key == FULL_KEY:
                STATUS.full = True
                make_black()
                run_menu()
            if key == HALF_KEY:
                STATUS.full = False
                run_menu()
            if key == BRIGHTER_KEY:
                STATUS.brightness += 10
                if STATUS.brightness > 100:
                    STATUS.brightness = 100
                deck.set_brightness(STATUS.brightness)
            if key == DARKER_KEY:
                STATUS.brightness -= 10
                if STATUS.brightness < 10:
                    STATUS.brightness = 10
                deck.set_brightness(STATUS.brightness)
            if key == LIVE_KEY:
                STATUS.config = False
            if 1 <= key <= 6:
                STATUS.bank1_mode = key - 1
                make_black(no_black = True)
                run_menu()
            if key >= 9 and key <= 14:
                STATUS.bank1_mode = key - 3
                run_menu()

        keys[key].color = colordict["yellow"]
        keys[key].update()
    else:
        keys[key].color = colordict["white"]
        keys[key].update()

def make_black(no_black = False):
    global keys
    for n in keys:
        if not no_black:
            n.background_color = colordict["black"]
            n.number = ""
            n.text = ""
        n.color = colordict["white"]
        n.update()

def run_menu():
    global keys
    if STATUS.config:
        # Set the direct selects 1:
        for x in range(1,7):
            keys[x].text = DS_MODES[x-1][0]
            keys[x].background_color = DS_MODES[x-1][1]
            keys[x].update()
        for x in range(9,15):
            keys[x].text = DS_MODES[x-3][0]
            keys[x].background_color = DS_MODES[x-3][1]
            keys[x].update()
        offset = 1
        if (STATUS.bank1_mode > 8):
            offset = 3
        keys[STATUS.bank1_mode+offset].color = colordict["pink"]
        keys[STATUS.bank1_mode+offset].update()
        # Set the 2nd page of direct selects
        if not STATUS.full:
            for x in range(1, 7):
                keys[x+16].text = DS_MODES[x - 1][0]
                keys[x+16].background_color = DS_MODES[x - 1][1]
                keys[x+16].update()
            for x in range(9, 15):
                keys[x+16].text = DS_MODES[x - 3][0]
                keys[x+16].background_color = DS_MODES[x - 3][1]
                keys[x+16].update()
            offset = 17
            if (STATUS.bank1_mode > 8):
                offset = 19
            keys[STATUS.bank2_mode + offset].color = colordict["pink"]
            keys[STATUS.bank2_mode + offset].update()
        keys[FULL_KEY].number = "FULL"
        keys[FULL_KEY].update()
        keys[HALF_KEY].number = "HALF"
        keys[HALF_KEY].update()
        keys[BRIGHTER_KEY].number = "+"
        keys[BRIGHTER_KEY].text= "Brightness"
        keys[BRIGHTER_KEY].update()
        keys[DARKER_KEY].number = "-"
        keys[DARKER_KEY].text= "Brightness"
        keys[DARKER_KEY].update()
        keys[LIVE_KEY].number = "EXIT"
        keys[LIVE_KEY].text = "Config"
        keys[LIVE_KEY].update()




#####################
### Stream Deck setup
#####################
deck = init_streamdeck()
deck.set_brightness(100)

deck.set_key_callback(on_key_change)

# Key-Infos
key_size = deck.key_image_format()['size']

# Font
try:
    font_number = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans-Bold.ttf", 25)
    font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans-Regular.ttf", 15)
except:
    font_number = ImageFont.load_default()
    font = ImageFont.load_default()

keys = []
for x in range(32):
    keys.append(key("", "", font_number, font, colordict["white"], colordict["black"], key_size, deck, x))

# Apply keys
for x in keys:
    x.update()

run_menu()


input("ENTER to Quit…")

deck.reset()
deck.close()