#!/usr/bin/python3
# coding: utf-8

import sys
import dict_ft
import my_math

# if float => last char is '0'or '.'=> remove
def trim_value(s:str):
	while s.find('.') != -1:
		if s[-1] == '0' or s[-1] == '.':
			s = s[:-1]
		else:
			break
	return s

#  print complex solution
def print_complex(v1, v2, nb_sqrt):
	s1 = trim_value(str(v1))
	s2 = trim_value(str(v2))
	sqrt = trim_value(str(my_math.my_round(nb_sqrt, 6)))
	print(f"({s1} + i * {sqrt}) / {s2}")
	print(f"({s1} - i * {sqrt}) / {s2}")

# with coef and degre return format ex: format(5, 2) -> 5X^2
def format(d, i):
	coef = ""
	degre = ""
	if i == 1:
		degre = "X"
	elif i > 1:
		degre = "X^" + str(i)
	if d[i] != 0:
		coef = str(my_math.my_abs(d[i]))
		coef = trim_value(coef)
	return coef + degre

def check_equation(s):
	#split str to 2 equations and del empty
	del_space = s.split()
	s = "".join(del_space)
	my_list = s.split("=")
	if len(my_list) != 2 or (not my_list[0]) or not(my_list[1]):
		raise Exception("Error input!")
	e1 = dict_ft.ft_filter(my_list[0])
	e2 = dict_ft.ft_filter(my_list[1])

	# reduce equation and del empty
	my_equation = {}
	if e1 == e2:
		print("All real numbers are solution.")
		return []
	if  e1["max"] >= e2["max"]:
		my_equation["max"] = e1["max"] 
		my_equation = dict_ft.ft_reduce(e1, e2, e1["max"])
	else:
		my_equation["max"] = e2["max"] 
		my_equation = dict_ft.ft_reduce(e2, e1, e2["max"])

	# print reduced equation and Polynomial degree
	i = 0
	max = my_equation["max"]
	bool_first = True
	print("Reduced form: ", end="")
	while i <= max:
		if i in my_equation.keys() and my_equation[i] > 0:
			if bool_first:
				print(f"{format(my_equation, i)} ", end="")
				bool_first = False
			else:
				print(f"+ {format(my_equation, i)} ", end="")
		elif i in my_equation.keys() and my_equation[i] < 0:
			print(f"- {format(my_equation, i)} ", end="")
			bool_first = False
		i += 1
	print("= 0")
	print(f"Polynomial degree: {max}")
	return my_equation

def solve(equation):
	a = dict_ft.ft_dict_value(equation, 2)
	b = dict_ft.ft_dict_value(equation, 1)
	c = dict_ft.ft_dict_value(equation, 0)

	# degree 1
	if a == 0:
		print("The solution is:")
		result = my_math.my_round((-c) / b, 6)
		print(trim_value(result))
		return

	# degree 2  (b*b = b^2)  => b^2 - 4ac
	delta = (b*b) - (4 * a * c)
	if delta == 0:
		result = -b / (2*a)
		print("Discriminant is zero, the solution is:")
		print(trim_value(my_math.my_round(result, 6)))
	elif delta > 0:
		sqrt = my_math.my_sqrt(delta)
		x1 = (-b + sqrt) / (2 * a)
		x2 = (-b - sqrt) / (2 * a)
		print("Discriminant is strictly positive, the two solutions are:")
		print(trim_value(my_math.my_round(x1, 6)))
		print(trim_value(my_math.my_round(x2, 6)))
	else:
		sqrt = my_math.my_sqrt(my_math.my_abs(delta))
		# x1 = (-b + sqrt) / (2 * a)
		# x2 = (-b - sqrt) / (2 * a)
		print("Discriminant is strictly negative, the two complex solutions are:")
		print_complex(-b, 2*a, sqrt)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		try:
			equation = check_equation(sys.argv[1])
		except Exception as e:
			print("Exception:", e)
			sys.exit()
		if equation:
			if equation["max"] >= 3:
				print("The polynomial degree is strictly greater than 2, I can't solve.")
			elif equation["max"] >= 1:
				solve(equation)
			elif equation["max"] <= 0:
				print("Warning: the polynomial is unsolvable!")
	else:
		print("usage: python3 main.py equation")

# bonus: input((lexique et syntaxe)
#		forme naturelle / input l'ordre / doublon
