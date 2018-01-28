from tkinter import *

from src.app.data import *


def create_tab4():
    tab4 = Canvas(data['root'])
    tab4.config(bg='#fff', bd=0, highlightthickness=0)
    tab4.config(
        width=data['root_width']
    )
    tab4.place(
        x=data['root_width'] * 6,
        y=data['navbar_height'] + data['tabbar_height'] + data['tabbarunderline_height'] + data['shadow_height'] + 10
    )
    update_data('tab4', tab4)
    Label(tab4, text='4').pack()
    tab4.update()
