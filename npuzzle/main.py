#!/usr/bin/python3
# coding: utf-8

import math
import sys
import heapq 
import time
import check_input
import soluble
import my_dict

# def manhattan(board, side):
# 	d = 0
# 	i = 1
# 	final = final_board.final_dict[side]
# 	while i < (side * side):
# 		# # total Manhattan distance += abs(x2 - x1) + abs(y2 - y1)
# 		d += abs(final.index(i) % side - board.index(i) % side) + abs(int(final.index(i) / side) - int(board.index(i) / side))
# 		i += 1
# 	return d

# def find_best(l_open=[]):
# 	best_node = l_open[0]
# 	for node in l_open:
# 		if node.costF < best_node.costF:
# 			best_node = node
# 	return best_node

# def set_neighbor(x, y, p, side):
# 	tmp_board = p.board.copy()
# 	tmp_value = p.board[x]
# 	tmp_board[x] = p.board[y]
# 	tmp_board[y] = tmp_value
# 	return Puzzle(p.costC + 1, manhattan(tmp_board, side), p, tmp_board)
	
# def find_neighbor(p, side):
# 	l_tmp = []
# 	i = p.board.index(0)
# 	if i % side > 0:
# 		l_tmp.append(set_neighbor(i, i - 1, p, side))
# 	if i % side + 1 < side:
# 		l_tmp.append(set_neighbor(i, i + 1, p, side))
# 	if i / side >= 1:
# 		l_tmp.append(set_neighbor(i, i - side, p, side))
# 	if i / side < side - 1:
# 		l_tmp.append(set_neighbor(i, i + side, p, side))
# 	return l_tmp

# def check_in(board=None, puzzle=None, l_p=[]):
# 	i = 0
# 	for p in l_p:
# 		if (board != None) and (board == p.board):
# 			return i
# 		elif (puzzle != None) and (puzzle.board == p.board):
# 			return i
# 		i += 1
# 	return -1

# def check_end(l=[]):
# 	for ele in l:
# 		if ele.costD == 0:
# 			return True
# 	return False

# def print_result(side, result, exec_time, nb_node):
# 	i = 0
# 	my_list = []
# 	while result.parent != None:
# 		my_list.insert(0, result.board)
# 		result = result.parent
# 	my_list.insert(0, result.board)

# 	for b in my_list:
# 		for nb in b:
# 			print(f"{nb} ", end="")
# 			if side > 3 and nb < 10:
# 				print(" ", end="")
# 			i += 1
# 			if i == side:
# 				i = 0
# 				print("")
# 		print("")
# 	print(f"Cost: {len(my_list) - 1}")
# 	print(f"Time: {exec_time:.5f}")
# 	print(f"Node: {nb_node}")

# def a_star(board, ft_heuristic, final_b, side):
# 	start_time = time.time()
# 	l_open = [Puzzle(0, manhattan(board, side), None, board)]
# 	l_close = []
# 	bool_end = check_end(l_open)
# 	while l_open:
# 		if bool_end:
# 			print_result(side, l_open[check_in(final_b, None, l_open)], time.time() - start_time, len(l_open) + len(l_close))
# 			return
# 		else:
# 			best_node = l_open[0]

# 			# print(len(l_close) + len(l_open))
# 			# for open in l_open:
# 			# 	print(open.board, open.costC, open.costD, open.costF)
# 			# print("close:")
# 			# for close in l_close:
# 			# 	print(close.board, close.costC, close.costD, close.costF)
# 			# print("best:",best_node.board,best_node.costC)
# 			# print("\n")
# 			# time.sleep(.2)


# 			# maybe del Puzzle
# 			# dict_open = {}
# 			# dict_open[board] = {"costC":0, "costD":manhattan(board, side), "costF":manhattan(board, side), "parent":None}
# 			# dict_close = {}

# 			# if key in dict:
# 			# list_open = []
# 			# value = (manhattan(board, side), 0, board) # costF costC board
# 			# heapq.heappop(list_open, value)  #add
# 			# heapq.heappop(list_open) # pop


# 			l_close.append(best_node)
# 			l_open.remove(best_node)
# 			l_neighbor = find_neighbor(best_node, side)
# 			bool_end = check_end(l_neighbor)
# 			for neighbor in l_neighbor:
# 				index_in_open = next((x for x in l_open if x.board == neighbor.board), None) #check_in(None, neighbor, l_open)
# 				index_in_close = next((x for x in l_close if x.board == neighbor.board), None)
# 				if (not index_in_open) and (not index_in_close):
# 					# if neighbor.costF <= best_node.costF:
# 					# 	l_open.insert(0, neighbor)
# 					# else:
# 					# 	l_open.append(neighbor)
# 					bisect.insort_left(l_open, neighbor)
# 					continue
# 				if index_in_open and neighbor.costF < index_in_open.costF:
# 					# if neighbor.costF <= best_node.costF:
# 					# 	l_open.remove(l_open[index_in_open])
# 					# 	l_open.insert(0, neighbor)
# 					# else:
# 					# 	l_open[index_in_open] = neighbor
# 					l_open.remove(index_in_open)
# 					bisect.insort_left(l_open, neighbor)
# 				# 	continue
# 				# if index_in_close and index_in_close.costF > neighbor.costF :
# 				# 	l_close.remove(index_in_close)
# 				# 	bisect.insort_left(l_open, neighbor)
# 	print("Puzzle insoluble")

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

def print_result(side, result, my_dict, exec_time, nb_node):
	i = 0
	my_list = []
	while result[4] != None:
		my_list.insert(0, result[3])
		result = my_dict[result[4]]
	my_list.insert(0, result[3])

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
	print(f"Time: {exec_time:.5f}")
	print(f"Node: {nb_node}")

# puzzle: (0= costF, 1= costD, 2= costC, 3= board, 4= parent)
def a_star(board, ft_heuristic, side):
	start_time = time.time()
	list_open = []
	dict_open = {}
	dict_close = {}

	heuristic = ft_heuristic(board, side)
	final = my_dict.final_dict[side]
	heapq.heappush(list_open, (heuristic, heuristic, 0, board, None))
	dict_open[board] = [heuristic, heuristic, 0, board, None]

	while list_open:
		if final in dict_open:
			time_use = time.time() - start_time
			complexity_time = len(list_open)
			dict_close.update(dict_open)
			print_result(side, dict_open[final], dict_close, time_use, len(dict_close))
			return
		else:
			puzzle = heapq.heappop(list_open)
			key = puzzle[3]
			if not(key in dict_open) or puzzle[2] != dict_open[key][2]:
				continue
			del dict_open[key]
			dict_close[key] = puzzle
			l_neighbor = find_neighbor(puzzle, side, ft_heuristic)
			for neighbor in l_neighbor:
				n_key = neighbor[3]
				if not (n_key in dict_open or n_key in dict_close):
					heapq.heappush(list_open, neighbor)
					dict_open[n_key] = neighbor
					continue
				if n_key in dict_open and neighbor[0] < dict_open[n_key][0]:
					heapq.heappush(list_open, neighbor)
					dict_open[n_key] = neighbor
				# if n_key in dict_close:
				# 	pass
	print("Puzzle insoluble")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		init_b = check_input.check_input(sys.argv[1])
		side = int(math.sqrt(len(init_b)))
		if soluble.check_soluble(init_b, my_dict.final_dict[side]):
			print("Chose your heuristic function:")
			print("1: Manhattan")
			print("2: Euclidean")
			print("3: Tiles out of place")
			nb = input()
			if nb in ["1", "2", "3"]:
				a_star(init_b, my_dict.heuristic_func[nb], side)
		else:
			print("Puzzle insoluble")
	else:
		print("usage: python3 ./main.py file_name")


# complexity in size  and complexity in time