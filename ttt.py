from __future__ import print_function
import numpy as np
import os
import time

class TicTacToe:
	def __init__(self):		
		self.board = np.array(['.' for i in range(9)])		
		self.player = 'X'
		self.positions = [i for i in range(9)]

	def printBoard(self):
		for i in range(9):
			print(self.board[i], end = " ")
			if (i+1) % 3 == 0:
				print("\n")	

	def availablePositions(self):
		pos = []
		for i in range(9):
			if self.board[i] == '.':
				pos.append(i)
		return pos

	def gameOver(self):
		rows = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
		cols = np.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]])
		diags = np.array([[0, 4, 8], [2, 4, 6]])
		
		#Checking the rows
		for row in rows:
			XrowsCheck = np.all([self.board[row[i]] == 'X' for i in range(3)]) 
			OrowsCheck = np.all([self.board[row[i]] == 'O' for i in range(3)])
			#print(rowsCheck)
			if XrowsCheck:
				return 1
			elif OrowsCheck:
				return -1

		#Checking the cols
		for col in cols:
			XcolsCheck = np.all([self.board[col[i]] == 'X' for i in range(3)]) 
			OcolsCheck = np.all([self.board[col[i]] == 'O' for i in range(3)]) 
			if XcolsCheck:
				return 1
			elif OcolsCheck:
				return -1

		#Checking the diagonals
		for diag in diags:
			XdiagsCheck = np.all([self.board[diag[i]] == 'X' for i in range(3)])
			OdiagsCheck = np.all([self.board[diag[i]] == 'O' for i in range(3)])
			if XdiagsCheck:
				return 1
			elif OdiagsCheck:
				return -1

		#Checking for draw
		count = 0
		for i in range(9):
			if self.board[i] == '.': count += 1
		#print(count)
		if count == 0:
			#print("Tie Game!")
			return 0

		#Still playing...		
		return 2


	def move(self, position):
		self.board[position] = self.player
		if self.player == 'X': self.player = 'O'
		else: self.player = 'X'
				

class Player:	
	def move(self, positions):
		while True:
			print("---------------------")
			print("Available Positions!")
			for i in range(9):
				if i in positions:
					print(i, end = " ")
				else:
					print(" ", end = " ")
				if (i+1) % 3 == 0:
					print("\n")
			position = input("Choose a position from the following : ")
			if position in positions:
				return position
			else:
				print("Invalid position...Try Again...")


class Computer:
	def __init__(self, game):
		self.game = game
		self.symbol = 'O'
		self.human = 'X'

	def minimax(self, node, depth, alpha, beta, maximizingPlayer):
		if self.game.gameOver() == 1:
			return 1, -1
		elif self.game.gameOver() == -1:
			return -1, -1
		elif self.game.gameOver() == 0:
			return 0, -1
			

		if maximizingPlayer:
			maxEval = -float('inf')
			maxPos = None
			for i in range(9):
				if self.game.board[i] == '.':
					self.game.board[i] = self.human
					evaluation, pos = self.minimax(self.game.board, depth + 1, alpha, beta, False)
					self.game.board[i] = '.'
					
					alpha = max(alpha, evaluation)
					if evaluation > maxEval:
						maxEval = evaluation
						maxPos = i
					if beta <= alpha:
						break
			return maxEval, maxPos

		else:
			minEval = float('inf')
			minPos = None
			for i in range(9):
				if self.game.board[i] == '.':
					self.game.board[i] = self.symbol
					evaluation, pos = self.minimax(self.game.board, depth + 1, alpha, beta, True)
					self.game.board[i] = '.'
					beta = min(beta, evaluation)
					if evaluation < minEval:
						minEval = evaluation
						minPos = i
					if beta <= alpha:
						break

			return minEval, minPos

if __name__ == "__main__":	
	game = TicTacToe()
	human = Player()
	comp = Computer(game)
	player = 'X'	
	alpha = -float('inf')
	beta = float('inf')

	while True:
		positions = game.availablePositions()
		os.system('clear')
		game.printBoard()
		
		if player == 'X':
			position = human.move(positions)
			player = 'O'
		else:
			score = -float('inf')
			position = None
			evaluation, possiblePos = comp.minimax(game.board, 0, alpha, beta, False)
			if evaluation > score:
				score = evaluation
				position = possiblePos
			player = 'X'
			#time.sleep(1)

		game.move(position)	

		if game.gameOver() == 1:
			print("Winner : Human")
			break
		elif game.gameOver() == -1:
			print("Winner : AI")
			break
		elif game.gameOver() == 0:
			print("Tie Game!")
			break

	game.printBoard()


