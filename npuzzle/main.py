#!/usr/bin/python3
# coding: utf-8

import math
import sys
import heapq 
import time
import check_input
import solvable
import my_dict
import graphical_interface

def set_neighbor(x, y, puzzle, side, ft_heuristic):
	board = puzzle[3]
	tmp_board = list(board)
	tmp_value = board[x]
	tmp_board[x] = board[y]
	tmp_board[y] = tmp_value
	heuristic = ft_heuristic(tmp_board, side)
	return (heuristic + (puzzle[2] + 1), heuristic, (puzzle[2] + 1), tuple(tmp_board), board)
	
def find_neighbor(puzzle, side, ft_heuristic):
	l_tmp = []
	i = puzzle[3].index(0)
	if i % side > 0:
		l_tmp.append(set_neighbor(i, i - 1, puzzle, side, ft_heuristic))
	if i % side + 1 < side:
		l_tmp.append(set_neighbor(i, i + 1, puzzle, side, ft_heuristic))
	if i / side >= 1:
		l_tmp.append(set_neighbor(i, i - side, puzzle, side, ft_heuristic))
	if i / side < side - 1:
		l_tmp.append(set_neighbor(i, i + side, puzzle, side, ft_heuristic))
	return l_tmp

def print_result(side, open, close, exec_time, graphic):
	complexity_time = len(close)
	complexity_size = len(close) + len(open)
	final = my_dict.final_dict[side]
	result = close[final]
	my_list = []
	while result[4] != None:
		my_list.insert(0, result[3])
		result = close[result[4]]
	my_list.insert(0, result[3])

	i = 0
	for b in my_list:
		for nb in b:
			print(f"{nb} ", end="")
			if side > 3 and nb < 10:
				print(" ", end="")
			i += 1
			if i == side:
				i = 0
				print("")
		print("")
	print(f"Cost: {len(my_list) - 1}")
	print(f"Time complexity: {complexity_time}")
	print(f"Size complexity: {complexity_size}")
	print(f"Time: {exec_time:.5f} sec")
	if graphic:
		graphical_interface.init_result(my_list, side)


# puzzle: (0= costF, 1= costD, 2= costC, 3= board, 4= parent)
# just check the best heuristic value  => costD
# No complete – can get stuck in loops. 
def gredy_search(board, ft_heuristic, side, graphic):
	start_time = time.time()
	current = []
	dict_close = {}

	heuristic = ft_heuristic(board, side)
	final = my_dict.final_dict[side]
	current = [heuristic, heuristic, 0, board, None]

	while current:
		puzzle = current
		key = puzzle[3]
		current = None
		dict_close[key] = puzzle
		if final == key:
			time_use = time.time() - start_time
			print_result(side, {}, dict_close, time_use, graphic)
			return
		else:
			l_neighbor = find_neighbor(puzzle, side, ft_heuristic)
			best = None
			for neighbor in l_neighbor:
				n_key = neighbor[3]
				if not (dict_close.get(n_key)):
					if not best:
						best = neighbor
					elif neighbor[1] < best[1]:
						best = neighbor
			current = best
	print("Greedy search error: infinite loop")		

	
# puzzle: (0= costC, 1=cost_heuristic, 2=cost_C, 3= board, 4= parent)   / 1 no use
# Just sort by current cost (lowest cumulative cost)  => ft_heuristic = empty / no use
# cost of all edges is the same => uniform_cost = BFS (Breadth First Search)
# heapq: binary trees -> push / pop and return the smallest item from the heap
def uniform_cost_search(board, side, graphic):
	start_time = time.time()
	list_open = []
	dict_open = {}
	dict_close = {}

	final = my_dict.final_dict[side]
	heapq.heappush(list_open, (0, 0, 0, board, None))
	dict_open[board] = [0, 0, 0, board, None]

	while list_open:
		puzzle = heapq.heappop(list_open)
		key = puzzle[3]
		del dict_open[key]
		dict_close[key] = puzzle
		if final == key:
			time_use = time.time() - start_time
			print_result(side, dict_open, dict_close, time_use, graphic)
			return
		else:
			l_neighbor = find_neighbor(puzzle, side, my_dict.uniform_cost)
			for neighbor in l_neighbor:
				n_key = neighbor[3]
				if not (dict_open.get(n_key) or dict_close.get(n_key)):
					heapq.heappush(list_open, neighbor)
					dict_open[n_key] = neighbor

# puzzle: (0= costF, 1= costD, 2= costC, 3= board, 4= parent)
# heapq: binary trees -> push / pop and return the smallest item from the heap
def a_star(board, ft_heuristic, side, graphic):
	start_time = time.time()
	list_open = []
	dict_open = {}
	dict_close = {}

	heuristic = ft_heuristic(board, side)
	final = my_dict.final_dict[side]
	heapq.heappush(list_open, (heuristic, heuristic, 0, board, None))
	dict_open[board] = [heuristic, heuristic, 0, board, None]

	while list_open:
		puzzle = heapq.heappop(list_open)
		key = puzzle[3]
		# heapq -> list_open peut contenir plusieurs fois des ele avec meme board
		# à cause de:  n_key in dict_open and neighbor[0] < dict_open[n_key][0]
		# On test just la meilleur qui est stocker dans dict_open
		if not(key in dict_open) or puzzle[2] != dict_open[key][2]:
			continue
		del dict_open[key]
		dict_close[key] = puzzle
		if final == key:
			time_use = time.time() - start_time
			print_result(side, dict_open, dict_close, time_use, graphic)
			return
		else:
			l_neighbor = find_neighbor(puzzle, side, ft_heuristic)
			for neighbor in l_neighbor:
				n_key = neighbor[3]
				if not (dict_open.get(n_key) or dict_close.get(n_key)):
					heapq.heappush(list_open, neighbor)
					dict_open[n_key] = neighbor
					continue
				if dict_open.get(n_key) and neighbor[0] < dict_open[n_key][0]:
					heapq.heappush(list_open, neighbor)
					dict_open[n_key] = neighbor
				# if dict_close.get(n_key):
				# 	pass

if __name__ == "__main__":
	if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[1] == "-g"):
		if len(sys.argv) == 2:
			init_b = check_input.check_input(sys.argv[1])
		else:
			init_b = check_input.check_input(sys.argv[2])
		side = int(math.sqrt(len(init_b)))
		if solvable.check_solvable(init_b, my_dict.final_dict[side]):
			if len(sys.argv) == 2:
				bool_graph = False
			else:
				bool_graph = True
			print("Chose your Search Algorithms:")
			print("1: Astar")
			print("2: Greedy seatch")
			print("3: Uniform cost search")
			algo = input().split()
			if len(algo) == 1 and  algo[0] in ["1", "2", "3"]:
				if algo[0] == "3":
					uniform_cost_search(init_b, side, bool_graph)
				else:
					print("Chose your heuristic function:")
					print("1: Manhattan")
					print("2: Euclidean")
					print("3: Tiles out-of-place")
					heuri = input().split()
					if len(heuri) == 1 and heuri[0] in ["1", "2", "3"]:
						if algo[0] == "1":
							a_star(init_b, my_dict.heuristic_func[heuri[0]], side, bool_graph)
						else:
							gredy_search(init_b, my_dict.heuristic_func[heuri[0]], side, bool_graph)
					else:
						print("Error: chose 1, 2 or 3")
			else:
				print("Error: chose 1, 2 or 3")
		else:
			print("Puzzle unsolvable")
	elif len(sys.argv) == 3 and sys.argv[1] == "-p":
		init_b = check_input.check_input(sys.argv[2])
		side = int(math.sqrt(len(init_b)))
		if solvable.check_solvable(init_b, my_dict.final_dict[side]):
			graphical_interface.init_play(list(init_b), side)
		else:
			print("Puzzle unsolvable")
	else:
		print("usage: python3 ./main.py [-p -g] file_name")

# test sur 5x5  bonus: spped mode?
# del les commentaires ?
