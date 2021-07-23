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

root = Tk()
root.title('FruityPlayer ~ 2021 Build+')
root.iconbitmap("D:\\FruityProjects\\FruityPlayer\\fruity.ico")
root.geometry("500x300")
root.configure(background='darkred')

pygame.mixer.init()

# Discordian Shitz Lolz
client_id = '868092183427837973'  # Put your Client ID here, this is a fake ID
RPC = Presence(client_id)  # Initialize the Presence class
if RPC.connect is None:
    pass
elif RPC.connect is True:
    RPC.connect()  # Start the handshake loop
    RPC.update(details="FruityProjects", state="Maybe listening to some jazz..", large_image="fruit") #Set the presence, picking a random quote

def statusTime():
    cTime = pygame.mixer.music.get_pos() / 1000
    converted = time.strftime('%H:%M:%S', time.gmtime(cTime))
    cSong = box.curselection()
    song = box.get(ACTIVE)
    song = f'D:\FruityProjects\FruityPlayer\music\{song}.mp3'
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
    song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3'

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

    song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3'

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

    song = f'D:/FruityProjects/FruityPlayer/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    box.selection_clear(0, END)
    box.activate(nextS)
    box.selection_set(nextS, last=None)

controls = Frame(root)
controls.pack()

backButton = Button(controls, text='back', background='darkgreen', command=backFunction)
forwardButton = Button(controls, text='forward', background='darkgreen', command=forwardFunction)
playButton = Button(controls, text='play', background='darkblue', command=playFunction)
pauseButton = Button(controls, text='pause', background='yellow', command=lambda: pauseFunction(paused))
stopButton = Button(controls, text='stop', background='yellow', command=stopFunction)

backButton.grid(row=0, column=0, padx=15)
forwardButton.grid(row=0, column=1, padx=15)
playButton.grid(row=0, column=2, padx=15)
pauseButton.grid(row=0, column=3, padx=15)
stopButton.grid(row=0, column=4, padx=15)

# Menu shitz lol

menu = Menu(root, tearoff=0)
root.config(menu=menu)

def addNewSong():
    newSong = filedialog.askopenfilename(initialdir="D:\FruityProjects\FruityPlayer\music", title='New Song Selector', filetypes=(("MP3 Files", "*.mp3"), ))
    # print(newSong)
    # newSong = newSong.replace("C:", "")
    # newSong = newSong.replace("D:", "")
    # newSong = newSong.replace("B:", "")
    # newSong = newSong.replace("F:", "")
    # newSong = newSong.replace("Y:", "")
    newSong = newSong.replace("D:/FruityProjects/FruityPlayer/music/", "")
    newSong = newSong.replace(".mp3", "")
    # newSong = newSong.replace(".opus", "")
    # newSong = newSong.replace(".wav", "")
    # newSong = newSong.replace(".ogg", "")
    # # newSong = newSong.replace("/", "")
    # # newSong = newSong.replace("\\", "")
    # # newSong = newSong.replace("", f"{newSong}")
    # newSong = newSong.replace("Downloads", "")
    box.insert(END, newSong)

def addNewSongs():
    newSongs = filedialog.askopenfilenames(initialdir="D:\FruityProjects\FruityPlayer\music", title='New Song Selector', filetypes=(("MP3 Files", "*.mp3"), ))

    for newSongw in newSongs:
        newSongw = newSongw.replace("D:/FruityProjects/FruityPlayer/music/", "")
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

root.mainloop()