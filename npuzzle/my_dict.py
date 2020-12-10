#!/usr/bin/python3
# coding: utf-8

import math

final_dict = {}
final_dict[3] = (1,2,3, 8,0,4, 7,6,5)
final_dict[4] = (1,2,3,4, 12,13,14,5, 11,0,15,6, 10,9,8,7)
final_dict[5] = (1,2,3,4,5, 16,17,18,19,6, 15,24,0,20,7, 14,23,22,21,8, 13,12,11,10,9)

# allow 4-way movement: right, left, top, bottom
def manhattan(board, side):
	d = 0
	i = 1
	final = final_dict[side]
	while i < (side * side):
		# # total Manhattan distance += abs(x2 - x1) + abs(y2 - y1)
		d += abs(final.index(i) % side - board.index(i) % side) + abs(int(final.index(i) / side) - int(board.index(i) / side))
		i += 1
	return d
	
# move at any angle 
def euclidean(board, side):
	d = 0
	i = 1
	final = final_dict[side]
	while i < (side * side):
		# # total Manhattan distance += abs(x2 - x1) + abs(y2 - y1)
		dx = abs(final.index(i) % side - board.index(i) % side)
		dy = abs(int(final.index(i) / side) - int(board.index(i) / side))
		d += math.sqrt(dx * dx + dy * dy)
		i += 1
	return d


def tiles_out_of_place(board, side):
	d = 0
	final = final_dict[side]
	for i in range(side * side):
		if board[i] != 0 and board[i] != final[i]:
			d += 1
	return d

def uniform_cost(board:None, side:None):
	return 0


heuristic_func = {}
heuristic_func["1"] = manhattan
heuristic_func["2"] = euclidean
heuristic_func["3"] = tiles_out_of_place
