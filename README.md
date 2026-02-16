# Streamdeck-ETC_EOS
A standalone application to use a Streamdeck XL for direct selects

## Used librarys
- [streamdeck](https://github.com/abcminiuser/python-elgato-streamdeck) library (```pip install streamdeck```)

## Usage
Start the main.py. You may need to set the venv first ```source venv/bin/activate```.
The program will automatically connect to ETC EOS (default 127.0.0.1:3032) with OSC/TCP.
A configuration page will be shown on the streamdeck.
There are 2 display styles: 
1. Full: All keys will display one category (e.g. Macros)
2. Half: The half of the keys will display one category while the other half displays another one (e.g. Groups and Colors)

To get back to the style select press the up and down button simultaneously.


## Troubleshooting
