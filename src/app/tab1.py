from tkinter import *

from src.app.data import *
from PIL import Image
import os


def get_emulator_image_path():
    data['emulator_image'] = '/boot/grub2/themes/openSUSE/background.png'


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

