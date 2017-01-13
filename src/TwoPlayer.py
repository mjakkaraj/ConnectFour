import tkinter as tk
import random
from tkinter import ttk

class TwoPlayer(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.canvas = tk.Canvas(self, width=700, height=700, borderwidth=0, highlightthickness=0)
		self.canvas.pack(side="top", fill="both", expand="true")
		self.rows = 0
		self.columns = 0
		self.cellwidth = 100
		self.cellheight = 100
		
		self.canvas.bind("<Button-1>", self.callback)

		self.turn = 0
		self.size = (700, 700)

		self.rect = {}
		self.oval = {}
		for column in range(7):
			for row in range(7):
				x1 = column*self.cellwidth
				y1 = row * self.cellheight
				x2 = x1 + self.cellwidth
				y2 = y1 + self.cellheight
				self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="yellow", tags="rect")
				self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="black", tags="oval")

		#self.redraw(1000)


	def callback(self,event):
	#print ("clicked at", event.x, event.y)
		loc = event.x//self.cellwidth
		for i in range(7):
			item_id = self.oval[6-i,loc]
			if(self.canvas.itemcget(item_id, "fill") == "black"):
				if(self.turn == 0):
					self.turn =1
					self.canvas.itemconfig(item_id, fill="Red")
					return self.checkstate("Red")
				if(self.turn == 1):
					self.turn =0
					self.canvas.itemconfig(item_id, fill="Blue")
					return self.checkstate("Blue")

	def checkstate(self, color):
		for i in range(7-3):
			for j in range(7):
				item_id = self.oval[i,j]
				c1 = self.canvas.itemcget(item_id, "fill")
				item_id2 = self.oval[i+1,j]
				c2 = self.canvas.itemcget(item_id2, "fill")
				item_id3 = self.oval[i+2,j]
				c3 = self.canvas.itemcget(item_id3, "fill")
				item_id4 = self.oval[i+3,j]
				c4 = self.canvas.itemcget(item_id4, "fill")
				if((c1 == color) and (c2 == color) and (c3 == color) and (c4 == color)):
					
					self.endgame(color)
					return

		for j in range(7-3):
			for i in range(7):
				item_id = self.oval[i,j]
				c1 = self.canvas.itemcget(item_id, "fill")
				item_id2 = self.oval[i,j+1]
				c2 = self.canvas.itemcget(item_id2, "fill")
				item_id3 = self.oval[i,j+2]
				c3 = self.canvas.itemcget(item_id3, "fill")
				item_id4 = self.oval[i,j+3]
				c4 = self.canvas.itemcget(item_id4, "fill")
				if((c1 == color) and (c2 == color) and (c3 == color) and (c4 == color)):
					
					self.endgame(color)
					return
		
		for i in range(3,7):
			for j in range(7-3):
				item_id = self.oval[i,j]
				c1 = self.canvas.itemcget(item_id, "fill")
				item_id2 = self.oval[i-1,j+1]
				c2 = self.canvas.itemcget(item_id2, "fill")
				item_id3 = self.oval[i-2,j+2]
				c3 = self.canvas.itemcget(item_id3, "fill")
				item_id4 = self.oval[i-3,j+3]
				c4 = self.canvas.itemcget(item_id4, "fill")
				if((c1 == color) and (c2 == color) and (c3 == color) and (c4 == color)):
					
					self.endgame(color)
					return

		for i in range(3,7):
			for j in range(3,7):
				item_id = self.oval[i,j]
				c1 = self.canvas.itemcget(item_id, "fill")
				item_id2 = self.oval[i-1,j-1]
				c2 = self.canvas.itemcget(item_id2, "fill")
				item_id3 = self.oval[i-2,j-2]
				c3 = self.canvas.itemcget(item_id3, "fill")
				item_id4 = self.oval[i-3,j-3]
				c4 = self.canvas.itemcget(item_id4, "fill")
				if((c1 == color) and (c2 == color) and (c3 == color) and (c4 == color)):
					
					self.endgame(color)
					return
				

	def endgame(self, color):
		#self.canvas.pack_forget()
		for i in range(7):
			for j in range(7):
				self.canvas.delete(self.oval[i,j])
		for i in range(7):
			for j in range(7):
				self.canvas.delete(self.rect[i,j])

		self.canvas.configure(background='yellow')

		# generate button text style
		#BUTTONS = "TkDefaultFont " + str(self.size[1] // (2*(3 + 3)))   TkHeadingFont
		BUTTONS = "Georgia " + str(self.size[1] // (3*(3 + 3))) + " bold"
		winnerTitle = ttk.Label(self.canvas,text=color+" Wins!",font="Georgia " + str(2*(self.size[1] // (3*(3 + 3)))) +" bold" ,anchor=tk.N)
		winnerTitle.configure(background='yellow')
		winnerTitle.grid(column = 0,row = 0)
		# create all buttons
		onePlayer = tk.Button(self.canvas,text="New Game",font=BUTTONS ,command=self.newgame)
		onePlayer.configure(background='white')
		onePlayer.grid(column = 0, row = 1)
		twoPlayer = tk.Button(self.canvas,text="Exit",font=BUTTONS ,command=self.nothing)
		twoPlayer.configure(background='white')
		twoPlayer.grid(column = 0, row = 2)
				
	def newgame(self):

		self.canvas.destroy()
		self.canvas = tk.Canvas(self, width=700, height=700, borderwidth=0, highlightthickness=0)
		self.canvas.pack(side="top", fill="both", expand="true")
		self.rows = 0
		self.columns = 0
		self.cellwidth = 100
		self.cellheight = 100
		self.canvas.bind("<Button-1>", self.callback)
		self.turn = 0
		self.size = (700, 700)
		self.rect = {}
		self.oval = {}
		for column in range(7):
			for row in range(7):
				x1 = column*self.cellwidth
				y1 = row * self.cellheight
				x2 = x1 + self.cellwidth
				y2 = y1 + self.cellheight
				self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="yellow", tags="rect")
				self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="black", tags="oval")


	def nothing(self):
		exit()

	def redraw(self, delay):
		self.canvas.itemconfig("rect", fill="yellow")
		self.canvas.itemconfig("oval", fill="black")
		for i in range(10):
			row = random.randint(0,6)
			col = random.randint(0,6)
			item_id = self.oval[row,col]
			self.canvas.itemconfig(item_id, fill="red")
		self.after(delay, lambda: self.redraw(delay))


