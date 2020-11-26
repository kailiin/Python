#!/usr/bin/python3
# coding: utf-8

import sys
import os

# check number is numeric or not
# 01 => False, 1 => True 
def check_numeric(my_str):
	my_list = ['0','1','2','3','4','5','6','7','8','9']
	if len(my_str) > 1 and my_str[0] == '0':
		return False
	for c in my_str:
		if not c in my_list:
			return False
	return True

# find puzzle size -> if line content:
#	comment / null / space  -> return None : check next line
#	one numeric number -> return number = puzzle size
#	not numeric or several number -> return -1 = Error
def find_size(line):  
	content = line.split()
	size = None
	for c in content:
		comment_index = c.find("#")
		if comment_index == 0:
			return size
		elif comment_index > 0:
			c = c[0:comment_index]
			if check_numeric(c) and size == None:
				return int(c)
		#check if  3 4 #....
		if check_numeric(c) and size == None:
			size = int(c)
		else:
			return -1
	return size

# check line content, if content:
# 	comment / null / space  -> return 0
# 	content == numeric and content < max and not duplicate -> add content to list and counter +=1  else return -1
# 	content != numeric -> return -1 = Error
# if counter != size -> return -1 else return counter ==> line OK
def check_line(line, size, listnumber):
	counter = 0
	max = size * size
	content = line.split()
	for c in content:
		comment_index = c.find("#")
		if comment_index == 0:
			return counter
		elif comment_index > 0:
			c = c[0:comment_index]
			if check_numeric(c) and int(c) < max and (not int(c) in listnumber):
				listnumber.append(int(c))
				counter += 1
				break
		if check_numeric(c) and int(c) < max and (not int(c) in listnumber):
			listnumber.append(int(c))
			counter += 1
		else:
			return -1
	if counter == size or len(content) == 0:
		return counter
	return -1

# check file line by line and return tuple:
# 	find / check puzzle size
#	find / check puzzle contenr
def check_input(file_name):
	size = None
	count_size = 0
	listnumber = []
	try:
		with open(file_name, 'r') as f:
			for line in f:
				if size == None:
					size = find_size(line)
					if size != None and size < 3 and size > 5:
						raise Exception("Size error: invalid or < 3 or > 5")
				elif check_line(line, size, listnumber) > 0:
					count_size +=1
					continue
				elif check_line(line, size, listnumber) == 0:
					continue
				else:
					raise Exception("Puzzle content error.")
		if size == None or count_size != size:
			raise Exception("Puzzle error: check size and content.")
		return tuple(listnumber)
	except Exception as e:
		print("Exception:", e)
		sys.exit()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		print(check_input(sys.argv[1]))
	else:
		print("usage: python3 ./check_input file_name")
