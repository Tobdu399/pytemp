import tkinter
import pathlib
import pyglet

path = str(pathlib.Path(__file__).resolve().parent)

pyglet.font.add_file(path + "/fonts/chango.ttf")
pyglet.font.add_file(path + "/fonts/ubuntu.ttf")

location_placeholder = "Location ( i.e. London )"
