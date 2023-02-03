from __future__ import annotations
import pygame # type: ignore
from heapq import *
from collections import namedtuple
from typing import Tuple, List, Callable, Dict
from .utils import reconstruct_path, check_quit
Pair = namedtuple("Pair",['weight', 'node'])


def h(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)
 
def gbfs(draw: Callable, grid: List[List[Node]], start: Node, end: Node):
	 # Count, x, y for smooth rectangle
    count = 0 
    x = 1; y = 0
    
	# Set PriorityQueue and ClosedSet
    PriorityQueue: List[Node] = []; Visited = {start}
    heappush(PriorityQueue, Pair(0, start))
    
    # Previous node
    came_from: Dict[Node, Node] = dict()
    
    # Track F score 
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
        
    while PriorityQueue:
        # PYGAME
        if check_quit():
            return False
    
        # Algorithm
        weight, node = heappop(PriorityQueue)
        
        if node is end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in node.neighbors:
            f = h(neighbor.get_pos(), end.get_pos())
            if f_score[neighbor] > f:
                came_from[neighbor] = node
                f_score[neighbor] = f
                
                if not neighbor in Visited:
                    heappush(PriorityQueue, Pair(f_score[neighbor], neighbor))
                    Visited.add(neighbor)
                    neighbor.make_open()
        
        draw()

        if node is not start:
            node.make_closed()

    return False
