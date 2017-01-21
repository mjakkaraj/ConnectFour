import tkinter as tk
import random
from copy import deepcopy
from tkinter import ttk
from ConnectProblem import *

class OnePlayer(tk.Tk):
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
				self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="Black", tags="oval")
		
		#self.canvas.itemconfig(self.oval[6,3], fill="Blue")


	def callback(self,event):
		loc = event.x//self.cellwidth
		for i in range(7):
			item_id = self.oval[6-i,loc]
			
			if(self.canvas.itemcget(item_id, "fill") == "Black"):
				if(self.turn == 0):
					self.canvas.itemconfig(item_id, fill="Red")
					self.checkstate("Red")
					break				


		
		self.computermove()
		#print("computer has moved")
		self.checkstate("Blue")
		return


	def computermove(self):
		state = []
		for i in range(7):
			row = []
			for j in range(7):
				item_id = self.oval[i,j]	
				row.append(deepcopy(self.canvas.itemcget(item_id, "fill")))
			state.append(row)
		
		problem = ConnectProblem(state, 7, "Blue", "Red")
		node = Node( problem.initial )


		#for child in node.expand(problem):
		#	print(child.getState())

		tmpnode = deepcopy(node)
		maxscore = float("-inf")
		for child in node.expand(problem):
			if problem.evaluation( child.getState() )==float("inf"):
				maxscore = float("inf")
				tmpnode = deepcopy(child)
				break
			
			tmpval = self.minimax(child, 4, False, problem)
			#print(tmpval)
			if tmpval > maxscore:
				maxscore = tmpval
				tmpnode = deepcopy(child)
		'''
		if(maxscore == float("-inf")):
			for child in node.expand(problem):
				
				tmpval = self.minimax(child, 4, False, problem)
					
				if tmpval > maxscore:
					maxscore = tmpval
					tmpnode = deepcopy(child)
		'''

		if(maxscore == float("-inf")):
			for child in node.expand(problem):
				
				tmpval = self.minimax(child, 3, False, problem)
					
				if tmpval > maxscore:
					maxscore = tmpval
					tmpnode = deepcopy(child)	

		if(maxscore == float("-inf")):
			for child in node.expand(problem):
				
				tmpval = self.minimax(child, 2, False, problem)
					
				if tmpval > maxscore:
					maxscore = tmpval
					tmpnode = deepcopy(child)

		if(maxscore == float("-inf")):
			for child in node.expand(problem):

				tmpval = self.minimax(child, 1, False, problem)
					
				if tmpval > maxscore:
					maxscore = tmpval
					tmpnode = deepcopy(child)
		
		if(maxscore == float("-inf")):
			for child in node.expand(problem):
	
				tmpval = self.minimax(child, 0, False, problem)
					
				if tmpval >= maxscore:
					maxscore = tmpval
					tmpnode = deepcopy(child)

		#print(problem.evaluation(tmpnode.getState()))

		for i in range(7):
			for j in range(7):
				item_id = self.oval[i,j]
				self.canvas.itemconfig(item_id, fill=tmpnode.getState()[i][j])


	def minimax(self, node, depth, maximizingPlayer, problem):
		if ((depth == 0) or (problem.getActions( node.getState() ) == [])):
			
			return problem.evaluation( node.getState() )


		if (maximizingPlayer == True):
			bestValue = float("-inf")

			#currentstate = problem.evaluation( node.getState() )
			#if (currentstate == float("inf") ):
			#	return currentstate

			for child in node.expand(problem):
				val = problem.evaluation( child.getState() )
				if (val == float("inf")):
					return val

				
					
				val = self.minimax(child, depth-1, False, problem)
				bestValue = max(bestValue, val)

			return bestValue
		
		if(maximizingPlayer == False):
			bestValue = float("inf")

			#currentstate = problem.evaluation( node.getState() )
			#if( currentstate == float("-inf") ):
			#	return currentstate

			for child in node.expand(problem):

				val = problem.evaluation( child.getState() )
				if (val == float("-inf")):
					return val

				val = self.minimax(child, depth-1, True, problem)
				bestValue = min(bestValue, val)
			
			return bestValue		
				
				
			

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
		
		for i in range(7):
			for j in range(7):
				self.canvas.delete(self.oval[i,j])
		for i in range(7):
			for j in range(7):
				self.canvas.delete(self.rect[i,j])

		self.canvas.configure(background='yellow')

		# generate button text style
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
				self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="Yellow", tags="rect")
				self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="Black", tags="oval")


	def nothing(self):
		exit()



class Node:

	nodeCount = 0

	def __init__(self, state, parent=None, action=None):
		self.state = state
		self.nodeCount = 0
		if parent:
			self.depth = parent.depth + 1

	def expand(self, problem):
		#print('actions:',problem.getActions(self.state))
		return [ self.makeChild( problem, action) for action in problem.getActions( self.state ) ]

	def makeChild(self, problem, action):
		Node.nodeCount += 1
		#if 0 == (Node.nodeCount % 100) :
		#	print( 'nodeCount: ',Node.nodeCount )
		childState = problem.applyAction( self.state, action )
		return Node( childState )

	def getState(self ):
		return self.state


