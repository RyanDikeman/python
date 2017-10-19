from graphics import *

def square(x):
	return x * x

def distance(x1, y1,x2,y2):
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	dist = (square(x2 - x1)  + square(y2 - y1))**0.5
	return dist


def main():
	h1 = input("Input h1 :")
	k1 = input("Input k1 :")
	h2 = input("Input h2 :")
	k2 = input("Input k2 :")
	#win = GraphWin('NIGHT', 400, 400)
	#win.yUp()
	#win.setBackground("#7f7f7f")
	
	dist = distance(h1,k1,h2,k2)
	#theline = Line(Point(h1, k1), Point(h2,k2))
	
	#theline.draw(win)
	print (dist)
main()
