"""
path              current search path (acts like a stack)
node              current node (last node in current path)
g                 the cost to reach current node
f                 estimated cost of the cheapest path (root..node..goal)
h(node)           estimated cost of the cheapest path (node..goal)
cost(node, succ)  step cost function
is_goal(node)     goal test
successors(node)  node expanding function, expand nodes ordered by g + h(node)
ida_star(root)    return either NOT_FOUND or a pair with the best path and its cost
 
procedure ida_star(root)
    bound := h(root)
    path := [root]
    loop
        t := search(path, 0, bound)
        if t = FOUND then return (path, bound)
        if t = ∞ then return NOT_FOUND
        bound := t
    end loop
end procedure

function search(path, g, bound)
    node := path.last
    f := g + h(node)
    if f > bound then return f
    if is_goal(node) then return FOUND
    min := ∞
    for succ in successors(node) do
        if succ not in path then
            path.push(succ)
            t := search(path, g + cost(node, succ), bound)
            if t = FOUND then return FOUND
            if t < min then min := t
            path.pop()
        end if
    end for
    return min
end function
"""
from __future__ import annotations
import pygame # type: ignore
from collections import deque
from typing import Callable, Tuple, List, Union
from .utils import check_quit, reconstruct_path

def h(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def search(path: deque[Node], g: int, bound: int, start: Node, goal: Node, draw: Callable):
	node = path[-1]

	if node is not start:
		node.make_closed()
	
	if check_quit():
		return 'Quit'

	f = g + h(node.get_pos(), goal.get_pos())
	if f > bound: 
		return f
	
	if node is goal: 
		return 'FOUND'
	
	minn = float('inf')
	for succ in node.neighbors:
		if succ not in path:
			path.append(succ)
			succ.make_open()
			draw()
			t = search(path, g + 1, bound, start, goal, draw)
			if t == 'FOUND': 
				return 'FOUND'
			elif t == 'Quit':
				return 'Quit'
			
			if t < minn: 
				minn = t

			end = path.pop()
			end.make_empty()

	return minn


def idastar(draw: Callable, start: Node, end: Node) -> bool:
	bound = h(start.get_pos(), end.get_pos())
	path = deque([start])
	while True:
		t = search(path, 0, bound, start, end, draw)
		if t == 'Quit': 
			return False

		if t == 'FOUND': 
			reconstruct_path(path, path[-1], draw, True)
			end.make_end()
			draw()
			return True

		if t == float('inf'): 
			return False
		
		bound = t 










