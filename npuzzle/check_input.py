#!/usr/bin/python3
# coding: utf-8

import sys
import os

def check_numeric(my_str):
	my_list = ['0','1','2','3','4','5','6','7','8','9']
	for c in my_str:
		if not c in my_list:
			return False
	return True

def find_rang(line):  
	content = line.split()
	rang = None
	for c in content:
		comment_index = c.find("#")
		if comment_index == 0:
			return rang
		elif comment_index > 0:
			c = c[0:comment_index]
			if check_numeric(c) and rang == None:
				return int(c)
		#check if  3 4 #....
		if check_numeric(c) and rang == None:
			rang = int(c)
		else:
			return -1
	return rang

def check_line(line, rang, listnumber):
	counter = 0
	max = rang * rang
	content = line.split()
	for c in content:
		comment_index = c.find("#")
		if comment_index == 0:
			return counter
		elif comment_index > 0:
			c = c[0:comment_index]
			if check_numeric(c) and int(c) < max and counter < max and listnumber.count(int(c)) == 0:
				listnumber.append(int(c))
				counter += 1
				break
		if check_numeric(c) and int(c) < max and counter < max and listnumber.count(int(c)) == 0:
			listnumber.append(int(c))
			counter += 1
		else:
			return -1
	if counter == rang or len(content) == 0:
		return counter
	return -1

def check_input(file_name):
	rang = None
	count_rang = 0
	listnumber = []
	try:
		with open(file_name, 'r') as f:
			for line in f:
				if rang == None:
					rang = find_rang(line)
					if rang != None and rang < 3 and rang > 5:
						raise Exception("Rang error: invalid or < 3 or > 5")
				elif check_line(line, rang, listnumber) > 0:
					count_rang +=1
					continue
				elif check_line(line, rang, listnumber) == 0:
					continue
				else:
					raise Exception("Puzzle content error.")
		if rang == None or count_rang != rang:
			raise Exception("Puzzle error: check rang and content.")
		return tuple(listnumber)
	except Exception as e:
		print("Exception:", e)
		sys.exit()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		my_list = []
		my_list = check_input(sys.argv[1])
		print(my_list)
	else:
		print("usage: python3 ./check_input file_name")
