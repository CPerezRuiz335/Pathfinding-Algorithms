"""

BUILD_RRT($q_{init},K,\Delta q$)
1 	G.init(qinit);
2 	for k = 1 to K
3 	$q_{rand} \leftarrow \;$RAND_CONF();
4 	$q_{near} \leftarrow \;$NEAREST_VERTEX(qrand,G);
5 	$q_{new} \leftarrow \;$NEW_CONF$(q_{near},\Delta q)$;
6 	G.add_vertex(qnew);
7 	G.add_edge(qnear,qnew);
8 	Return G

"""

from __future__ import annotations
import pygame # type: ignore
from random import randint
from typing import List, Tuple, Callable, Dict, NamedTuple, Set, Union
from .utils import reconstruct_path, check_quit

class Graf(NamedTuple):
    came_from: Dict[Node, Node]
    nodes: Set[Node]

clock = pygame.time.Clock()
FPS = 60

def rand_conf(grid: List[List[Node]], G: Graf, end: Node) -> Node:
    width = len(grid[0]); height = len(grid) 
    
    # Do while
    x = randint(0,width-1)
    y = randint(0,height-1)
    node = grid[x][y]
    
    while node.is_barrier() or node in G.nodes:
        x = randint(0,width-1)
        y = randint(0,height-1)
        node = grid[x][y]
    
    return grid[x][y]

def nearest_vertex(qrand: Node, otherNodes: Union[List[Node], Set[Node]]) -> List[Node]: # G is an iterable
    
    def manhattan(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)   
    
    nearest: List[Node] = []
    distance = float('inf')
    
    for node in otherNodes:
        d = manhattan(qrand.get_pos(),node.get_pos())
        if d < distance:
            distance = d
            nearest = []
            nearest.append(node)
        
        elif d == distance:
            nearest.append(node)
    
    return nearest     

def new_conf(nearest: List[Node], qrand: Node, G: Graf, draw: Callable, start: Node, end: Node) -> bool: # qrand: rand_conf
    
    def check_end(current):
        if current == end: # check end
            reconstruct_path(G.came_from, end, draw)
            current.make_end()
            return True
    
    for node in nearest:
        if node is not start:
            node.make_closed() 
        
        nearest_neighbor = nearest_vertex(qrand, node.neighbors)
        for neighbor in nearest_neighbor:
            if not neighbor in G.nodes:
                G.nodes.add(neighbor) 
                G.came_from[neighbor] = node

                if check_end(neighbor):
                    return True
                else:
                    neighbor.make_open()
            
    draw()
    clock.tick(FPS)

def rrt(draw: Callable, grid: List[List[Node]], start: Node, end: Node):
    # Pre: exists a path to the end
    G = Graf(dict(), {start})

    while True:
        if check_quit():
            return False

        random_point = rand_conf(grid, G, end)
        random_point.make_random()
        
        draw()
        clock.tick(FPS)
        
        nearest = nearest_vertex(random_point, G.nodes)
        if new_conf(nearest, random_point, G, draw, start, end): # found
            return True
        
        if random_point is end:
            random_point.make_end()
        elif not random_point.is_open():
            random_point.make_empty()
        
        draw()
        clock.tick(FPS)
