from __future__ import annotations
import pygame # type: ignore
from heapq import *
from collections import namedtuple
from typing import Tuple, List, Callable, Dict
from .utils import reconstruct_path, check_quit

Trio = namedtuple("Trio",['weight', 'count', 'node'])

def h(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def astar(draw: Callable, grid: List[List[Node]], start: Node, end: Node) -> bool:
	 # Count, x, y for smooth rectangle
    count = 0 
    x = 1; y = 0
    
	# Set PriorityQueue and ClosedSet
    PriorityQueue: List[Trio] = [] 
    Visited = {start}
    heappush(PriorityQueue, Trio(0, count, start))
    
    # Previous node
    came_from: Dict[Node, Node] = dict()
    
    # Track G score
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    # Track F score 
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
        
   
    while PriorityQueue:
        # PYGAME
        if check_quit(): 
            return False
    
        # Algorithm
        weight, c, node = heappop(PriorityQueue)
        
        if node is end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in node.neighbors:
            g = g_score[node] + x
            if g_score[neighbor] > g:
                came_from[neighbor] = node
                g_score[neighbor] = g
                f_score[neighbor] = g + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in Visited:
                    count += y
                    heappush(PriorityQueue, Trio(f_score[neighbor], count, neighbor))
                    Visited.add(neighbor)
                    neighbor.make_open()
        
        draw()

        if node is not start:
            node.make_closed()

    return False
