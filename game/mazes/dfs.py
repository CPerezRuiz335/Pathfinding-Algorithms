import pygame # type: ignore
from collections import deque
from random import shuffle

#clock = pygame.time.Clock()
#FPS = 120

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def dfs_maze(grid, draw):
    stack = deque()
    stack.append(grid[0][0])
    visited = {grid[0][0]}
    
    while stack:
        check_quit()
        node = stack.pop()
        neighbors = [node for node in node.neighbors if not node.is_barrier()]
        is_wall   = [node for node in neighbors if node in visited]
        
        if len(is_wall) <= 1: # only one neighbor closed: its father or None 
            shuffle(neighbors)
            
            for neighbor in neighbors:
                if not neighbor in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        else:
            node.make_barrier()
        
#        draw()
#        clock.tick(FPS)
