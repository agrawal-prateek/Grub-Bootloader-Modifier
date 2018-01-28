#!/usr/bin/env python3

from tkinter import *
import sys
import json

sys.path.append(json.loads(open('paths.json', 'r').read())['root_path'])

from src.app.data import *
from src.app.tab1 import create_tab1, create_emulator_image, get_emulator_image_path
from src.app.tab2 import create_tab2
from src.app.tab3 import create_tab3
from src.app.tab4 import create_tab4
from src.app.tab5 import create_tab5


def update_tabs_width():
    if data['active_tab'] == 1:
        data['tab1'].config(width=data['root_width'])
    elif data['active_tab'] == 2:
        data['tab2'].config(width=data['root_width'])
    elif data['active_tab'] == 3:
        data['tab3'].config(width=data['root_width'])
    elif data['active_tab'] == 4:
        data['tab4'].config(width=data['root_width'])
    elif data['active_tab'] == 5:
        data['tab5'].config(width=data['root_width'])


def update_tab1_elements():
    try:
        pass
    except KeyError:
        pass


def update_tab2_elements():
    try:
        data['bootloader_label'].place(x=(data['root_width'] - data['bootloader_label'].winfo_reqwidth()) / 2)
    except KeyError:
        pass
    try:
        data['select_bootloader'].place(x=(data['root_width'] - data['select_bootloader'].winfo_reqwidth()) / 2)
    except KeyError:
        pass
    try:
        data['tab2_responsive_frame1'].config(width=data['root_width'] - 70)
    except KeyError:
        pass
    try:
        data['tab2_frame1_entry1'].place(width=data['root_width'] - 140)
    except KeyError:
        pass


def update_tab3_elements():
    # Start tab3 updation
    data['kernel_parameters_entry'].place(width=data['root_width'] - 70)
    data['graphical_console_frame'].config(width=data['root_width'] - 70)
    data['graphical_console_theme_entry'].place(width=data['graphical_console_frame'].winfo_reqwidth() - 210)
    data['console_theme_browse_button'].place(x=45 + data['graphical_console_theme_entry'].winfo_width())
    data['serial_console_frame'].config(width=data['root_width'] - 70)
    data['serial_console_theme_entry'].place(width=data['serial_console_frame'].winfo_reqwidth() - 70)


def update_tab4_elements():
    pass


def update_tab5_elements():
    try:
        data['tab5_button1'].place(
            x=(data['root_width'] - data['tab5_button1'].winfo_reqwidth()) / 2
        )
    except KeyError:
        pass
    try:
        data['tab5_checkbox1'].place(x=data['root_width'] / 2 + 35)
    except KeyError:
        pass
    try:
        data['tab5_label1'].place(x=data['root_width'] / 2 + 45 + data['tab5_checkbox1'].winfo_reqwidth())
    except KeyError:
        pass
    try:
        data['tab5_checkbox2'].place(x=data['root_width'] / 2 + 35)
    except KeyError:
        pass
    try:
        data['tab5_entry1'].place(width=data['root_width'] / 2 - 70)
    except KeyError:
        pass
    try:
        data['tab5_label3'].place(x=data['root_width'] / 2 + 45 + data['tab5_checkbox2'].winfo_reqwidth())
    except KeyError:
        pass
    try:
        data['tab5_label4'].place(x=int(data['root_width'] - data['tab5_label4'].winfo_reqwidth()) / 2)
    except KeyError:
        pass
    try:
        data['tab5_dropdown1'].place(x=int(data['root_width'] - data['tab5_dropdown1'].winfo_reqwidth()) / 2)
    except KeyError:
        pass
    try:
        data['tab5_frame1'].config(width=data['root_width'] - 70)
    except KeyError:
        pass
    try:
        data['tab5_label5'].place(x=int(data['root_width'] - data['tab5_label5'].winfo_reqwidth()) / 2)
    except KeyError:
        pass
    try:
        data['tab5_label7'].place(x=data['tab5_frame1'].winfo_reqwidth() / 2 + 35)
    except KeyError:
        pass
    try:
        data['tab5_entry2'].place(width=data['tab5_frame1'].winfo_reqwidth() / 2 - 70)
    except KeyError:
        pass

    try:
        data['tab5_entry3'].place(
            x=data['tab5_frame1'].winfo_reqwidth() / 2 + 35,
            width=data['tab5_frame1'].winfo_reqwidth() / 2 - 70
        )
    except KeyError:
        pass


def change_root_width(event):
    root.update()
    data['root_width'] = root.winfo_width()
    update_tabs_width()
    update_tab1_elements()
    update_tab2_elements()
    update_tab3_elements()
    update_tab4_elements()
    update_tab5_elements()



def style_root_window():
    global root
    root.config(bg='#fff', bd=0)


def style_menu_bar(menu_bar=None):
    menu_bar.config(bd=0, bg='#0019a8', fg='#fff')


def style_nav_bar(nav_bar=None):
    nav_bar.config(bd=0, bg='#2540db', height=25)


def style_tab_bar(tab_bar=None):
    tab_bar.config(bg='#2540db', height=50, bd=0)


def style_tabbar_emulator(tabbar_emulator=None):
    tabbar_emulator.config(fg='#fff', font='"Roboto Mono" 12 bold', bd=0,
                           bg='#2540db', padx=35, pady=10, cursor='hand2')
    tabbar_emulator.grid(row=1, column=1)


def style_tabbar_bootloader(tabbar_bootloader=None):
    tabbar_bootloader.config(fg='#fff', font='"Roboto Mono" 12 bold', bd=0,
                             bg='#2540db', padx=35, pady=10, cursor='hand2')
    tabbar_bootloader.grid(row=1, column=2)


def style_tabbar_kernel_parameters(tabbar_kernel_parameters=None):
    tabbar_kernel_parameters.config(fg='#fff', font='"Roboto Mono" 12 bold', bd=0,
                                    bg='#2540db', padx=35, pady=10, cursor='hand2')
    tabbar_kernel_parameters.grid(row=1, column=3)


def style_tabbar_appearance_settings(tabbar_appearance_settings=None):
    tabbar_appearance_settings.config(fg='#fff', font='"Roboto Mono" 12 bold',
                                      bd=0, bg='#2540db', padx=35, pady=10, cursor='hand2')
    tabbar_appearance_settings.grid(row=1, column=4)


def style_tabbar_bootloader_settings(tabbar_bootloader_settings=None):
    tabbar_bootloader_settings.grid(row=1, column=5)
    tabbar_bootloader_settings.config(fg='#fff', font='"Roboto Mono" 12 bold',
                                      bd=0, bg='#2540db', padx=35, pady=10, cursor='hand2')


def style_tab_underline(tab_underline=None):
    tab_underline.config(bg='#2540db', bd=0, height=5)


def view_full_screen(event=None):
    global root
    root.attributes("-fullscreen", True)
    change_root_width(event=None)


def exit_full_screen(event=None):
    global root
    root.attributes("-fullscreen", False)


def animate_underline(activetab, opentab):
    if activetab < opentab:
        if opentab == 2:
            distance = data['bootloader'].winfo_x() - data['underline'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() + 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() < data['bootloader'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() + 2)
                # time.sleep(0.00001)
        elif opentab == 3:
            distance = data['kernelparameters'].winfo_x() - data['underline'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() + 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() < data['kernelparameters'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() + 2)
                # time.sleep(0.00001)
        elif opentab == 4:
            distance = data['appearancesettings'].winfo_x() - data['underline'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() + 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() < data['appearancesettings'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() + 2)
                # time.sleep(0.00001)
        elif opentab == 5:
            distance = data['bootloadersettings'].winfo_x() - data['underline'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() + 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() < data['bootloadersettings'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() + 2)
                # time.sleep(0.00001)

    elif activetab > opentab:
        if opentab == 1:
            distance = data['underline'].winfo_x() - data['emulator'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() - 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() > data['emulator'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() - 2)
                # time.sleep(0.00001)
        elif opentab == 2:
            distance = data['underline'].winfo_x() - data['bootloader'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() - 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() > data['bootloader'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() - 2)
                # time.sleep(0.00001)
        elif opentab == 3:
            distance = data['underline'].winfo_x() - data['kernelparameters'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() - 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() > data['kernelparameters'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() - 2)
                # time.sleep(0.00001)
        elif opentab == 4:
            distance = data['underline'].winfo_x() - data['appearancesettings'].winfo_x()
            for i in range(0, distance, 2):
                data['underline'].place(x=data['underline'].winfo_x() - 2)
                data['underline'].update()
                if data['underline'].winfo_reqwidth() > data['appearancesettings'].winfo_reqwidth():
                    data['underline'].config(width=data['underline'].winfo_reqwidth() - 2)
                # time.sleep(0.00001)


def open_tab1(event=None):
    active_tab = data['active_tab']
    data['active_tab'] = 0
    animate_underline(activetab=active_tab, opentab=1)

    if active_tab == 1:
        data['active_tab'] = 1

    elif active_tab == 2:
        data['tab1'].place(x=- data['root_width'])
        data['tab1'].update()
        current_tab_x = data['tab1'].winfo_x()
        new_tab_x = data['tab2'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab1'].place(x=current_tab_x)
            data['tab2'].place(x=new_tab_x)
            data['tab2'].update()
            data['tab2'].update()
        data['active_tab'] = 1

    elif active_tab == 3:
        data['tab1'].place(x=- data['root_width'])
        data['tab1'].update()
        current_tab_x = data['tab3'].winfo_x()
        new_tab_x = data['tab1'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab3'].place(x=current_tab_x)
            data['tab1'].place(x=new_tab_x)
            data['tab3'].update()
            data['tab1'].update()
        data['active_tab'] = 1

    elif active_tab == 4:
        data['tab1'].place(x=- data['root_width'])
        data['tab1'].update()
        current_tab_x = data['tab4'].winfo_x()
        new_tab_x = data['tab1'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab4'].place(x=current_tab_x)
            data['tab1'].place(x=new_tab_x)
            data['tab4'].update()
            data['tab1'].update()
        data['active_tab'] = 1

    elif active_tab == 5:
        data['tab1'].place(x=- data['root_width'])
        data['tab1'].update()
        current_tab_x = data['tab5'].winfo_x()
        new_tab_x = data['tab1'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab5'].place(x=current_tab_x)
            data['tab1'].place(x=new_tab_x)
            data['tab5'].update()
            data['tab1'].update()
        data['active_tab'] = 1


def open_tab2(event=None):
    active_tab = data['active_tab']
    data['active_tab'] = 0
    animate_underline(activetab=active_tab, opentab=2)

    if active_tab == 1:
        data['tab2'].place(x=data['root_width'])
        data['tab2'].update()
        current_tab_x = data['tab1'].winfo_x()
        new_tab_x = data['tab2'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab1'].place(x=current_tab_x)
            data['tab2'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab2'].update()
        data['active_tab'] = 2

    elif active_tab == 2:
        data['active_tab'] = 2

    elif active_tab == 3:
        data['tab2'].place(x=data['tab3'].winfo_x() - data['root_width'])
        data['tab2'].update()
        current_tab_x = data['tab3'].winfo_x()
        new_tab_x = data['tab2'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab3'].place(x=current_tab_x)
            data['tab2'].place(x=new_tab_x)
            data['tab3'].update()
            data['tab2'].update()
        data['active_tab'] = 2

    elif active_tab == 4:
        data['tab2'].place(x=data['tab4'].winfo_x() - data['root_width'])
        data['tab2'].update()
        current_tab_x = data['tab4'].winfo_x()
        new_tab_x = data['tab2'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab4'].place(x=current_tab_x)
            data['tab2'].place(x=new_tab_x)
            data['tab4'].update()
            data['tab2'].update()
        data['active_tab'] = 2

    elif active_tab == 5:
        data['tab2'].place(x=- data['root_width'])
        data['tab2'].update()
        current_tab_x = data['tab5'].winfo_x()
        new_tab_x = data['tab2'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab5'].place(x=current_tab_x)
            data['tab2'].place(x=new_tab_x)
            data['tab4'].update()
            data['tab2'].update()
        data['active_tab'] = 2


def open_tab3(event=None):
    active_tab = data['active_tab']
    data['active_tab'] = 0
    animate_underline(activetab=active_tab, opentab=3)

    if active_tab == 1:
        data['tab3'].place(x=data['root_width'])
        data['tab3'].update()
        current_tab_x = data['tab1'].winfo_x()
        new_tab_x = data['tab3'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab1'].place(x=current_tab_x)
            data['tab3'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab3'].update()
        data['active_tab'] = 3

    elif active_tab == 2:
        data['tab3'].place(x=data['root_width'])
        data['tab3'].update()
        current_tab_x = data['tab2'].winfo_x()
        new_tab_x = data['tab3'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab2'].place(x=current_tab_x)
            data['tab3'].place(x=new_tab_x)
            data['tab2'].update()
            data['tab3'].update()
        data['active_tab'] = 3

    elif active_tab == 3:
        data['active_tab'] = 3

    elif active_tab == 4:
        data['tab3'].place(x=- data['root_width'])
        data['tab3'].update()
        current_tab_x = data['tab4'].winfo_x()
        new_tab_x = data['tab3'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab4'].place(x=current_tab_x)
            data['tab3'].place(x=new_tab_x)
            data['tab4'].update()
            data['tab3'].update()
        data['active_tab'] = 3

    elif active_tab == 5:
        data['tab3'].place(x=- data['root_width'])
        data['tab3'].update()
        current_tab_x = data['tab5'].winfo_x()
        new_tab_x = data['tab3'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab5'].place(x=current_tab_x)
            data['tab3'].place(x=new_tab_x)
            data['tab5'].update()
            data['tab3'].update()
        data['active_tab'] = 3


def open_tab4(event=None):
    active_tab = data['active_tab']
    data['active_tab'] = 0
    animate_underline(activetab=active_tab, opentab=4)

    if active_tab == 1:
        data['tab4'].place(x=data['root_width'])
        data['tab4'].update()
        current_tab_x = data['tab1'].winfo_x()
        new_tab_x = data['tab4'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab1'].place(x=current_tab_x)
            data['tab4'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab4'].update()

        data['active_tab'] = 4

    elif active_tab == 2:
        data['tab4'].place(x=data['root_width'])
        data['tab4'].update()
        current_tab_x = data['tab2'].winfo_x()
        new_tab_x = data['tab4'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab2'].place(x=current_tab_x)
            data['tab4'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab4'].update()
        data['active_tab'] = 4

    elif active_tab == 3:
        data['tab4'].place(x=data['root_width'])
        data['tab4'].update()
        current_tab_x = data['tab3'].winfo_x()
        new_tab_x = data['tab4'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab3'].place(x=current_tab_x)
            data['tab4'].place(x=new_tab_x)
            data['tab3'].update()
            data['tab4'].update()
        data['active_tab'] = 4

    elif active_tab == 4:
        data['active_tab'] = 4

    elif active_tab == 5:
        data['tab4'].place(x=- data['root_width'])
        data['tab4'].update()
        current_tab_x = data['tab5'].winfo_x()
        new_tab_x = data['tab4'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x += 2
            new_tab_x += 2
            data['tab5'].place(x=current_tab_x)
            data['tab4'].place(x=new_tab_x)
            data['tab5'].update()
            data['tab4'].update()
        data['active_tab'] = 4


def open_tab5(event=None):
    active_tab = data['active_tab']
    data['active_tab'] = 0
    animate_underline(activetab=active_tab, opentab=5)

    if active_tab == 1:
        data['tab5'].place(x=data['root_width'])
        data['tab5'].update()
        current_tab_x = data['tab1'].winfo_x()
        new_tab_x = data['tab5'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab1'].place(x=current_tab_x)
            data['tab5'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab5'].update()
        data['active_tab'] = 5

    elif active_tab == 2:
        data['tab5'].place(x=data['root_width'])
        data['tab5'].update()
        current_tab_x = data['tab2'].winfo_x()
        new_tab_x = data['tab5'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab2'].place(x=current_tab_x)
            data['tab5'].place(x=new_tab_x)
            data['tab1'].update()
            data['tab5'].update()
        data['active_tab'] = 5

    elif active_tab == 3:
        data['tab5'].place(x=data['root_width'])
        data['tab5'].update()
        current_tab_x = data['tab3'].winfo_x()
        new_tab_x = data['tab5'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab3'].place(x=current_tab_x)
            data['tab5'].place(x=new_tab_x)
            data['tab3'].update()
            data['tab5'].update()
        data['active_tab'] = 5

    elif active_tab == 4:
        data['tab5'].place(x=data['root_width'])
        data['tab5'].update()
        current_tab_x = data['tab4'].winfo_x()
        new_tab_x = data['tab5'].winfo_x()
        for i in range(0, data['root_width'], 2):
            current_tab_x -= 2
            new_tab_x -= 2
            data['tab4'].place(x=current_tab_x)
            data['tab5'].place(x=new_tab_x)
            data['tab4'].update()
            data['tab5'].update()
        data['active_tab'] = 5

    elif active_tab == 5:
        data['active_tab'] = 5


def root_config():
    global root
    root.title('Grub Modifier')
    root.bind("<F12>", view_full_screen)
    root.bind("<Escape>", exit)
    style_root_window()


def create_menubar():
    global root
    menubar = Menu(root)
    style_menu_bar(menu_bar=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=exit)
    filemenu.add_command(label="Open", command=exit)
    filemenu.add_command(label="Save", command=exit)
    filemenu.add_command(label="Save as...", command=exit)
    filemenu.add_command(label="Close", command=exit)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=exit)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=exit)
    editmenu.add_command(label="Copy", command=exit)
    editmenu.add_command(label="Paste", command=exit)
    editmenu.add_command(label="Delete", command=exit)
    editmenu.add_command(label="Select All", command=exit)
    menubar.add_cascade(label="Edit", menu=editmenu)

    viewmenu = Menu(menubar, tearoff=0, bd=0, bg='#fff')
    viewmenu.add_separator()
    viewmenu.add_command(label="Full Screen    F12", command=view_full_screen)
    menubar.add_cascade(label="View", menu=viewmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=exit)
    helpmenu.add_command(label="About...", command=exit)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)


def create_nav():
    global root
    navbar = Frame(root)
    style_nav_bar(nav_bar=navbar)
    navbar.pack(fill=BOTH)
    update_data('navbar_height', navbar.winfo_reqheight())


def create_blank_space():
    global root
    blankspace = Frame(root)
    blankspace.config(bg='#2540db', bd=0, highlightthickness=0, height=15)
    blankspace.pack(fill=BOTH)


def create_tab_bar():
    tabbar = Frame(root)
    style_tab_bar(tab_bar=tabbar)

    emulator = Label(tabbar, text='EMULATOR')
    style_tabbar_emulator(tabbar_emulator=emulator)
    emulator.bind('<Button-1>', open_tab1)

    bootloader = Label(tabbar, text='BOOTLOADER')
    style_tabbar_bootloader(tabbar_bootloader=bootloader)
    bootloader.bind('<Button-1>', open_tab2)

    kernelparameters = Label(tabbar, text='KERNEL PARAMETERS')
    style_tabbar_kernel_parameters(tabbar_kernel_parameters=kernelparameters)
    kernelparameters.bind('<Button-1>', open_tab3)

    appearancesettings = Label(tabbar, text='APPEARANCE SETTINGS')
    style_tabbar_appearance_settings(tabbar_appearance_settings=appearancesettings)
    appearancesettings.bind('<Button-1>', open_tab4)

    bootloadersettings = Label(tabbar, text='BOOTLOADER SETTINGS')
    style_tabbar_bootloader_settings(tabbar_bootloader_settings=bootloadersettings)
    bootloadersettings.bind('<Button-1>', open_tab5)

    tabbar.pack(fill=BOTH)

    tabunderline = Frame(root)
    style_tab_underline(tab_underline=tabunderline)
    tabunderline.pack(fill=BOTH)

    underline = Canvas(tabunderline, height=5, width=emulator.winfo_reqwidth(),
                       bg='#fff', bd=0, highlightthickness=0)
    underline.place(x=emulator.winfo_x(), y=0)

    update_data(
        'tabbar_height', tabbar.winfo_reqheight(),
        'tabbarunderline_height', tabunderline.winfo_reqheight(),
        'tabbar', tabbar,
        'tabbarunderline', tabunderline,
        'underline', underline,
        'emulator', emulator,
        'bootloader', bootloader,
        'kernelparameters', kernelparameters,
        'appearancesettings', appearancesettings,
        'bootloadersettings', bootloadersettings
    )


def create_shadow():
    global root
    shadow_frame = Frame(root)
    shadow_frame.config(bg='#aaa', bd=0, highlightthickness=0, height=11)
    shadow_frame.pack(fill=BOTH)
    shadow = Canvas(shadow_frame, width=data['root_width'], height=10, bd=0, highlightthickness=0)
    shadow.config(bg='#fff')
    shadow.pack(fill=BOTH)

    shadow.create_line(0, 0, data['screen_width'], 0, tag='layer0', fill='#bcbcbc')
    shadow.create_line(0, 1, data['screen_width'], 1, tag='layer1', fill='#c9c8c8')
    shadow.create_line(0, 2, data['screen_width'], 2, tag='layer2', fill='#d3d3d3')
    shadow.create_line(0, 3, data['screen_width'], 3, tag='layer3', fill='#dfdfdf')
    shadow.create_line(0, 4, data['screen_width'], 4, tag='layer4', fill='#e7e7e7')
    shadow.create_line(0, 5, data['screen_width'], 5, tag='layer5', fill='#f5f5f5')
    shadow.create_line(0, 6, data['screen_width'], 6, tag='layer6', fill='#f9f9f9')
    shadow.create_line(0, 7, data['screen_width'], 7, tag='layer7', fill='#fcfcfc')
    shadow.create_line(0, 8, data['screen_width'], 8, tag='layer8', fill='#fefefe')

    update_data('shadow_height', 10)


if __name__ == '__main__':
    root = Tk()
    update_data(
        'root', root,
        'screen_width', root.winfo_screenwidth(),
        'screen_height', root.winfo_screenheight()
    )
    root_config()
    create_menubar()
    create_nav()
    create_blank_space()
    create_tab_bar()
    root.update()
    update_data(
        'root_width', root.winfo_width(),
        'root_height', int(data['screen_height'] * 0.8)
    )
    root.geometry('{}x{}+{}+{}'.format(data['root_width'], data['root_height'], int(data['root_width'] * 0.1),
                                       int(data['root_height'] * 0.1)))

    create_shadow()
    create_tab1()
    create_tab2()
    create_tab3()
    create_tab4()
    create_tab5()
    root.bind('<Configure>', change_root_width)
    root.mainloop()
