from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

from src.app.data import *


def set_text(entry_widget: object = None, text: object = None):
    entry_widget.delete(0, END)
    entry_widget.insert(0, text)


def load_file():
    fname = askopenfilename(filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    if fname:
        try:
            graphical_console_theme = data['graphical_console_theme_entry']
            set_text(entry_widget=graphical_console_theme, text=fname)
        except Exception as e:
            print(e)
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return


def create_tab3():
    tab3 = Canvas(data['root'])
    tab3.config(bg='#fff', bd=0, highlightthickness=0)
    tab3.config(
        width=data['root_width'],
        height=data['root_height']
    )
    tab3.place(
        x=data['root_width'] * 4,
        y=data['navbar_height'] + data['tabbar_height'] + data['tabbarunderline_height'] + data['shadow_height'] + 10
    )
    update_data('tab3', tab3)

    l1 = Label(tab3, text="Optional kernel command line parameter")
    l1.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    l1.place(x=35, y=10)
    l1.update()

    kernel_parameters = StringVar(tab3, value='default kernel parameters')
    e1 = Entry(tab3)
    e1.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=kernel_parameters
    )
    l1.update()
    e1.place(x=35, y=20 + l1.winfo_reqheight(), height=30, width=data['root_width'] - 70)
    e1.update()

    use_graphical_console = BooleanVar()
    c1 = Checkbutton(
        tab3, variable=use_graphical_console,
        onvalue=True, offvalue=False
    )
    c1.config(fg='#888', bd=0)
    c1.place(x=35, y=50 + l1.winfo_reqheight() + e1.winfo_reqheight(), height=25, width=25)
    c1.select()
    c1.update()
    l2 = Label(tab3, text='Use graphical console')
    l2.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    l2.place(x=c1.winfo_reqwidth() + 40, y=50 + l1.winfo_reqheight() + e1.winfo_reqheight())
    l2.update()

    graphical_console_frame = Frame(tab3)
    graphical_console_frame.config(
        bd=3, highlightthickness=2, bg='#fff', width=data['root_width'] - 70, height=100
    )
    graphical_console_frame.place(
        x=35, y=60 + l1.winfo_reqheight() + e1.winfo_reqheight() + c1.winfo_reqheight()
    )
    graphical_console_frame.update()

    l3 = Label(graphical_console_frame, text='Console Theme')
    l3.config(
        fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0
    )
    l3.place(x=35, y=10)
    l3.update()

    graphical_console_theme = StringVar(graphical_console_frame, value='default theme')
    e2 = Entry(graphical_console_frame)
    e2.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=graphical_console_theme
    )
    e2.place(
        x=35, y=20 + l3.winfo_reqheight(),
        height=30, width=graphical_console_frame.winfo_reqwidth() - 210
    )
    e2.update()

    console_theme_browse_button = Button(graphical_console_frame, text="Browse", command=load_file)
    console_theme_browse_button.config(
        fg='#fff', bg='#F83E7D', bd=0, font='"Futura" 12 bold', padx=20, cursor='hand2'
    )
    console_theme_browse_button.place(
        x=45 + e2.winfo_width(), y=20 + l3.winfo_reqheight(), height=30
    )
    console_theme_browse_button.update()

    use_serial_console = BooleanVar()
    c2 = Checkbutton(
        tab3, variable=use_serial_console,
        onvalue=True, offvalue=False
    )
    c2.config(fg='#888', bd=0)
    c2.place(
        x=35,
        y=100 + l1.winfo_reqheight() + e1.winfo_reqheight() + graphical_console_frame.winfo_height(),
        height=25, width=25
    )
    c2.update()
    l4 = Label(tab3, text=' Use serial console')
    l4.config(
        fg='#555', bg='#fff', font='"Roboto" 14 bold', bd=0
    )
    l4.place(
        x=c1.winfo_reqwidth() + 40,
        y=100 + l1.winfo_reqheight() + e1.winfo_reqheight() + graphical_console_frame.winfo_height(),
    )
    l4.update()

    serial_console_frame = Frame(tab3)
    serial_console_frame.config(
        bd=3, highlightthickness=2, bg='#fff', width=data['root_width'] - 70, height=100
    )
    serial_console_frame.place(
        x=35,
        y=110 + l1.winfo_reqheight() + e1.winfo_reqheight() + graphical_console_frame.winfo_height() + c1.winfo_reqheight()
    )
    serial_console_frame.update()

    l5 = Label(serial_console_frame, text='Console Arguments')
    l5.config(
        fg='#555', bg='#fff', font='"Roboto" 12 bold', bd=0
    )
    l5.place(x=35, y=10)
    l5.update()

    serial_console_theme = StringVar(serial_console_frame, value='default theme')
    e3 = Entry(serial_console_frame)
    e3.config(
        fg='#888', bg='#fff', bd=0, font='"Times" 12 bold', exportselection=0,
        highlightcolor='#2540db', textvariable=serial_console_theme
    )
    e3.place(
        x=35, y=20 + l3.winfo_reqheight(),
        height=30, width=serial_console_frame.winfo_reqwidth() - 70
    )
    e3.update()

    update_data(
        'kernel_parameters', kernel_parameters,
        'graphical_console_theme', graphical_console_theme,
        'serial_console_theme', serial_console_theme,
        'use_graphical_console', use_graphical_console,
        'use_serial_console', use_serial_console,
        'kernel_parameters_entry', e1,
        'graphical_console_theme_entry', e2,
        'serial_console_theme_entry', e3,
        'graphical_console_frame', graphical_console_frame,
        'serial_console_frame', serial_console_frame,
        'console_theme_browse_button', console_theme_browse_button
    )
