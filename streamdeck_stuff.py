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

