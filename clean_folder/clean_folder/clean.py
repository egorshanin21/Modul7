#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import shutil
from pathlib import Path
from os.path import basename, splitext

staff_dirs = ['archives', 'video', 'audio', 'documents', 'images', 'other']
images = ['.jpg', '.png', '.jpeg', '.svg']
audio = ['.mp3', '.ogg', '.wav', '.amr']
video = ['.avi', '.mp4', '.mov', '.mkv']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
archives = ['.zip', '.gz', '.tar']


def parse(current_path, main_path):
    current_path_list = os.listdir(current_path)
    # get all files
    fullpaths = map(lambda name: os.path.join(current_path, name), current_path_list)

    for el in fullpaths:
        filename, file_extension = os.path.splitext(el)
        name, ext = splitext(basename(filename))

        if os.path.isdir(el) and not name in staff_dirs:

            if not len(os.listdir(el)):
                os.rmdir(el)
            else:
                parse(el, main_path)
        elif not el.split('/')[-1] in staff_dirs:
            os.makedirs(f'{main_path}/archives', exist_ok=True)
            os.makedirs(f'{main_path}/video', exist_ok=True)
            os.makedirs(f'{main_path}/audio', exist_ok=True)
            os.makedirs(f'{main_path}/documents', exist_ok=True)
            os.makedirs(f'{main_path}/images', exist_ok=True)
            os.makedirs(f'{main_path}/other', exist_ok=True)

            if file_extension in images:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/images')
                os.rename(file, file.replace(name, new_filename))
            elif file_extension in audio:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/audio')
                os.rename(file, file.replace(name, new_filename))
            elif file_extension in video:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/video')
                os.rename(file, file.replace(name, new_filename))
            elif file_extension in documents:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/documents')
                os.rename(file, file.replace(name, new_filename))
            elif file_extension in archives:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/archives')
                os.makedirs(f'{main_path}/archives/{new_filename}', exist_ok=True)
                shutil.unpack_archive(file, f'{main_path}/archives/{new_filename}')
            else:
                new_filename = normalize(name)
                file = shutil.move(el, main_path + '/other')
                os.rename(file, file.replace(name, new_filename))


def normalize(name):
    new_name = tranc(name)

    return new_name


def tranc(name):
    # name[name.rfind('/')+1, name.rfind('.')]
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n",
    "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i",
    "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    new_name = ""

    for i in name:

        if TRANS.get(ord(i)):
            new_name = new_name + TRANS[ord(i)]
        elif i.isalpha() or i.isdigit():
            new_name += i
        else:
            new_name += '_'

    return new_name

def run():
    try:
        main_path = sys.argv[1]
    except Exception as e:
        main_path = os.getcwdb().decode()
    print(f'current dir: {main_path}')
    current_path = main_path

    parse(current_path, main_path)

run()