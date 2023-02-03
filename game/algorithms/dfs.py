from __future__ import annotations
import pygame # type: ignore
from collections import deque
from random import shuffle
from typing import Callable, List, Dict
from .utils import reconstruct_path, check_quit

def dfs(draw: Callable, start: Node, end: Node) -> bool:
    stack = deque([start])
    visited = {start}
    came_from: Dict[Node, Node] = dict()
    
    while stack:
        # Check quit
        if check_quit():
            return False
        
        # Main algorithm
        node = stack.pop()
        if node is not start:
            node.make_closed()
        
        neighbors = node.neighbors
        shuffle(neighbors) # add some randomness
        
        for neighbor in neighbors:
            if neighbor not in visited:
                came_from[neighbor] = node
                
                if neighbor is end: # check end
                    reconstruct_path(came_from, end, draw)
                    end.make_end()
                    return True 
                
                visited.add(neighbor)
                stack.append(neighbor)
                
                neighbor.make_open()

        draw()
