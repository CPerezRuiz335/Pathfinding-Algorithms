from __future__ import annotations
import pygame # type: ignore
from collections import deque
from random import shuffle
import time
from typing import Callable, List, Dict, Generator
from .utils import check_quit, reconstruct_path
 
def bfs(draw: Callable, start: Node, came_from: Dict[Node, Node]) -> Generator:
    queue = deque([start])
    visited = {start}
    
    while queue:
        # Check quit
        if check_quit():
            return 'Quit'
        
        # Main algorithm
        node = queue.popleft()
        if node is not start:
            node.make_closed()
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if neighbor in came_from: 
                    reconstruct_path(came_from, neighbor, draw)
                    reconstruct_path(came_from, node, draw)
                    return True 
                else:
                    yield False
                
                came_from[neighbor] = node
                
                visited.add(neighbor)
                queue.append(neighbor)
                neighbor.make_open()
        

def bidirectional(draw, start, end) -> bool:
    came_from: Dict[Node, Node] = dict()
    bfsStart = bfs(draw, start, came_from)
    bfsEnd   = bfs(draw, end, came_from)
    while True:
        try:
            s = next(bfsStart)
            e = next(bfsEnd)
            
            if s == 'Quit' or e == 'Quit':
                return False

            if s and e:
                return True
            draw()

        except StopIteration:
            return True
        
    
    
    
    
    
    
    
    
    
