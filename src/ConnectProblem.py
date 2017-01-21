from copy import deepcopy
import random
from AIproblem import *



class ConnectProblem(AIproblem):
	def __init__(self, initialState, size, color1, color2, evalFn=None, goal=None ):

		self.initial = deepcopy(initialState)
		self.size = size
		self.goal = goal
		self.evalFn = evalFn
		self.color1 = deepcopy(color1)
		self.color2 = deepcopy(color2)
		self.actions = [0, 1, 2, 3, 4, 5, 6]

	# Potential additional method of getNeighbors, but essentially this is the same as expanding a node
	# so really not necessary.
	# return [ applyAction( state, a) for a in getActions( state ) ]

	def getRandomAction( self, state ):
		# randomly produce a single action applicable for this state
		return None

	def getActions( self, state ) :
		# produce a list of actions to be applied to the current state
		# Pruning could happen here (i.e. only generate legal actions that result in legal states)
		newactions = deepcopy(self.actions)
		for j in range(self.size):
			if state[0][j] != "Black":
				newactions.remove(j)
			
		return newactions

	def applyAction ( self, state, action ) :
		# Does nothing but copy the current state. This will be problem specific.
		# Apply the action to the current state to produce a new state
		# If you did not check for illegal states in getActions, then check for illegal states here
		# Can evaluate node based on path cost, heuristic function, or fitness function
		if None :
			return []
		else :
			newState = deepcopy(state)
			count1 =0
			count2 =0
			for i in range(7):
				for j in range(7):
					if(newState[i][j] == self.color1):
						count1+=1
					if(newState[i][j] == self.color2):
						count2+=1
			
			nextmove = deepcopy(self.color1)
			if(count1>=count2):
				nextmove = deepcopy(self.color2)

				#print ("clicked at", event.x, event.y)
			loc = deepcopy(action)
			for i in range(7):
				#item_id = self.oval[6-i,loc]
				if(newState[6-i][loc] == "Black"):
					newState[6-i][loc] = nextmove
					break
			
			return newState

	def evaluation( self, state ):

		score = 0

		#print(state)

		for i in range(7-3):
			for j in range(7):
				c1 = state[i][j]
				c2 = state[i+1][j]
				c3 = state[i+2][j]
				c4 = state[i+3][j]

				if((c1 == self.color1) and (c2 == self.color1)):
					score+=1
				if((c1 == self.color2) and (c2 == self.color2)):
					score-=2
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1)):
					score+=2
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2)):
					score-=3
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1) and (c4 == self.color1)):		
					#score+=100000
					score = float("inf")
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2) and (c4 == self.color2)):
					#score-=100000
					score = float("-inf")

		for j in range(7-3):
			for i in range(7):

				c1 = state[i][j]
				c2 = state[i][j+1]
				c3 = state[i][j+2]
				c4 = state[i][j+3]

				if((c1 == self.color1) and (c2 == self.color1)):
					score+=1
				if((c1 == self.color2) and (c2 == self.color2)):
					score-=2
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1)):
					score+=2
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2)):
					score-=3
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1) and (c4 == self.color1)):		
					#score+=100000
					score = float("inf")
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2) and (c4 == self.color2)):
					#score-=100000
					score = float("-inf")

		for i in range(3,7):
			for j in range(7-3):

				c1 = state[i][j]
				c2 = state[i-1][j+1]
				c3 = state[i-2][j+2]
				c4 = state[i-3][j+3]

				if((c1 == self.color1) and (c2 == self.color1)):
					score+=1
				if((c1 == self.color2) and (c2 == self.color2)):
					score-=2
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1)):
					score+=2
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2)):
					score-=3
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1) and (c4 == self.color1)):		
					#score+=100000
					score = float("inf")
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2) and (c4 == self.color2)):
					#score-=100000
					score = float("-inf")

		for i in range(3,7):
			for j in range(3,7):

				c1 = state[i][j]
				c2 = state[i-1][j-1]
				c3 = state[i-2][j-2]
				c4 = state[i-3][j-3]

				if((c1 == self.color1) and (c2 == self.color1)):
					score+=1
				if((c1 == self.color2) and (c2 == self.color2)):
					score-=2
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1)):
					score+=2
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2)):
					score-=3
				if((c1 == self.color1) and (c2 == self.color1) and (c3 == self.color1) and (c4 == self.color1)):		
					#score+=100000
					score = float("inf")
				if((c1 == self.color2) and (c2 == self.color2) and (c3 == self.color2) and (c4 == self.color2)):
					#score-=100000
					score = float("-inf")
		return score

	def isGoal ( self, state ):
		# Determine if current state is goal
		return False
