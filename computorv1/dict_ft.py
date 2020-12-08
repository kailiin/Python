#!/usr/bin/python3
# coding: utf-8

import re

# return dict[key] value
# return 0 if not key in dict
def ft_dict_value(d, k):
	if k in d.keys():
		return d[k]
	else:
		return 0

# del dict empty value, set new max(degree)
def ft_del_empty(corrent={}):	
	i = corrent["max"]
	max = 0
	while i >= 0:
		if i in corrent.keys():
			if corrent[i] == 0:
				del corrent[i]
			else:
				if i > max :
					max = i
		i -= 1
	corrent["max"] = max
	return corrent

# add dict[degre, coef]
def ft_append(coef, degre, d):
	if degre in d.keys():
		d[degre] += float(coef)
	else:
		d[degre] = (float(coef))

def ft_find_coef(e):
	if e.find("X") >= 0:
		split = e.split("X")
		if split[0].find("*") >= 0:
			return split[0][0:split[0].find("*")]
		elif len(split[0]) == 1:
			if split[0].find("+") == 0 or split[0].find("-") == 0:
				return split[0] + "1"
			else:
				return split[0]
		elif len(split[0]) == 0:
			return "1"
		else:
			return split[0]
	else:
		return e

def ft_find_degre(e):
	if e.find("X") >= 0:
		split = e.split("X")
		if split[1].find("^") >= 0:
			return split[1][split[0].find("^"): ]
		else:
			return "1"
	else:
		return "0"

# str split "+" and "-" => list [a ∗ x^p]
# for ele in list: check regex 
# with ft_find_coef and ft_find_degre => get coef and degree
# result: dict[p] = a, a: coef p: degre
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

	if len(final) == 0:
		raise Exception("Error input, equation empty")

	info = {}
	info["max"] = 0
	# ^ [\+|-])?  ([0-9]+(.[0-9]+)?)?  ( (\*X\^|X\^)([0-9]+) |  (\*X|X) )?   $ 
	reg = "(^[\+|-])?([0-9]+(.[0-9]+)?)?((\*X\^|X\^)([0-9]+)|(\*X|X))?$"
	error_reg = "^(\+|-)$"
	for e in final:
		if e:
			search = re.match(reg, e)
			# print("e:",e)
			# print(search) # else = None
			error_s = re.match(error_reg, e)
			# print("errors:", error_s)
			if search == None or error_s:
				raise Exception("Error input, lexical errors or syntactic errors.")
			coef = ft_find_coef(e)
			degre = int(ft_find_degre(e))
			if degre > info["max"]:
				info["max"] = degre
			ft_append(coef, degre, info)
	return ft_del_empty(info)

# e = e1 - e2, and del empty
def ft_reduce(e1, e2, max):
	my_equation = {}
	my_equation["max"] = max
	i = max
	while i >= 0:
		if i in e1.keys() and i in e2.keys():
			my_equation[i] = e1[i] - e2[i]
		elif i in e1.keys() and not(i in e2.keys()):
			my_equation[i] = e1[i]
		elif not(i in e1.keys()) and i in e2.keys():
			my_equation[i] = 0 - e2[i]
		i -= 1
	return ft_del_empty(my_equation)
