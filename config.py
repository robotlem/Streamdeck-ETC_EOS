from PIL.ImageChops import constant

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
    "yellow" : (255,255,0)
}
DS_MODES = [["Channels", colordict["channels"]], ["Groups", colordict["groups"]],
            [ "Intensity", colordict["intensity"]], [ "Focus", colordict["focus"]],
            ["Colors", colordict["color"]], [ "Beam", colordict["beam"]],
            ["Presets", colordict["presets"]], [ "Macros", colordict["macros"]],
            [ "Effects", colordict["effects"]],["Snapshots", colordict["snapshots"]],
            [ "Magic Sheets", colordict["magic_sheets"]], [ "Scenes", colordict["scenes"]]]




UP_KEY_1 = 23
DOWN_KEY_1 = 31
UP_KEY_2 = 7
DOWN_KEY_2 = 15

LIVE_KEY = 31
BRIGHTER_KEY = 7
DARKER_KEY = 15
FULL_KEY = 0
HALF_KEY = 8

class STATUS:
    config = True
    full = True
    bank1_mode = 0
    bank2_mode = 0
    brightness = 100




