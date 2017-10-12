#!/bin/python2
# -*- coding: utf-8 -*-

__author__ = "Shuai Yuan"

debug = True

import xml.dom.minidom as Dom
import datetime
import os

def gen_transition(from_file_path, to_file_path, transition_sec=5.0):
    # init
    doc = Dom.Document()
    transition_node = doc.createElement("transition")

    # create
    duration_node = doc.createElement("duration")
    duration_value = doc.createTextNode(str(transition_sec))
    duration_node.appendChild(duration_value)

    from_node = doc.createElement("from")
    from_value = doc.createTextNode(from_file_path)
    from_node.appendChild(from_value)

    to_node = doc.createElement("to")
    to_value = doc.createTextNode(to_file_path)
    to_node.appendChild(to_value)

    transition_node.appendChild(duration_node)
    transition_node.appendChild(from_node)
    transition_node.appendChild(to_node)

    # debug
    if debug:
        print(transition_node.toxml())
    return transition_node


def gen_static(file_path, static_sec=1800.0):
    # init
    doc = Dom.Document()
    static_node = doc.createElement("static")

    # create
    duration_node = doc.createElement("duration")
    duration_value = doc.createTextNode(str(static_sec))
    duration_node.appendChild(duration_value)

    file_node = doc.createElement("file")
    file_value = doc.createTextNode(file_path)
    file_node.appendChild(file_value)

    static_node.appendChild(duration_node)
    static_node.appendChild(file_node)

    # debug
    if debug:
        print(static_node.toxml())
    return static_node

def gen_starttime(date=None):
    # init
    doc = Dom.Document()
    if date == None:
        date = datetime.datetime.now()
    start_node = doc.createElement("starttime")

    # create
    year_node = doc.createElement("year")
    year_value = doc.createTextNode(str(date.year))
    year_node.appendChild(year_value)

    month_node = doc.createElement("month")
    month_value = doc.createTextNode(str(date.month))
    month_node.appendChild(month_value)

    day_node = doc.createElement("day")
    day_value = doc.createTextNode(str(date.day))
    day_node.appendChild(day_value)

    hour_node = doc.createElement("hour")
    hour_value = doc.createTextNode(str(date.hour))
    hour_node.appendChild(hour_value)

    minute_node = doc.createElement("minute")
    minute_value = doc.createTextNode(str(date.minute))
    minute_node.appendChild(minute_value)

    second_node = doc.createElement("second")
    second_value = doc.createTextNode(str(date.second))
    second_node.appendChild(second_value)

    start_node.appendChild(year_node)
    start_node.appendChild(month_node)
    start_node.appendChild(day_node)
    start_node.appendChild(hour_node)
    start_node.appendChild(minute_node)
    start_node.appendChild(second_node)

    # debug
    if debug:
        print(start_node.toxml())

    return start_node

def gen_background(img_path_list, static_sec=1795.0, transition_sec=5.0):
    # init
    doc = Dom.Document()
    background_node = doc.createElement("background")
    background_child_list = []

    starttime_node = gen_starttime()
    background_child_list.append(starttime_node)

    # create nodes
    for img_idx in xrange(len(img_path_list)):
        # from and to imgs
        if img_idx == len(img_path_list)-1:
            from_img = img_path_list[img_idx]
            to_img = img_path_list[0]
        else:
            from_img = img_path_list[img_idx]
            to_img = img_path_list[img_idx+1]

        static_node = gen_static(from_img, static_sec)
        transition_node = gen_transition(from_img, to_img, transition_sec)
        background_child_list.append(static_node)
        background_child_list.append(transition_node)

    # append nodes
    for nidx in xrange(len(background_child_list)):
        child = background_child_list[nidx]
        background_node.appendChild(child)

    # debug
    if debug:
        background_node.toxml()

    return background_node

def gen_XML(xml_doc, xml_path):
    with open(xml_path, "w") as f:
        f.write(xml_doc.toprettyxml(indent="\t",\
                                    newl="\n",\
                                    encoding="utf-8")\
               )


def get_img_list(absolute_file_path):

    def get_all_filename(absolute_file_path, all_file_list=[]):
        filename_list = os.listdir(absolute_file_path)
        for idx in xrange(len(filename_list)):
            filename = filename_list[idx]
            filepath = os.path.join(absolute_file_path, filename)
            if os.path.isdir(filepath):
                get_all_filename(filepath, all_file_list)
            else:
                all_file_list.append(filepath)
        return all_file_list

    all_file_list = get_all_filename(absolute_file_path)

    def isImg(file_name):
        img_format_list = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        for f in img_format_list:
            if file_name[-len(f):].lower() == f:
                return True
        return False

    img_path_list = filter(lambda img_path: isImg(img_path), all_file_list)

    if debug:
        print(len(img_path_list))
        for i in img_path_list: print i

    return img_path_list


if __name__ == "__main__":
    print("abc")
    gen_starttime()
    gen_static("abc")
    img_list = get_img_list('/home/yuens/Pictures/head')
    background_node = gen_background(img_list, static_sec=10, transition_sec=1)
    gen_XML(background_node, "abc.xml")


