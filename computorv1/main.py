#!/usr/bin/python3
# coding: utf-8

import math
import sys
import my_dict

def ft_format(d, i):
	coef = ""
	degre = ""
	if i == 1:
		degre = "X"
	elif i > 1:
		degre = "X^" + str(i)
	
	if d[i] == 1 and degre < 1:
		coef = str(abs(d[i]))
	else:
		coef = str(abs(d[i]))
	return coef + degre

def ft_check_equation(s):
	#split str to 2 equations and del empty
	del_space = s.split()
	s = "".join(del_space)
	my_list = s.split("=")
	e1 = my_dict.ft_filter(my_list[0])
	e2 = my_dict.ft_filter(my_list[1])

	# reduce equation and del empty
	my_equation = {}
	if e1 == e2:
		print("All real numbers are solution.")
		return []
	if  e1["max"] >= e2["max"]:
		my_equation["max"] = e1["max"] 
		my_equation = my_dict.ft_reduce(e1, e2, e1["max"])
	else:
		my_equation["max"] = e2["max"] 
		my_equation = my_dict.ft_reduce(e2, e1, e2["max"])

	# print reduced equation and Polynomial degree
	i = 0
	max = my_equation["max"]
	bool_first = True
	print(f"Reduced form: ", end="")
	while i <= max:
		if i in my_equation.keys() and my_equation[i] > 0:
			if bool_first:
				print(f"{ft_format(my_equation, i)} ", end="")
				bool_first = False
			else:
				print(f"+ {ft_format(my_equation, i)} ", end="")
		elif i in my_equation.keys() and my_equation[i] < 0:
			print(f"- {ft_format(my_equation, i)} ", end="")
		i += 1
	print("= 0")
	print(f"Polynomial degree: {max}")
	return my_equation

def solve(equation):
	a = my_dict.ft_dict_value(equation, 2)
	b = my_dict.ft_dict_value(equation, 1)
	c = my_dict.ft_dict_value(equation, 0)

	# degree 1
	if a == 0:
		print("The solution is:")
		print((-c) / b)
		return

	# degree 2
	delta = b**2 - (4 * a * c)
	if delta >= 0:
		i = math.sqrt(delta)
		x1 = (-b + i) / (2 * a)
		x2 = (-b - i) / (2 * a)
		if x1 == x2:
			print("Discriminant is zero, the solution is:")
			print(x1)
		else:
			print("Discriminant is strictly positive, the two solutions are:")
			print(f"{x1:0.6f}\n{x2:0.6f}")
	else:
		i = math.sqrt(-delta)
		x1 = (-b + i) / (2 * a)
		x2 = (-b - i) / (2 * a)
		print("Discriminant is strictly negative, the two solutions are:")
		print(f"{x1:0.6f}\n{x2:0.6f}")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		equation = ft_check_equation(sys.argv[1])
		if equation:
			if equation["max"] >= 3:
				print("The polynomial degree is strictly greater than 2, I can't solve.")
			elif equation["max"] >= 1:
				solve(equation)
			elif equation["max"] <= 0:
				print("Warning: the polynomial is unsolvable!")
	elif len(sys.argv) == 3 and sys.argv[1] == "-b":
		print("bonus")
	else:
		print("usage: python3 main.py [-b] equation")
