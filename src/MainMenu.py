import tkinter as tk
import random
from tkinter import ttk
from TwoPlayer import *
from OnePlayer import *

class MainMenu(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.canvas = tk.Canvas(self, width=700, height=700, borderwidth=0, highlightthickness=0)
		self.canvas.pack(side="top", fill="both", expand="true")


		self.turn = 0
		self.size = (700, 700)
		self.setup()




	def setup(self):

		self.canvas.configure(background='yellow')

		# generate button text style
		#BUTTONS = "TkDefaultFont " + str(self.size[1] // (2*(3 + 3)))   TkHeadingFont
		BUTTONS = "Georgia " + str(38) + " bold"
		winnerTitle = ttk.Label(self.canvas,text = "Connect Four",font="Georgia " + str(76) +" bold" ,anchor=tk.N)
		winnerTitle.configure(background='yellow')
		winnerTitle.grid(column = 0,row = 0)
		# create all buttons
		onePlayer = tk.Button(self.canvas,text="Single Player",font=BUTTONS ,command=self.onePlayer)
		onePlayer.configure(background='white')
		onePlayer.grid(column = 0, row = 1)

		twoPlayer = tk.Button(self.canvas,text="Two Player",font=BUTTONS ,command=self.twoPlayer)
		twoPlayer.configure(background='white')
		twoPlayer.grid(column = 0, row = 2)

		exitgame = tk.Button(self.canvas,text="Exit",font=BUTTONS ,command=self.nothing)
		exitgame.configure(background='white')
		exitgame.grid(column = 0, row = 3)


	def onePlayer(self):
		#self.canvas.destroy()
		app3 = OnePlayer()
		app3.mainloop()
	def twoPlayer(self):
		#self.canvas.destroy()
		app2 = TwoPlayer()
		app2.mainloop()
		


	def nothing(self):
		exit()



app = MainMenu()
app.mainloop()
