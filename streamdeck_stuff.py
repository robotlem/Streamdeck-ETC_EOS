# Streamdeck-ETC_EOS
# Streamdeck-Class
# Author: S. Pauthner
# Date:   16.02.2026

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper
from StreamDeck.DeviceManager import DeviceManager
from data import *

def init_streamdeck():
    # search Stream Deck
    streamdecks = DeviceManager().enumerate()

    if not streamdecks:
        raise RuntimeError("No Streamdeck found")

    deck = streamdecks[0]
    deck.open()
    deck.reset()

    print(f"Connected to: {deck.deck_type()}")
    return deck

class key:
    def __init__(self, font_number, font_text, color, color_highlight, background_color, deck, key_index):
        self._number = ""
        self._text = ""
        self._font_number = font_number
        self._font_text = font_text
        self.color = color
        self.color_highlight = color_highlight
        self.background_color = background_color
        self._key_size = deck.key_image_format()['size']
        self._deck = deck
        self._key_index = key_index
        self._callback = None

    def set_callback(self, callback):        # Callback function get's key_index as parameter
        self._callback = callback

    def set_keyset(self, keyset):
        self.set_content(keyset.number, keyset.text)
        self.color = keyset.color
        self.background_color = keyset.background_color

    def pushed(self):
        if self._callback:
            self._callback(self._key_index)
        self.update(self.color_highlight)

    def released(self):
        self.update()

    def set_content(self, number, text):
        self._number = number
        self._text = text

    def update(self, textcolor=None):
        if textcolor is None:
            textcolor = self.color
        image = Image.new("RGB", (self._key_size[0], self._key_size[1]), color=self.background_color)
        draw = ImageDraw.Draw(image)
        nbox = draw.textbbox((0, 0), self._number, font=self._font_number)
        number_w = nbox[2] - nbox[0]
        number_h = nbox[3] - nbox[1]
        draw.text(
            ((self._key_size[0] - number_w) / 2, (self._key_size[1] - number_h) / 6),
            self._number,
            fill=textcolor,
            font=self._font_number
        )

        tbox = draw.textbbox((0, 0), self._text, font=self._font_text)
        text_w = tbox[2] - tbox[0]
        text_h = tbox[3] - tbox[1]
        draw.text(
            ((self._key_size[0] - text_w) / 2, (self._key_size[1] - text_h) / 1.5),
            self._text,
            fill=textcolor,
            font=self._font_text
        )
        st_image =  PILHelper.to_native_format(self._deck, image)
        self._deck.set_key_image(self._key_index, st_image)



class CustomStreamDeck:
    brightness = 100
    palette = ["channels", "channels"]
    def __init__(self):
        self.deck = init_streamdeck()
        try:
            font_number = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans-Bold.ttf", 25)
            font = ImageFont.truetype("./fonts/Open_Sans/static/OpenSans-Regular.ttf", 15)
        except:
            font_number = ImageFont.load_default()
            font = ImageFont.load_default()
        self.keys = []
        for x in range(32):
            self.keys.append(key(font_number, font, colordict["white"], colordict["yellow"], colordict["black"], self.deck, x))
        for x in self.keys:
            x.update()
        self.deck.set_key_callback(self.key_action_callback)
        self.deck.set_brightness(self.brightness)

    def brighter(self):
        self.brightness = min(100, self.brightness+10)
        if self.brightness == 50:           # Compensate strange dimming behaviour
            self.brightness = 80
        self.deck.set_brightness(self.brightness)

    def darker(self):
        self.brightness = max(10, self.brightness-10)
        if self.brightness == 70:           # Compensate strange dimming behaviour
            self.brightness = 40
        self.deck.set_brightness(self.brightness)
        self.deck.set_brightness(self.brightness)

    def reset(self):
        for x in self.keys:
            x.set_content("", "")
            x.color = colordict["white"]
            x.background_color = colordict["black"]
            x.update()

    def reset_all_callbacks(self):
        for x in self.keys:
            x.set_callback(None)
    def update_all_keys(self):
        for x in self.keys:
            x.update()
    def set_keyset(self, keyset):
        for i in range(len(self.keys)):
            self.keys[i].set_keyset(keyset[i])

    def key_action_callback(self, deck, key_nr, state):      # keyNr begins at 0
        if state:
            self.keys[key_nr].pushed()
        else:
            self.keys[key_nr].released()

    def exit(self):
        self.deck.reset()
        self.deck.close()

    def set_palette_from_key_press(self, key_nr):
        if key_nr < 16:
            palette_idx = 0
            key_nr -= 1
        else:
            palette_idx = 1
            key_nr -= 17
        if key_nr >= 6: key_nr -= 2
        self.palette[palette_idx] = index_map_reverse[key_nr]

        if palette_idx == 0:
            highlight_current_panel(self)
        else:
            highlight_current_panel(self, False)


def open_live_full(sd):
    print("Opening Live Full")

def open_live_half(sd):
    print("Opening Live Half")


def open_config_full(sd):
    sd.reset_all_callbacks()
    sd.keys[7].set_callback(lambda x: sd.brighter())
    sd.keys[15].set_callback(lambda x: sd.darker())
    sd.keys[8].set_callback(lambda x: open_config_half(sd))
    sd.keys[31].set_callback(lambda x: open_live_full(sd))
    sd.set_keyset(PAGE_CONFIG_FULL)
    connect_config_selection_keys(sd)
    highlight_current_panel(sd)     # contains update all keys

def open_config_half(sd):
    sd.reset_all_callbacks()
    sd.keys[7].set_callback(lambda x: sd.brighter())
    sd.keys[15].set_callback(lambda x: sd.darker())
    sd.keys[0].set_callback(lambda x: open_config_full(sd))
    sd.keys[31].set_callback(lambda x: open_live_half(sd))
    sd.set_keyset(PAGE_CONFIG_HALF)
    connect_config_selection_keys(sd)
    connect_config_selection_keys(sd, False)
    highlight_current_panel(sd)     # contains update all keys
    highlight_current_panel(sd, upper_set = False)

def highlight_current_panel(sd, upper_set = True):
    if upper_set:
        key_idx = [1,2,3,4,5,6,9,10,11,12,13,14]
        keyword = sd.palette[0]
        idx = 1
    else:
        key_idx = [17,18,19,20,21,22,25,26,27,28,29,30]
        keyword = sd.palette[1]
        idx = 17
    for i in key_idx:
        sd.keys[i].color = colordict["white"]
    idx += index_map[keyword]
    if index_map[keyword] >= 6: idx += 2
    sd.keys[idx].color = colordict["selected"]
    sd.update_all_keys()

def connect_config_selection_keys(sd, upper_set = True):
    if upper_set:
        key_idx = [1,2,3,4,5,6,9,10,11,12,13,14]
    else:
        key_idx = [17,18,19,20,21,22,25,26,27,28,29,30]
    for i in key_idx:
        sd.keys[i].set_callback(lambda x: sd.set_palette_from_key_press(x))
