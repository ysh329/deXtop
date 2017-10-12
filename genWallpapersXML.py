#!/bin/python2
# -*- coding: utf-8 -*-

__author__ = "Shuai Yuan"

debug = True

import xml.dom.minidom as Dom
import datetime
import os

def gen_wallpapers(options="zoom", pcolor="#000000", scolor="#000000", shade_type="solid"):
    doc = Dom.Document()
    wallpapers_node = doc.createElement("Wallpapers")
    return wallpapers_node

def gen_wallpaper(name, filename, options="zoom", pcolor="#000000", scolor="#000000", shade_type="solid"):
    doc = Dom.Document()
    wallpaper_node = doc.createElement("wallpaper")

    name_node = doc.createElement("name")
    name_value = doc.createTextNode(name)
    name_node.appendChild(name_value)

    filename_node = doc.createElement("filename")
    filename_value = doc.createTextNode(filename)
    filename_node.appendChild(filename_value)

    options_node = doc.createElement("options")
    options_value = doc.createTextNode(options)
    options_node.appendChild(options_value)

    pcolor_node = doc.createElement("pcolor")
    pcolor_value = doc.createTextNode(pcolor)
    pcolor_node.appendChild(pcolor_value)

    scolor_node = doc.createElement("scolor")
    scolor_value = doc.createTextNode(scolor)
    scolor_node.appendChild(scolor_value)

    shade_node = doc.createElement("shade_type")
    shade_value = doc.createElement(shade_type)
    shade_node.appendChild(shade_value)

    wallpaper_node.appendChild(name_node)
    wallpaper_node.appendChild(filename_node)
    wallpaper_node.appendChild(options_node)
    wallpaper_node.appendChild(pcolor_node)
    wallpaper_node.appendChild(scolor_node)
    wallpaper_node.appendChild(shade_node)

    if debug:
        print(wallpaper_node.toxml())

    return wallpaper_node


def gen_XML(xml_doc, xml_path):
    with open(xml_path, "w") as f:
        f.write(xml_doc.toprettyxml(indent="\t",\
                newl="\n",\
                encoding="utf-8")\
                )


def get_img_list():
    pass

if __name__ == "__main__":
    gen_wallpaper("1", "2", "3", "4", "5", "6")
