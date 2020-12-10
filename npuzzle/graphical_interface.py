#!/usr/bin/python3
# coding: utf-8

from tkinter import Tk, Label
import my_dict

def modif_graph(list_label, new_content):
	for i in range(len(new_content)):
		if new_content[i] == 0 :
			txt = " "
		else:
			txt = new_content[i]
		list_label[i]["text"] = txt


def init_result(list_result, side):
	root = Tk()
	root.title('N-Puzzle')
	list_label = []
	l = list_result[0]
	max = len(list_result) - 1
	label_i = Label(text="Cost: 0 / "+ str(max), borderwidth=1)
	label_i.grid(row = 0, columnspan = side)
	for i in range(len(l)):
		if l[i] == 0 :
			txt = " "
		else:
			txt = l[i]
		list_label.append(Label(text=txt, width=8, height=5, borderwidth=1, relief="solid"))
		list_label[i].grid(row = int(i / side) + 1, column= int(i % side))
	
	def move(event):
		key = event.keysym
		nonlocal l
		i = list_result.index(l)
		if key == "Escape":
			root.destroy()
			return
		if (key == "Down" or key == "Right") and i < max:
			i += 1
			l = list_result[i]
			label_i["text"] = "Cost: " + str(i) + " / " + str(max)
			modif_graph(list_label, l)
		elif (key == "Up" or key == "Left") and i > 0:
			i -= 1
			l = list_result[i]
			label_i["text"] = "Cost: " + str(i) + " / " + str(max)
			modif_graph(list_label, l)

	root.focus_set()
	root.bind("<Key>", move)
	root.mainloop()


def swap_val(l, x, y, c, label_i):
	tmp = l[x]
	l[x] = l[y]
	l[y] = tmp
	label_i["text"] = "Cost: " + str(c)

def init_play(l, side):
	root = Tk()
	root.title('N-Puzzle')
	list_label = []
	cost = 0
	label_i = Label(text="Cost: 0")
	label_i.grid(row = 0, columnspan = side)
	for i in range(len(l)):
		if l[i] == 0 :
			txt = " "
		else:
			txt = l[i]
		list_label.append(Label(text=txt, width=8, height=5, borderwidth=1, relief="solid"))
		list_label[i].grid(row = int(i / side) + 1, column= int(i % side))

	def move(event):
		key = event.keysym
		i = l.index(0)
		nonlocal cost
		if key == "Escape":
			root.destroy()
			return
		if l != final:
			if key == "Down" and i / side >= 1:
				cost += 1
				swap_val(l, i, i - side, cost, label_i)
				modif_graph(list_label, l)
			elif key == "Up" and i / side < side - 1:
				cost += 1
				swap_val(l, i, i + side, cost, label_i)
				modif_graph(list_label, l)
			elif key == "Right" and i % side > 0:
				cost += 1
				swap_val(l, i, i - 1, cost, label_i)
				modif_graph(list_label, l)
			elif key == "Left" and i % side + 1 < side:
				cost += 1
				swap_val(l, i, i + 1, cost, label_i)
				modif_graph(list_label, l)
			if l == final:
				print("GG!")

	final = list(my_dict.final_dict[side])
	root.focus_set()
	root.bind("<Key>", move)
	root.mainloop()


if __name__ == "__main__":
	l = [1,2,3, 8,4,5, 7,6,0]
	init_play(l, 3)
