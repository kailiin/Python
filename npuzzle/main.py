#!/usr/bin/python3
# coding: utf-8

import math
import sys
import time
import check_input
from puzzle import Puzzle
import final_board
import soluble

def manhattan(board):
	d = 0
	side = int(math.sqrt(len(board)))
	i = 0
	final_b = final_board.final_dict[side]
	while i < (side * side - 1):
		# # total Manhattan distance += abs(x2 - x1) + abs(y2 - y1)
		d += abs(i % side - board.index(final_b[i]) % side) + abs(int(i / side) - int(board.index(final_b[i]) / side))
		i += 1
	return d

def find_best(l_open):
	best_node = l_open[0]
	for node in l_open:
		if node.costF < best_node.costF:
			best_node = node
	return best_node

def set_neighbor(x, y, p):
	tmp_board = p.board.copy()
	tmp_value = p.board[x]
	tmp_board[x] = p.board[y]
	tmp_board[y] = tmp_value
	return Puzzle(p.costC + 1, manhattan(tmp_board), p, tmp_board)
	
def find_neighbor(p):
	l_tmp = []
	i = p.board.index(0)
	side = int(math.sqrt(len(p.board)))
	if i % side > 0:
		l_tmp.append(set_neighbor(i, i - 1, p))
	if i % side + 1 < side:
		l_tmp.append(set_neighbor(i, i + 1, p))
	if i / side >= 1:
		l_tmp.append(set_neighbor(i, i - side, p))
	if i / side < side - 1:
		l_tmp.append(set_neighbor(i, i + side, p))
	return l_tmp

def check_in(board=None, puzzle=None, l_p=[]):
	i = 0
	for p in l_p:
		if (board != None) and (board == p.board):
			return i
		elif (puzzle != None) and (puzzle.board == p.board):
			return i
		i += 1
	return -1

def print_result(result, exec_time):
	side = int(math.sqrt(len(result.board)))
	i = 0
	my_list = []
	while result.parent != None:
		my_list.insert(0, result.board)
		result = result.parent
	my_list.insert(0, result.board)

	for b in my_list:
		for nb in b:
			print(nb, " ", end="")
			i += 1
			if i == side:
				i = 0
				print("")
		print("")
	print("Cost: ", len(my_list) - 1)
	print("Time: ", exec_time, "s")

def a_star(board, ft_heuristic, final_b):
	start_time = time.time()
	l_open = [Puzzle(0, manhattan(board), None, board)]
	l_close = []
	while l_open:
		if check_in(final_b, None, l_open) >= 0:
			print_result(l_open[check_in(final_b, None, l_open)], time.time() - start_time)
			return
		else:
			best_node = find_best(l_open)
			l_close.append(best_node)
			l_open.remove(best_node)
			# print(best_node.board)
			l_neighbor = find_neighbor(best_node)
			for neighbor in l_neighbor:
				index_in_open = check_in(None, neighbor, l_open)
				index_in_close = check_in(None, neighbor, l_close)
				if (index_in_open < 0) and (index_in_close < 0):
					l_open.append(neighbor)
					continue
				if index_in_open >= 0 and neighbor.costF < l_open[index_in_open].costF:
					l_open[index_in_open] = neighbor
					continue
				# if index_in_close >= 0 and l_close[index_in_close].costF >= neighbor.costF :
				# 	l_close.remove(l_close[index_in_close])
				# 	l_open.append(neighbor)
				# 	continue
	print("Puzzle insoluble")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		init_b = check_input.check_input(sys.argv[1])
		side = int(math.sqrt(len(init_b)))
		final_b = final_board.final_dict[side]
		if soluble.check_soluble(init_b, final_b):
			a_star(init_b, manhattan, final_b)
		else:
			print("Puzzle insoluble")
	else:
		print("usage: python3 ./main.py file_name")

	# # init_b = [0,2,3,1,4,5,8,7,6]
	# # init_b = [1,2,3,4,5,6,7,0,8]
	# init_b = [8,4,6,2,3,5,1,0,7]
	# side = int(math.sqrt(len(init_b)))
	# # test range -> ok ou error
	# final_b = final_board.final_dict[side]
	# if soluble.check_soluble(init_b, final_b):
	# 	a_star(init_b, manhattan, final_b)
	# else:
	# 	print("Puzzle insoluble")
