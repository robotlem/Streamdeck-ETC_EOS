# Streamdeck-ETC_EOS
# misc. data
# Author: S. Pauthner
# Date:   16.02.2026


colordict = {
    "channels" : (19,33,46),
    "groups" : (54,71,87),
    "intensity" : (110,42,21),
    "focus": (5,56,37),
    "color": (49,49,61),
    "beam": (12,26,74),
    "presets": (8,56,66),
    "macros": (64,56,55),
    "effects": (54,20,74),
    "snapshots": (99,16,16),
    "magic_sheets": (87,12,40),
    "scenes": (8,74,37),
    "black": (0,0,0),
    "white": (255,255,255),
    "pink": (255,0,255),
    "yellow" : (255,255,0),
    "selected" : (255,0,255)
}

index_map = {
    "channels" : 0,
    "groups" : 1,
    "intensity" : 2,
    "focus": 3,
    "color": 4,
    "beam": 5,
    "presets": 6,
    "macros": 7,
    "effects": 8,
    "snapshots": 9,
    "magic_sheets": 10,
    "scenes": 11
}
index_map_reverse = {v: k for k, v in index_map.items()}

DS_MODES = [["Channels", colordict["channels"]], ["Groups", colordict["groups"]],
            [ "Intensity", colordict["intensity"]], [ "Focus", colordict["focus"]],
            ["Colors", colordict["color"]], [ "Beam", colordict["beam"]],
            ["Presets", colordict["presets"]], [ "Macros", colordict["macros"]],
            [ "Effects", colordict["effects"]],["Snapshots", colordict["snapshots"]],
            [ "Magic Sheets", colordict["magic_sheets"]], [ "Scenes", colordict["scenes"]]]



class Keyset:
    def __init__(self, number = "", text="" , background_color = colordict["black"], color=colordict["white"]):
        self.number = number
        self.text = text
        self.color = color
        self.background_color = background_color

### Menu Pages
PAGE_CONFIG_FULL = [Keyset("Full", "Deck", colordict["black"], colordict["selected"]),
               Keyset("", "Channels", colordict["channels"]),
               Keyset("", "Groups", colordict["groups"]),
               Keyset("", "Intensity", colordict["intensity"]),
               Keyset("", "Focus", colordict["focus"]),
               Keyset("", "Colors", colordict["color"]),
               Keyset("", "Beam", colordict["beam"]),
               Keyset("Up", "Brightness"),
               Keyset("Half", "Deck"),
               Keyset("", "Presets", colordict["presets"]),
               Keyset("", "Macros", colordict["macros"]),
               Keyset("", "Effects", colordict["effects"]),
               Keyset("", "Snapshots", colordict["snapshots"]),
               Keyset("", "Magic Sheets", colordict["magic_sheets"]),
               Keyset("", "Scenes", colordict["scenes"]),
               Keyset("Down", "Brightness"),
               ### Half time
               Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),
               Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),Keyset(),
               Keyset("EXIT", "Configuration"),
               ]

PAGE_CONFIG_HALF = [Keyset("Full", "Deck"),
               Keyset("", "Channels", colordict["channels"]),
               Keyset("", "Groups", colordict["groups"]),
               Keyset("", "Intensity", colordict["intensity"]),
               Keyset("", "Focus", colordict["focus"]),
               Keyset("", "Colors", colordict["color"]),
               Keyset("", "Beam", colordict["beam"]),
               Keyset("Up", "Brightness"),
               Keyset("Half", "Deck", colordict["black"], colordict["selected"]),
               Keyset("", "Presets", colordict["presets"]),
               Keyset("", "Macros", colordict["macros"]),
               Keyset("", "Effects", colordict["effects"]),
               Keyset("", "Snapshots", colordict["snapshots"]),
               Keyset("", "Magic Sheets", colordict["magic_sheets"]),
               Keyset("", "Scenes", colordict["scenes"]),
               Keyset("Down", "Brightness"),
               ### Half time
               Keyset(),
               Keyset("", "Channels", colordict["channels"]),
               Keyset("", "Groups", colordict["groups"]),
               Keyset("", "Intensity", colordict["intensity"]),
               Keyset("", "Focus", colordict["focus"]),
               Keyset("", "Colors", colordict["color"]),
               Keyset("", "Beam", colordict["beam"]),
               Keyset(),
               Keyset(),
               Keyset("", "Presets", colordict["presets"]),
               Keyset("", "Macros", colordict["macros"]),
               Keyset("", "Effects", colordict["effects"]),
               Keyset("", "Snapshots", colordict["snapshots"]),
               Keyset("", "Magic Sheets", colordict["magic_sheets"]),
               Keyset("", "Scenes", colordict["scenes"]),
               Keyset("EXIT", "Configuration"),
               ]


