import tkinter
from tkinter import *
import pygame
from pygame import *
from pygame.key import name
from tkinter import filedialog
from pypresence import Presence
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

splash = Tk()
splash.iconbitmap("D:\\FruityProjects\\FruityPlayer\\fruity.ico") # No need to change this
splash.title('FruityPlayer ~ Loading+')

appW = 727
appH = 200

screenW = splash.winfo_screenwidth()
screenH = splash.winfo_screenheight()

x = (screenW / 2) - (appW / 2)
y = (screenH / 2) - (appH / 2)

splash.geometry(f"{appW}x{appH}+{int(x)}+{int(y)}")
splash.configure(background='darkred')
splash.resizable(False, False)

splashLabel = Label(splash, text="Loading..", font=("Bold", 60))
splashLabel.pack(pady=20)

pygame.mixer.init()

def playerWindow():
    splash.destroy()

    root = Tk()
    root.title('FruityPlayer ~ 2021 Build+')
    root.iconbitmap("D:\\FruityProjects\\FruityPlayer\\fruity.ico") # No need to change this
    
    appW = 500
    appH = 300

    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    
    x = (screenW / 2) - (appW / 2)
    y = (screenH / 2) - (appH / 2)

    root.geometry(f"{appW}x{appH}+{int(x)}+{int(y)}")
    root.configure(background='darkred')
    root.resizable(False, False)

    background_image = PhotoImage("D:\FruityProjects\FruityPlayer\images\\fruity2.png")
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=500, relheight=300)

    # back = PhotoImage(file="D:\FruityProjects\FruityPlayer\images\\fruity2.png")

    # backDisplay = Canvas(root, width=500, height=300)
    # backDisplay.pack(fill="both", expand=True, anchor='nw')

    # backDisplay.create_image(0, 0, image=back)

    # Discordian Shitz Lolz (Only uncomment if you have discord open, will not work if discord is not open.)

    # client_id = '868092183427837973'
    # RPC = Presence(client_id)
    # RPC.connect()
    # RPC.update(details="FruityProjects", state="Maybe listening to some jazz..", large_image="fruit")

    def statusTime():
        cTime = pygame.mixer.music.get_pos() / 1000
        converted = time.strftime('%H:%M:%S', time.gmtime(cTime))
        cSong = box.curselection()
        song = box.get(ACTIVE)
        song = f'D:\FruityProjects\FruityPlayer\music\{song}.mp3' # (PERSONAL GUIDE) Replace with the url to your music directory, along with the song.mp3 thing.
        mut = MP3(song)
        status.after(1000, statusTime)
        songL = mut.info.length
        convertedL = time.strftime('%H:%M:%S', time.gmtime(songL))
        status.config(text=f"Elapsed: {converted} ~ Duration: {convertedL}")

    # Variables for later lol

    box = Listbox(root, bg="grey", fg="white", width=60, selectbackground='red', selectforeground='yellow')
    box.pack(pady=20)

    # backButton = Button(name='Back')
    # forwardButton = Button(name='Forward')
    # playButton = Button(name='Play')
    # pauseButton = Button(name='Pause')
    # stopButton = Button(name='Stop')

    # Function Shitz Lol
    def playFunction():
        song = box.get(ACTIVE)
        song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3' # (PERSONAL GUIDE) Replace with the url to your music directory, along with the song.mp3 thing.

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        statusTime()

    def stopFunction():
        pygame.mixer.music.stop()
        box.selection_clear(ACTIVE)
        status.config(text="")

    global paused
    paused = False

    def pauseFunction(pauseds):
        global paused
        paused = pauseds

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:        
            pygame.mixer.music.pause()
            paused = True

    def forwardFunction():
        nextS = box.curselection()
        # print(nextS)
        # print(nextS[0])
        nextS = nextS[0]+1
        song = box.get(nextS)

        song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3' # (PERSONAL GUIDE) Replace with the url to your music directory, along with the song.mp3 thing.

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        box.selection_clear(0, END)
        box.activate(nextS)
        box.selection_set(nextS, last=None)

    def backFunction():
        nextS = box.curselection()
        # print(nextS)
        # print(nextS[0])
        nextS = nextS[0]-1
        song = box.get(nextS)

        song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3' # (PERSONAL GUIDE) Replace with the url to your music directory, along with the song.mp3 thing.

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        box.selection_clear(0, END)
        box.activate(nextS)
        box.selection_set(nextS, last=None)

    def loopFunction():
        pygame.mixer.music.play(loops=-1)

    def replayFunction():
        pygame.mixer.music.rewind()

    controls = Frame(root)

    controls.pack()

    backButton = Button(controls, text='previous', background='purple', command=backFunction)
    forwardButton = Button(controls, text='next', background='darkgreen', command=forwardFunction)
    playButton = Button(controls, text='play', background='darkblue', command=playFunction)
    pauseButton = Button(controls, text='pause', background='yellow', command=lambda: pauseFunction(paused))
    stopButton = Button(controls, text='stop', background='pink', command=stopFunction)
    loopButton = Button(controls, text='loop', background='red', command=loopFunction)
    replayButton = Button(controls, text='replay', background='cyan', command=replayFunction)

    backButton.grid(row=0, column=0, padx=15)
    forwardButton.grid(row=0, column=1, padx=15)
    playButton.grid(row=0, column=2, padx=15)
    pauseButton.grid(row=0, column=3, padx=15)
    stopButton.grid(row=0, column=4, padx=15)
    loopButton.grid(row=0, column=5, padx=15)
    replayButton.grid(row=0, column=6, padx=15)

    # Menu shitz lol

    menu = Menu(root, tearoff=0)
    root.config(menu=menu)

    def addNewSong(): # (PERSONAL GUIDE) Change initialdir to your music directory, or just remove it..doesn't matter.
        newSong = filedialog.askopenfilename(initialdir="D:\FruityProjects\FruityPlayer\music", title='New Song Selector', filetypes=(("MP3 Files", "*.mp3"), ))
        # print(newSong)
        # newSong = newSong.replace("C:", "")
        # newSong = newSong.replace("D:", "")
        # newSong = newSong.replace("B:", "")
        # newSong = newSong.replace("F:", "")
        # newSong = newSong.replace("Y:", "")
        newSong = newSong.replace("D:/FruityProjects/FruityPlayer/music/", "") # (PERSONAL GUIDE) Change this to your music directory.
        newSong = newSong.replace(".mp3", "")
        # newSong = newSong.replace(".opus", "")
        # newSong = newSong.replace(".wav", "")
        # newSong = newSong.replace(".ogg", "")
        # # newSong = newSong.replace("/", "")
        # # newSong = newSong.replace("\\", "")
        # # newSong = newSong.replace("", f"{newSong}")
        # newSong = newSong.replace("Downloads", "")
        box.insert(END, newSong)

    def addNewSongs(): # (PERSONAL GUIDE) Change initialdir to your music directory, or just remove it..doesn't matter.
        newSongs = filedialog.askopenfilenames(initialdir="D:\FruityProjects\FruityPlayer\music", title='New Song Selector', filetypes=(("MP3 Files", "*.mp3"), ))

        for newSongw in newSongs:
            newSongw = newSongw.replace("D:/FruityProjects/FruityPlayer/music/", "") # (PERSONAL GUIDE) Change this to your music directory.
            newSongw = newSongw.replace(".mp3", "")
            box.insert(END, newSongw)

    addSong = Menu(menu, tearoff=0)
    menu.add_cascade(label='New Song', menu=addSong)
    addSong.add_command(label='Add Song', command=addNewSong)
    addSong.add_command(label='Add Songs', command=addNewSongs)
    addSong.add_separator()
    addSong.add_command(label='Exit', command=root.destroy)

    def deleteSong():
        box.delete(ANCHOR)
        pygame.mixer.music.stop()

    def deleteSongs():
        box.delete(0, END)
        pygame.mixer.music.stop()

    removeSong = Menu(menu, tearoff=0)
    menu.add_cascade(label='Delete Song', menu=removeSong)
    removeSong.add_command(label="Remove Song", command=deleteSong)
    removeSong.add_command(label="Remove Songs", command=deleteSongs)

    status = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
    status.pack(fill=X, side=BOTTOM, ipady=2)

# Other Function Stuff lool

def confirm():
    confirmation = "D:\FruityProjects\FruityPlayer\musicAssets\confirm.wav" # (PERSONAL GUIDE) Make sure this shit exist somewhere in your files and link the dir right here, idk if it works without it or not so do it anyway lol
    pygame.mixer.music.load(confirmation)
    pygame.mixer.music.play()

splash.after(3000, confirm)
splash.after(3000, playerWindow)
mainloop()