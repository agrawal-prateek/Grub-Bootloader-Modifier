from tkinter import *

from src.app.data import *


def create_tab5():
    def change_disk_boot_order():
        pass

    def change_default_boot_section():
        pass

    ###################################################################################################################

    tab5 = Canvas(data['root'])
    tab5.config(bg='#fff', bd=0, highlightthickness=0)
    tab5.config(
        width=data['root_width'],
        height=data['root_height']
    )
    tab5.place(
        x=data['root_width'] * 8,
        y=data['navbar_height'] + data['tabbar_height'] + data['tabbarunderline_height'] + data['shadow_height'] + 10
    )
    update_data('tab5', tab5)
    tab5.update()

    ###################################################################################################################

    tab5_button1 = Button(data['tab5'], text='Edit Disk Boot Order', command=change_disk_boot_order)
    tab5_button1.place(
        x=(data['root_width'] - tab5_button1.winfo_reqwidth()) / 2, y=10
    )
    tab5_button1.update()
    update_data('tab5_button1', tab5_button1)

    ###################################################################################################################

    probe_foreign_os = BooleanVar()
    update_data('probe_foreign_os', probe_foreign_os)
    tab5_checkbox1 = Checkbutton(
        data['tab5'], variable=data['probe_foreign_os'],
        onvalue=True, offvalue=False
    )
    tab5_checkbox1.config(fg='#888', bd=0)
    tab5_checkbox1.place(x=data['root_width'] / 2 + 35,
                         y=data['tab5_button1'].winfo_y() + data['tab5_button1'].winfo_reqheight() + 20)
    tab5_checkbox1.select()
    tab5_checkbox1.update()
    update_data('tab5_checkbox1', tab5_checkbox1)

    ###################################################################################################################

    tab5_label1 = Label(tab5, text='Probe foreign OS')
    tab5_label1.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    tab5_label1.place(
        x=data['root_width'] / 2 + 45 + data['tab5_checkbox1'].winfo_reqwidth(),
        y=data['tab5_button1'].winfo_y() + data['tab5_button1'].winfo_reqheight() + 15
    )
    tab5_label1.update()
    update_data('tab5_label1', tab5_label1)

    ###################################################################################################################

    tab5_label2 = Label(tab5, text='Timeout in Seconds')
    tab5_label2.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    tab5_label2.place(
        x=35, y=data['tab5_checkbox1'].winfo_y() + data['tab5_checkbox1'].winfo_reqheight() + 10
    )
    tab5_label2.update()

    update_data('tab5_label2', tab5_label2)

    ###################################################################################################################

    bootloader_timeout = IntVar()
    update_data('bootloader_timeout', bootloader_timeout)
    tab5_entry1 = Entry(tab5)
    tab5_entry1.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=bootloader_timeout
    )
    tab5_entry1.place(
        x=35,
        y=data['tab5_label2'].winfo_y() + data['tab5_label2'].winfo_reqheight() + 10,
        width=data['root_width'] / 2 - 70
    )
    tab5_entry1.update()
    update_data('tab5_entry1', tab5_entry1)

    ###################################################################################################################

    hide_menu_on_boot = BooleanVar()
    update_data('hide_menu_on_boot', hide_menu_on_boot)
    tab5_checkbox2 = Checkbutton(
        data['tab5'], variable=data['hide_menu_on_boot'],
        onvalue=True, offvalue=False
    )
    tab5_checkbox2.config(fg='#888', bd=0)
    tab5_checkbox2.place(
        x=data['root_width'] / 2 + 35,
        y=data['tab5_entry1'].winfo_y() + data['tab5_entry1'].winfo_reqheight() + 10
    )
    tab5_checkbox2.select()
    tab5_checkbox2.update()
    update_data('tab5_checkbox2', tab5_checkbox2)

    ###################################################################################################################

    tab5_label3 = Label(tab5, text='Hide menu on Boot')
    tab5_label3.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    tab5_label3.place(
        x=data['root_width'] / 2 + 45 + data['tab5_checkbox2'].winfo_reqwidth(),
        y=data['tab5_entry1'].winfo_y() + data['tab5_entry1'].winfo_reqheight() + 5
    )
    tab5_label3.update()
    update_data('tab5_label3', tab5_label3)

    ###################################################################################################################

    tab5_label4 = Label(tab5, text='Default Boot Section')
    update_data('tab5_label4', tab5_label4)
    tab5_label4.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    tab5_label4.place(
        x=int(data['root_width'] - data['tab5_label4'].winfo_reqwidth()) / 2,
        y=data['tab5_checkbox2'].winfo_y() + data['tab5_checkbox2'].winfo_reqheight() + 20
    )
    tab5_label4.update()

    ###################################################################################################################

    default_boot_section = StringVar()
    default_boot_section.set("opensuse leap 42.3")
    update_data('default_boot_section', default_boot_section)

    tab5_dropdown1 = OptionMenu(
        tab5, default_boot_section, "GRUB2 for EFI", "GRUB2", "Not Managed",
        command=change_default_boot_section
    )
    update_data('tab5_dropdown1', tab5_dropdown1)
    tab5_dropdown1.place(
        x=int(data['root_width'] - data['tab5_dropdown1'].winfo_reqwidth()) / 2,
        y=data['tab5_label4'].winfo_y() + data['tab5_label4'].winfo_reqheight() + 10
    )
    tab5_dropdown1.update()

    ###################################################################################################################

    tab5_frame1 = Frame(tab5)
    tab5_frame1.config(
        bd=3, highlightthickness=2, bg='#fff', width=data['root_width'] - 70, height=200
    )
    tab5_frame1.place(
        x=35,
        y=data['tab5_dropdown1'].winfo_y() + data['tab5_dropdown1'].winfo_reqheight() + 20
    )
    tab5_frame1.update()
    update_data('tab5_frame1', tab5_frame1)

    ###################################################################################################################

    tab5_label5 = Label(data['tab5_frame1'], text='Protect Boot Loader with password')
    update_data('tab5_label5', tab5_label5)
    tab5_label5.config(
        fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0
    )
    tab5_label5.place(
        x=int(data['root_width'] - data['tab5_label5'].winfo_reqwidth()) / 2,
        y=10
    )
    tab5_label5.update()

    ###################################################################################################################
    tab5_label6 = Label(data['tab5_frame1'], text='Password for GRUB2')
    update_data('tab5_label6', tab5_label6)
    tab5_label6.config(
        fg='#888', bg='#fff', font='"Times" 12 bold', bd=0
    )
    tab5_label6.place(
        x=35,
        y=data['tab5_label5'].winfo_y() + data['tab5_label5'].winfo_reqheight() + 20
    )
    tab5_label6.update()

    ###################################################################################################################

    tab5_label7 = Label(data['tab5_frame1'], text='Retype Password')
    update_data('tab5_label7', tab5_label7)
    tab5_label7.config(
        fg='#888', bg='#fff', font='"Times" 12 bold', bd=0
    )
    tab5_label7.place(
        x=data['tab5_frame1'].winfo_reqwidth() / 2 + 35,
        y=data['tab5_label5'].winfo_y() + data['tab5_label5'].winfo_reqheight() + 20
    )
    tab5_label7.update()

    ###################################################################################################################

    grub2_password = StringVar()
    update_data('grub2_password', grub2_password)
    tab5_entry2 = Entry(data['tab5_frame1'])
    update_data('tab5_entry2', tab5_entry2)

    tab5_entry2.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=grub2_password
    )
    tab5_entry2.place(
        x=35,
        y=data['tab5_label6'].winfo_y() + data['tab5_label6'].winfo_reqheight() + 10,
        width=data['tab5_frame1'].winfo_reqwidth() / 2 - 70
    )
    tab5_entry2.update()

    ###################################################################################################################

    grub2_password_retype = StringVar()
    update_data('grub2_password_retype', grub2_password_retype)
    tab5_entry3 = Entry(data['tab5_frame1'])
    update_data('tab5_entry3', tab5_entry3)

    tab5_entry3.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=grub2_password_retype
    )
    tab5_entry3.place(
        x=data['tab5_frame1'].winfo_reqwidth() / 2 + 35,
        y=data['tab5_label7'].winfo_y() + data['tab5_label7'].winfo_reqheight() + 10,
        width=data['tab5_frame1'].winfo_reqwidth() / 2 - 70
    )
    tab5_entry3.update()

    ###################################################################################################################
