from pytube import YouTube


def checkUrl(url):
    global yt
    yt = YouTube(url)
    return yt


def downloadYouTube(yt, fileType, fileName, fileDir):
    global stream
    if fileType == 'Vídeo':
        stream = yt.streams.first().download(fileDir, filename=fileName)
    elif fileType == 'Áudio':
        stream = yt.streams.filter(only_audio=True).first().download(fileDir,
                                                                     filename=fileName)
