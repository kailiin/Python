#!/usr/bin/python3
# coding: utf-8

def my_abs(val):
	if val > 0:
		return val
	else:
		return -val

def my_sqrt(val):
	low = 0.
	hight = val
	mid = 0
	for _ in range(1000):
		mid = (low + hight) /2
		mid_t = mid * mid 
		if mid * mid_t == val:
			return mid
		elif mid_t > val:
			hight = mid
		else:
			low = mid
	return mid
