
from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper
from StreamDeck.DeviceManager import DeviceManager

def init_streamdeck():
    # search Stream Deck
    streamdecks = DeviceManager().enumerate()

    if not streamdecks:
        raise RuntimeError("Kein Stream Deck gefunden")

    deck = streamdecks[0]
    deck.open()
    deck.reset()

    print(f"Connected to: {deck.deck_type()}")
    return deck

class key:

    def __init__(self, number, text, font_number, font, color, background_color, key_size, deck, key_index):
        self.number = number
        self.text = text
        self.font_number = font_number
        self.font_text = font
        self.color = color
        self.background_color = background_color
        self.key_size = key_size
        #self.image = Image.new("RGB", (self.key_size[0], self.key_size[1]), color=background_color)
        self.deck = deck
        self.key_index = key_index

    def update(self):
        image = Image.new("RGB", (self.key_size[0], self.key_size[1]), color=self.background_color)
        draw = ImageDraw.Draw(image)
        nbox = draw.textbbox((0, 0), self.number, font=self.font_number)
        number_w = nbox[2] - nbox[0]
        number_h = nbox[3] - nbox[1]
        draw.text(
            ((self.key_size[0] - number_w) / 2, (self.key_size[1] - number_h) / 6),
            self.number,
            fill=self.color,
            font=self.font_number
        )

        tbox = draw.textbbox((0, 0), self.text, font=self.font_text)
        text_w = tbox[2] - tbox[0]
        text_h = tbox[3] - tbox[1]
        draw.text(
            ((self.key_size[0] - text_w) / 2, (self.key_size[1] - text_h) / 1.5),
            self.text,
            fill=self.color,
            font=self.font_text
        )
        st_image =  PILHelper.to_native_format(self.deck, image)
        self.deck.set_key_image(self.key_index, st_image)



