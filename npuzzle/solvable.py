#!/usr/bin/python3
# coding: utf-8

import math 

# Wiki Fr: La parité de la case vide étant identique à la parité de la permutation, la résolution est possible.
# ex: (empty_parity % 2) == (permutation_parity % 2) si tout les 2 paire ou tout les 2 impaire
#  empty_parity  = nombre de movement pour aller de la case Vide initial à la case Vide final (0) dans notre cas
#  permutation_parity = movement total pour atteimdre le taquin final (en echanger directement les cases)

def check_solvable(b=(), final_b=()):
	side = int(math.sqrt(len(b)))
	empty_parity = abs(final_b.index(0) % side - b.index(0) % side) + abs(int(final_b.index(0) / side) - int(b.index(0) / side))
	permutation_parity = 0
	copy = list(b)
	for i in range(len(copy)):
		if copy[i] != final_b[i]:
			index = copy.index(final_b[i])
			copy[index] = copy[i]
			copy[i] = final_b[i]
			permutation_parity += 1
	if (empty_parity % 2) == (permutation_parity % 2):
		return True
	return False
