import configure_one as conf_o
from threading import Thread
import functions as func
import download as downld
from time import sleep


class PathAndName():
    def __init__(self, master=None):
        self.frameConfig()
        self.labelConfig()
        self.entryConfig()
        self.buttonConfig()

    def frameConfig(self):
        global frameTitle, frameEntry, frameButton, frameWait, frameFinish, \
            destroyFrames
        frameTitle = func.makeFrame()
        frameTitle.place(x=172, y=20)

        frameEntry = func.makeFrame()
        frameEntry.place(x=56, y=55)

        frameButton = func.makeFrame()
        frameButton.place(x=197, y=90)

        destroyFrames = [frameTitle, frameEntry, frameButton]

        # ------- Second Part --------
        frameWait = func.makeFrame()
        frameWait.place(x=147, y=60)

        frameFinish = func.makeFrame()
        frameFinish.place(x=153, y=50)

    def labelConfig(self):
        func.makeLabel('Nome do arquivo', frameTitle)

    def entryConfig(self):
        self.fileName = func.makeEntry(frameEntry)

    def buttonConfig(self):
        download = func.makeButton('Download', frameButton)
        download.bind('<Button-1>', self.doDownload)

    def waitConfig(self):
        func.makeLabel('Download em andamento', frameWait)

    def finishConfig(self):
        func.makeLabel('Download concluído', frameFinish)

    def doDownload(self, event=None):
        try:
            fileName = self.fileName.get()
            fileDir = func.openDirectory()
            for frame in destroyFrames:
                frame.destroy()
            self.waitConfig()
            conf_o.root.update()
            sleep(1)
            Thread(target=downld.downloadYouTube,
                   args=(conf_o.yt, conf_o.fileType, fileName, fileDir)).start()
            Thread(target=self.threadDownload).start()

        except:
            self.fileName.delete(0, 'end')
            self.fileName.insert('end', 'Erro no download')

    def threadDownload(self):
        while True:
            sleep(1)
            try:
                downld.stream
                frameWait.destroy()
                self.finishConfig()
                conf_o.root.update()
                break
            except:
                try:
                    conf_o.root.winfo_exists()
                except:
                    exit()
