# -*- coding: utf-8 -*-

from tkinter import *

fen = Tk()

label = Label(fen, text="coucou")
label.pack()

bouton = Button(fen, text="Fermer", command=fen.quit)
bouton.pack()

fen.mainloop()