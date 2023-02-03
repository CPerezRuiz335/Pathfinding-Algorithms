from __future__ import annotations
import pygame # type: ignore
from heapq import * 
from collections import namedtuple
from typing import Callable, List
from .utils import reconstruct_path, check_quit

Pair = namedtuple("Pair",['weight', 'node'])

def dijkstra(draw: Callable, grid: List[List[Node]], start: Node, end: Node) -> bool:
	# Set PriorityQueue and ClosedSet
    PriorityQueue: List[Node] = []
    heappush(PriorityQueue, Pair(0, start))
    
    # Previous node
    came_from: Dict[Node, Node] = dict()
    
    # Track F score 
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = 0
        
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
        
        if weight <= f_score[node]:
            for neighbor in node.neighbors:
                nw = f_score[neighbor]
                if nw > f_score[node] + 1:
                    came_from[neighbor] = node
                    f_score[neighbor] = f_score[node] + 1
                    heappush(PriorityQueue, Pair(f_score[neighbor], neighbor))
                    neighbor.make_open()
            
        draw()

        if node is not start:
            node.make_closed()

    return False
