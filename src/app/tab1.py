from tkinter import *

from src.app.data import *
from PIL import Image
import os
import json


def get_emulator_image_path():
    path_file = open("paths.json", "r")
    paths = path_file.read()
    grubfile = json.loads(paths)['grub_file']
    path_file.close()
    grubfile = open(grubfile,"r")
    grubfiledata = grubfile.read()
    grubfile.close()
    GRUB_BACKGROUND=None
    if 'GRUB_BACKGROUND' in grubfiledata:
        GRUB_BACKGROUND = re.search('%s(.*)%s' % ('GRUB_BACKGROUND=', '\n'), grubfiledata).group(1)
    else:
        grubtheme = re.search('%s(.*)%s' % ('GRUB_THEME=', '\n'), grubfiledata).group(1)
        grubthemefile = open(grubtheme, "r")
        grubthemedata = grubthemefile.read()
        data['grubthemedata'] = grubthemedata
        grubthemefile.close()
        GRUB_BACKGROUND = re.search('%s(.*)%s' % ('desktop-image: "', '"'), grubthemedata).group(1)
        index = 0
        for i in range(len(grubtheme) - 1, -1, -1):
            if grubtheme[i] == '/':
                index = i+1
                break
        GRUB_BACKGROUND = grubtheme[0:index] + GRUB_BACKGROUND
        print(GRUB_BACKGROUND)

    data['emulator_image'] = GRUB_BACKGROUND


def create_emulator_image():
    get_emulator_image_path()
    base_dir = os.path.expanduser('~') + '/.grub-modifier'
    try:
        os.mkdir(base_dir)
    except FileExistsError:
        pass

    base_dir += '/temp'
    try:
        os.mkdir(base_dir)
    except FileExistsError:
        pass
    basewidth = data['root_width']
    tab1_background_image = Image.open(data['emulator_image'])
    wpercent = (basewidth / float(tab1_background_image.size[0]))
    hsize = int((float(tab1_background_image.size[1]) * float(wpercent)))
    tab1_background_image_resized = tab1_background_image.resize((basewidth, hsize), Image.ANTIALIAS)
    output_dir = base_dir + '/emulator_backgroud.' + tab1_background_image.format
    tab1_background_image_resized.save(output_dir)
    image = PhotoImage(file=output_dir)
    return image


def create_tab1():
    tab1 = Canvas(data['root'])
    tab1.config(bd=0, highlightthickness=0)
    update_data('tab1', tab1)
    tab1.config(width=data['root_width'], height=data['root_height'])
    tab1.place(
        x=0,
        y=data['navbar_height'] + data['tabbar_height'] + data['tabbarunderline_height'] + data['shadow_height'] + 5
    )
    tab1.update()

    ################################################# Emulator #####################################################

    # Create Background Image #######################
    background_image = create_emulator_image()
    background = Label(data['tab1'], image=background_image)
    background.place(x=0, y=0)
    background.update()
    data['background'] = background
    data['tab1_background_image'] = background_image
