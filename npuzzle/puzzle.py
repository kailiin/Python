#!/usr/bin/python3

class Puzzle:

	def __init__(self, c=int, d=int, p=None, b=[]):
		self.costC = c
		self.costD = d
		self.costF = c + d
		self.parent = p
		self.board = b

	def switch_parent(self, new_p):
		self.parent = new_p
	
	