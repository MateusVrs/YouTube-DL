import configure_one as conf_o


def makeFrame():
    frame = conf_o.tk.Frame(conf_o.root)
    return frame


def makeButton(text, master=None):
    btn = conf_o.tk.Button(master, text=text, font=conf_o.fontGeral,
                           bg='coral', relief='ridge')
    btn['activebackground'] = 'tomato'
    btn.pack(side='top')
    return btn


def makeEntry(master=None):
    entry = conf_o.tk.Entry(master, font=conf_o.fontGeral,
                            width='40', bg=conf_o.bgGeral)
    entry.pack(side='top')
    return entry


def makeLabel(text, master=None):
    label = conf_o.tk.Label(master, text=text,
                            font=conf_o.fontGeral, bg=conf_o.bgGeral)
    label.pack(side='top')
    return label


def makeChoiceBox(options, master=None):
    choice = conf_o.ttk.Combobox(master, width='6', state='readonly')
    choice['values'] = options
    choice.current(0)
    return choice


def openDirectory():
    dirs = conf_o.askDir(parent=conf_o.root)
    return dirs
