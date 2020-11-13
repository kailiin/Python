#!/usr/bin/env python3
# coding: utf-8

import sys

def ft_find_rang(line):  
	content = line.split()
	rang = None
	for c in content:
		if c.find("#") == 0:
			return rang
		elif c.isnumeric() and rang == None:
			rang = int(c)
		else:
			return -1
	return rang

def ft_check_line(line, rang, listnumber):
	counter = 0
	max = rang * rang
	content = line.split()
	for c in content:
		if c.find("#") == 0:
			break
		elif c.isnumeric() and int(c) < max and counter < max and listnumber.count(int(c)) == 0:
			listnumber.append(int(c))
			counter += 1
		else:
			return False
	if counter == 0 or counter ==rang:
		return True
	return False

def ft_check_input(file_name):
	rang = None
	count_rang = 0
	listnumber = []
	with open(file_name, 'r') as f:
		for line in f:
			if rang == None:
				rang = ft_find_rang(line)
				if rang !=None and rang < 3:
					print("error: ", rang) #####################  test print   ########################
					return False
			elif ft_check_line(line, rang, listnumber):
				count_rang +=1
				continue
			else:
				return False
	if rang ==None or rang < 3 or count_rang != rang:
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
