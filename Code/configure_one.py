import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter.filedialog import askdirectory as askDir
import configure_two as conf_t
from threading import Thread
import functions as func
import download as downld


bgGeral = 'white smoke'
fontGeral = ('Consolas', '12')
tpChoice = ('Vídeo', 'Áudio')


class HomePage():
    def __init__(self, master=None):
        self.windowConfig()
        self.frameConfig()
        self.buttonConfig()
        self.entryConfig()
        self.labelConfig()
        self.choiceConfig()

    def frameConfig(self):
        global frameTitle, frameUrl, frameEntry, frameBtn, frameFile, destroyFrames

        frameTitle = func.makeFrame()
        frameTitle.place(x=190, y=20)

        frameUrl = func.makeFrame()
        frameUrl.place(x=15, y=47)

        frameEntry = func.makeFrame()
        frameEntry.place(x=56, y=50)

        frameBtn = func.makeFrame()
        frameBtn.place(x=100, y=100)

        frameFile = func.makeFrame()
        frameFile.place(x=310, y=85)

        destroyFrames = [frameBtn, frameFile, frameTitle, frameUrl, frameEntry]

    def windowConfig(self):
        root.title('YouTube - Download')
        img = tk.PhotoImage(file='Images/youtube.png')
        root.iconphoto(False, img)
        # root.iconbitmap('C:/Users/matuc/Downloads/youtube.ico')
        root.configure(bg=bgGeral)
        root.geometry('480x200+440+240')
        root.resizable(False, False)

    def buttonConfig(self):
        down = func.makeButton('Download', frameBtn)
        down.bind('<Button-1>', self.changeLayout)

    def entryConfig(self):
        self.urlEntry = func.makeEntry(frameEntry)
        self.urlEntry.focus()

    def labelConfig(self):
        func.makeLabel('YouTube URL', frameTitle)

        func.makeLabel('URL:', frameUrl)

        func.makeLabel('Arquivo', frameFile)

    def choiceConfig(self):
        self.choiceBox = func.makeChoiceBox(tpChoice, frameFile)
        self.choiceBox.pack(side='bottom')

    def changeLayout(self, event=None):
        try:
            url = self.urlEntry.get()
            self.urlEntry.delete(0, 'end')
            self.urlEntry.insert('end', 'Aguarde...')
            root.update()

            checkUrl = Thread(target=downld.checkUrl, args=(url,))
            checkUrl.start()
            check = Thread(target=self.checkToChange)
            check.start()

        except:
            self.urlEntry.delete(0, 'end')
            self.urlEntry.insert('end', 'Verifique a URL')

    def checkToChange(self):
        global yt
        while True:
            sleep(1)
            try:
                yt = downld.yt
                self.destroyAndChange()
                break
            except:
                try:
                    root.winfo_exists()
                except:
                    exit()

    def destroyAndChange(self):
        global fileType
        fileType = self.choiceBox.get()
        for frame in destroyFrames:
            frame.destroy()
        Thread(target=conf_t.PathAndName(root))


root = tk.Tk()
Thread(target=HomePage(root))
