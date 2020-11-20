#!/usr/bin/env python3
# coding: utf-8

import math 
import check_input
from puzzle import Puzzle

def manhattan(board):
	d = 0
	s = int(math.sqrt(len(board)))
	for i in range(len(board)):
		# total Manhattan distance += abs(x2 - x1) + abs(y2 - y1)
		d += abs(i / s - board[i] / s ) + abs(i % s - board[i] % s )
	return d

def find_best(l_open):
	best_node = l_open[0]
	for node in l_open:
		if node.costF < best_node.costF:
			best_node = node
	return best_node

def set_neighbor(x, y, p):
	tmp_board = p.board.copy()
	# print("befor switch: ", tmp_board)
	tmp_value = p.board[x]
	tmp_board[x] = p.board[y]
	tmp_board[y] = tmp_value
	# print("after switch: ", tmp_board)
	return Puzzle(p.costC + 1, manhattan(tmp_board), p, tmp_board)
	
def find_neighbor(p):
	l_tmp = []
	i = p.board.index(0)
	side = int(math.sqrt(len(p.board)))
	# print(i)
	# print(p.board)
	if i % side > 0:
		# print("1 ", end="")
		l_tmp.append(set_neighbor(i, i - 1, p))
	if i % side + 1 < side:
		# print("2 ", end="")
		l_tmp.append(set_neighbor(i, i + 1, p))
	if i / side >= 1:
		# print("3 ", end="")
		l_tmp.append(set_neighbor(i, i - side, p))
	if i / side < side - 1:
		# print("4 ", end="")
		l_tmp.append(set_neighbor(i, i + side, p))
	# print("")
	return l_tmp

def check_in(b, l_p):
	i = 0
	for p in l_p:
		if p.board == b.board:
			return i
		i += 1
	return -1		

def a_star(board, ft_heuristic, final_b):
	l_open = [Puzzle(0, manhattan(board), None, board)]
	l_close = []
	succes = False
	while l_open and (not succes):
		best_node = find_best(l_open)
		if best_node.board == final_b:
			return best_node
		else:
			l_close.append(best_node)
			l_open.remove(best_node)
			# print(best_node.board)
			l_neighbor = find_neighbor(best_node)
			for neighbor in l_neighbor:
				index_in_open = check_in(neighbor, l_open)
				index_in_close = check_in(neighbor, l_close)
				if (index_in_open < 0) and (index_in_close < 0):
					l_open.append(neighbor)
					continue
				if index_in_open >= 0 and neighbor.costF < l_open[index_in_open].costF:
					l_open[index_in_open] = neighbor
					continue
				if index_in_close >= 0 and l_close[index_in_close].costF >= neighbor.costF :
					l_close.remove(l_close[index_in_close])
					l_open.append(neighbor)
					continue
				if index_in_open < 0:
					l_open.append(neighbor)
	print("pas de solution")


if __name__ == "__main__":
# final_b = [1,2,3,8,0,4,7,6,5]
	init_b = [0,2,3,1,4,5,8,7,6]
	final_b = [1,2,3,4,5,6,7,8,0]
	result = a_star(init_b, manhattan, final_b)
	print(result.board)
