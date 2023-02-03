from __future__ import annotations
import pygame # type: ignore
from collections import deque, namedtuple
from random import shuffle
from typing import List, Callable, Dict, Set
from .utils import check_quit, reconstruct_path, fill_black

nodeDist  = namedtuple("nodeDist", ["node", "dist"])

def iddfs(draw: Callable, grid: List[List[Node]], start: Node, end: Node, maxDepth: int = 80) -> bool:
    
    def ids(depth):
        
        s = deque([nodeDist(start, depth)])
        visited.add(start)

        while s:
            node, nodeDepth = s.pop()
            if nodeDepth == 0: 
                continue
            
            if check_quit():
                return 'Quit'

            if node is not start: 
                node.make_closed()

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    came_from[neighbor] = node
                    s.append(nodeDist(neighbor, nodeDepth-1))
                    neighbor.make_open()
                    visited.add(neighbor)
                    draw()

                elif neighbor is end:
                    reconstruct_path(came_from, neighbor, draw)
                    end.make_end()
                    return True

        return False
            
    for depth in range(maxDepth):
        fill_black(grid, start, end)
        came_from: Dict[Node, Node] = dict()
        visited: Set[Node] = set()
        retval = ids(depth)
        if retval:
            return True
        elif retval == 'Quit':
            False


