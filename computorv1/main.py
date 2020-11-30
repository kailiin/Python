#!/usr/bin/python3
# coding: utf-8

import math
import sys

def ft_del_null(corrent=[]):
	corrent.reverse()
	while corrent and corrent[0] == 0:
		del corrent[0]
	corrent.reverse()
	return corrent

def ft_filter(s):
	ele = []
	start = 0
	add = s.find("+")
	while add != -1:
		ele.append(s[start:add])
		start = add
		add = s.find("+", add+1)
	ele.append(s[start:])

	final = []
	for e in ele:
		start = 0
		sub = e.find("-")
		while sub != -1:
			final.append(e[start:sub])
			start = sub
			sub = e.find("-", sub+1)
		final.append(e[start:])

	info = []
	for e in final:
		split = e.split("*X^")
		try:
			info.append(int(split[0]))
		except Exception:
			info.append(float(split[0]))
	return ft_del_null(info)

def ft_reduce(e1,e2):
	my_equation = []
	for i in range(len(e1)):
		if i < len(e2):
			my_equation.append(e1[i] - e2[i])
		else:
			my_equation.append(e1[i])
	return ft_del_null(my_equation)

def ft_check_equation(s):
	del_space = s.split()
	s = "".join(del_space)
	my_list = s.split("=")
	f1 = ft_filter(my_list[0])
	f2 = ft_filter(my_list[1])

	my_equation = []
	if f1 == f2:
		print("All real numbers are solution.")
		return []
	if len(f1) >= len(f2):
		my_equation = ft_reduce(f1, f2)
	else:
		my_equation = ft_reduce(f2, f1)
	
	for i in range(len(my_equation)):
		if i == 0:
			print(f"Reduced form: {my_equation[i]} * X^{i} ", end="")
		elif my_equation[i] >= 0:
			print(f"+ {my_equation[i]} * X^{i} ", end="")
		else:
			print(f"- {abs(my_equation[i])} * X^{i} ", end="")
	print("= 0")
	print(f"Polynomial degree: {len(my_equation) - 1}")
	return my_equation

def solve(c, b, a):
	if a == 0:
		print("The solution is:")
		print((-c) / b)
		return

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
		l = []
		equation = ft_check_equation(sys.argv[1])
		if len(equation) > 3:
			print("The polynomial degree is strictly greater than 2, I can't solve.")
		elif len(equation) == 3:
			solve(equation[0], equation[1], equation[2])
		elif len(equation) == 2:
			solve(equation[0], equation[1], 0)
		elif len(equation) == 1:
			print("Warning: the polynomial is unsolvable!")
	else:
		print("usage: python3 main.py equation")
