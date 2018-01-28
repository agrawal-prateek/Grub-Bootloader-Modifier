from tkinter import *

from src.app.data import *


def create_tab2():
    def update_tab2(option=None):
        print(option)
        if data['bootloader_value'].get() == 'GRUB2':
            tab2_label1 = Label(data['tab2'], text='Boot Loader Location')
            tab2_label1.config(
                fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
            )
            tab2_label1.place(x=35, y=30 + data['select_bootloader'].winfo_y())
            tab2_label1.update()
            tab2_frame1 = Frame(data['tab2'])
            tab2_frame1.config(
                bd=3, highlightthickness=2, bg='#fff', width=data['root_width'] - 70, height=165
            )
            tab2_frame1.place(
                x=35, y=10 + tab2_label1.winfo_y() + tab2_label1.winfo_reqheight()
            )
            tab2_frame1.update()
            update_data('tab2_responsive_frame1', tab2_frame1)

            boot_from_root_partition = BooleanVar()
            boot_from_master_boot_record = BooleanVar()
            custom_boot_partition = BooleanVar()

            update_data(
                'boot_from_root_partition', boot_from_root_partition,
                'boot_from_master_boot_record', boot_from_master_boot_record,
                'custom_boot_partition', custom_boot_partition,
            )

            tab2_frame1_checkbox1 = Checkbutton(
                data['tab2_responsive_frame1'], variable=data['boot_from_root_partition'],
                onvalue=True, offvalue=False
            )
            tab2_frame1_checkbox2 = Checkbutton(
                data['tab2_responsive_frame1'], variable=data['boot_from_master_boot_record'],
                onvalue=True, offvalue=False
            )
            tab2_frame1_checkbox3 = Checkbutton(
                data['tab2_responsive_frame1'], variable=data['custom_boot_partition'],
                onvalue=True, offvalue=False
            )
            tab2_frame1_checkbox1.config(fg='#888', bd=0)
            tab2_frame1_checkbox2.config(fg='#888', bd=0)
            tab2_frame1_checkbox3.config(fg='#888', bd=0)

            tab2_frame1_checkbox1.place(x=35, y=10, height=25, width=25)
            tab2_frame1_checkbox2.place(x=35, y=45, height=25, width=25)
            tab2_frame1_checkbox3.place(x=35, y=80, height=25, width=25)

            tab2_frame1_checkbox1.update()
            tab2_frame1_checkbox2.update()
            tab2_frame1_checkbox3.update()

            tab2_frame1_checkbox1_label = Label(data['tab2_responsive_frame1'], text='Boot from Root Partition')
            tab2_frame1_checkbox2_label = Label(data['tab2_responsive_frame1'], text='Boot from Master Boot Record')
            tab2_frame1_checkbox3_label = Label(data['tab2_responsive_frame1'], text='Custom Boot Partition')

            tab2_frame1_checkbox1_label.config(fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0)
            tab2_frame1_checkbox2_label.config(fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0)
            tab2_frame1_checkbox3_label.config(fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0)

            tab2_frame1_checkbox1_label.place(x=70, y=10)
            tab2_frame1_checkbox2_label.place(x=70, y=45)
            tab2_frame1_checkbox3_label.place(x=70, y=80)

            custom_boot_partition_location = StringVar()
            update_data('custom_boot_partition_location', custom_boot_partition_location)

            tab2_frame1_entry1 = Entry(data['tab2_responsive_frame1'])
            tab2_frame1_entry1.config(
                fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
                highlightcolor='#2540db', textvariable=data['custom_boot_partition_location']
            )
            tab2_frame1_entry1.place(x=35, y=115, height=30, width=data['root_width'] - 140)
            tab2_frame1_entry1.update()
            update_data('tab2_frame1_entry1', tab2_frame1_entry1)

            set_active_flag_in_partition_table_for_boot_partition = BooleanVar()
            write_generic_boot_code_to_mbr = BooleanVar()
            enable_trusted_boot_support = BooleanVar()

            update_data(
                'set_active_flag_in_partition_table_for_boot_partition',
                set_active_flag_in_partition_table_for_boot_partition,
                'write_generic_boot_code_to_mbr', write_generic_boot_code_to_mbr,
                'enable_trusted_boot_support', enable_trusted_boot_support
            )

            tab2_checkbox1 = Checkbutton(
                data['tab2'], variable=data['set_active_flag_in_partition_table_for_boot_partition'],
                onvalue=True, offvalue=False
            )
            tab2_checkbox2 = Checkbutton(
                data['tab2'], variable=data['write_generic_boot_code_to_mbr'],
                onvalue=True, offvalue=False
            )
            tab2_checkbox3 = Checkbutton(
                data['tab2'], variable=data['enable_trusted_boot_support'],
                onvalue=True, offvalue=False
            )

            tab2_checkbox1.config(fg='#888', bd=0)
            tab2_checkbox2.config(fg='#888', bd=0)
            tab2_checkbox3.config(fg='#888', bd=0)

            tab2_checkbox1.place(x=35, y=185 + tab2_frame1.winfo_y(), height=25, width=25)
            tab2_checkbox2.place(x=35, y=220 + tab2_frame1.winfo_y(), height=25, width=25)
            tab2_checkbox3.place(x=35, y=255 + tab2_frame1.winfo_y(), height=25, width=25)

            tab2_checkbox1.update()
            tab2_checkbox2.update()
            tab2_checkbox3.update()

            tab2_label2 = Label(data['tab2'], text='Set active Flag in Partition Table for Boot Partition')
            tab2_label3 = Label(data['tab2'], text='Write generic Boot Code to MBR')
            tab2_label4 = Label(data['tab2'], text='Enable Trusted Boot Support')

            tab2_label2.config(fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0)
            tab2_label3.config(fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0)
            tab2_label4.config(fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0)

            tab2_label2.place(x=70, y=185 + tab2_frame1.winfo_y())
            tab2_label3.place(x=70, y=220 + tab2_frame1.winfo_y())
            tab2_label4.place(x=70, y=255 + tab2_frame1.winfo_y())

            tab2_label2.update()
            tab2_label3.update()
            tab2_label4.update()
        elif data['bootloader_value'].get() == 'GRUB2 for EFI' and 'enable_secure_boot' not in data.keys():
            data['enable_secure_boot'] = BooleanVar()
            checkbox = Checkbutton(
                data['tab2'], variable=data['enable_secure_boot'],
                onvalue=True, offvalue=False
            )
            checkbox.config(fg='#888', bd=0)
            checkbox.place(x=35, y=30 + data['select_bootloader'].winfo_y(), height=25, width=25)
            checkbox.select()
            checkbox.update()
            update_data('enable secure boot', data['enable_secure_boot'])
            label = Label(data['tab2'], text='Enable Secure boot options')
            label.config(
                fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
            )
            label.place(x=10 + checkbox.winfo_x() + checkbox.winfo_reqwidth(),
                        y=30 + data['select_bootloader'].winfo_y())
            label.update()
        else:
            info = Tk()
            info.resizable(0, 0)
            info.geometry('{}x{}+{}+{}'.format(
                str(int(data['root_width'] / 2)),
                str(int(data['root_height'] / 2)),
                str(int(data['root'].winfo_x() + int(data['root_width'] / 4))),
                str(int(data['root'].winfo_y() + int(data['root_height'] / 4)))
            ))
            info.config(bg='#aaa', bd=0, highlightthickness=0)
            info.wm_attributes('-type', 'splash')
            info.update()
            info_frame = Frame(info)
            info_frame.pack()
            label_info = Label(
                info_frame,
                text='If you do not install any boot loader,\n the system might not start.\n\n\nProceed?'
            )
            label_info.config(
                fg='#fff', bg='#aaa', font='"Roboto" 14 bold', bd=0, pady=30
            )
            label_info.grid(row=1, column=1)
            button1 = Button(info, text='OK', command=exit)
            button2 = Button(info, text='Cancel', command=info.destroy)

            button1.place(
                x=int(data['root_width'] / 2) - button1.winfo_reqwidth() - 10,
                y=int(data['root_height'] / 2) - button1.winfo_reqheight() - 10
            )
            button2.place(
                x=int(data['root_width'] / 2) - button2.winfo_reqwidth() - button1.winfo_reqwidth() - 20,
                y=int(data['root_height'] / 2) - button2.winfo_reqheight() - 10
            )
            info.mainloop()

    tab2 = Canvas(data['root'])
    tab2.config(bg='#fff', bd=0, highlightthickness=0)
    tab2.config(
        width=data['root_width'],
        height=data['root_height']
    )
    tab2.place(
        x=data['root_width'] * 2,
        y=data['navbar_height'] + data['tabbar_height'] + data['tabbarunderline_height'] + data['shadow_height'] + 10
    )
    update_data('tab2', tab2)
    tab2.update()

    bootloader_label = Label(tab2, text="Boot Loader")
    bootloader_label.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    bootloader_label.place(x=(data['root_width'] - bootloader_label.winfo_reqwidth()) / 2, y=10)
    bootloader_label.update()

    update_data('bootloader_label', bootloader_label)

    bootloader_value = StringVar(tab2)
    bootloader_value.set("GRUB2 for EFI")
    update_data('bootloader_value', bootloader_value)
    select_bootloader = OptionMenu(tab2, bootloader_value, "GRUB2 for EFI", "GRUB2", "Not Managed", command=update_tab2)

    select_bootloader.place(
        x=(data['root_width'] - select_bootloader.winfo_reqwidth()) / 2,
        y=20 + bootloader_label.winfo_reqheight()
    )
    select_bootloader.update()
    update_data('select_bootloader', select_bootloader)
