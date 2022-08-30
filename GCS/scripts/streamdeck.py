#!/usr/bin/env python3

import os
import threading

from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper

# Folder location of image assets used by this example.
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "Assets")

def render_key_image(deck, icon_filename, font_filename, label_text):
    icon = Image.open(icon_filename)
    image = PILHelper.create_scaled_image(deck, icon, margins=[0, 0, 20, 0])

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_filename, 14)
    draw.text((image.width / 2, image.height - 5), text=label_text, font=font, anchor="ms", fill="white")

    return PILHelper.to_native_format(deck, image)


def get_key_style(deck, key, state):
    exit_key_index = deck.key_count() - 1

    if key == exit_key_index:
        name = exit_key_index
        icon = "{}.png".format("Exit")
        font = "Roboto-Regular.ttf"
        label = "Bye" if state else "Exit"
    else:
        name = key
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Key {}".format(key)

    if key == 0:
        name = 0
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "None"

    if key == 1:
        name = 1
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Guided"

    if key == 2:
        name = 2
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Auto"

    if key == 3:
        name = 3
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Circle"

    if key == 4:
        name = 4
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Loiter"

    if key == 5:
        name = 5
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "guided 100"

    if key == 6:
        name = 6
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Gimbal Up"

    if key == 7:
        name = 7
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Gimbal Down"

    if key == 8:
        name = 8
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Zoom In"

    if key == 9:
        name = 9
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Zoom Out"

    if key == 10:
        name = 10 
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Cam1 Tilt"

    if key == 11:
        name = 11 
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Gimbal Left"

    if key == 12:
        name = 12 
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Gimbal Right"

    if key == 13:
        name = 13 
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Gimbal Center"



    return {
        "name": name,
        "icon": os.path.join(ASSETS_PATH, icon),
        "font": os.path.join(ASSETS_PATH, font),
        "label": label
    }

def update_key_image(deck, key, state):
    key_style = get_key_style(deck, key, state)

    image = render_key_image(deck, key_style["icon"], key_style["font"], key_style["label"])

    with deck:
        deck.set_key_image(key, image)


def streamdeck_exit(deck):
    with deck:
        deck.reset()     
        deck.close()

def key_change_callback(deck, key, state):
    print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)

    update_key_image(deck, key, state)

    if state:
        key_style = get_key_style(deck, key, state)

        if key_style["name"] == "loiter":
            print("loiter")
        if key_style["name"] == "guided":
            print("guided")

        if key_style["name"] == "exit":
            streamdeck_exit(deck)

def streamdeck_init():
    streamdecks = DeviceManager().enumerate()

    deck = streamdecks[0]

    if not deck.is_visual():
        return

    deck.open()
    deck.reset()

    print("Opened '{}' device (serial number: '{}', fw: '{}')".format(
        deck.deck_type(), deck.get_serial_number(), deck.get_firmware_version()
    ))

    deck.set_brightness(30)

    return deck

if __name__ == "__main__":
    deck = streamdeck_init()
    for key in range(deck.key_count()):
        update_key_image(deck, key, False)

    deck.set_key_callback(key_change_callback)

    for t in threading.enumerate():
        try:
            t.join()
        except RuntimeError:
            pass


