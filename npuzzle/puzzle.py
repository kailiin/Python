#!/usr/bin/python3
# coding: utf-8

class Puzzle:

	def __init__(self, c=int, d=int, p=None, b=[]):
		self.costC = c
		self.costD = d
		self.costF = c + d
		self.parent = p
		self.board = b

	def __lt__(self, other):
		return self.costF < other.costF
	