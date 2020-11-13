#!/usr/bin/env python3
# coding: utf-8

import sys

def ft_find_rang(line):  
	content = line.split()
	for c in content:
		if c.find("#") == 0:
			return None
		elif c.isnumeric():
			return int(c)
		elif c != " ":
			return -1
	return None

def ft_check_line(line, rang, listnumber):
	counter = 0
	max = rang * rang
	content = line.split()
	for c in content:
		if c.find("#") == 0:
			break
		elif c.isdigit() and int(c) < max and counter < max and listnumber.count(int(c)) == 0:
			listnumber.append(int(c))
			counter += 1
		else:
			return False
	if counter == 0 or counter ==rang:
		return True
	return False

def ft_check_input(file_name):
	rang = None
	listnumber = []
	with open(file_name, 'r') as f:
		for line in f:
			if rang == None:
				rang = ft_find_rang(line)
				if rang !=None and rang < 3:
					print("error: ", rang)
					return False
			elif ft_check_line(line, rang, listnumber):
				continue
			else:
				return False
	if rang ==None or rang < 3:
		return False
		
	# print file info			
	print(rang)
	counter = 0
	for ele in listnumber:
		print(ele, " ",end="")
		counter +=1
		if counter == rang:
			counter = 0
			print("")
	
	return True


			


if __name__ == "__main__":
	if len(sys.argv) == 2:
		if ft_check_input(sys.argv[1]):
			print("file ok")
		else:
			print("fille error")
	else:
		print("usage : python3 argv1 argv2")
