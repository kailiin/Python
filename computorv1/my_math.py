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
		if mid_t == val:	
			return mid
		elif mid_t > val:
			hight = mid
		else:
			low = mid
	return mid

# 0.12345678 => 0.123457   
# -0.1234567 => -0.123457
def my_round(val, ndigit):
	s = str(val)
	f = s.find('.')
	if f != -1 and len(s) > f + ndigit + 1:
		if s[f+ndigit+1] >= '5':
			if val >= 0:
				s = str(val + 0.000001)
			else:
				s = str(val - 0.000001)
		s = s[:f + ndigit + 1]
	return s

