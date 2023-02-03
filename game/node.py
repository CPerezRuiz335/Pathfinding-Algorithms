import pygame # type: ignore
from typing import List, Tuple
from .constants import *


class Node:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.color = BLACK
        self.neighbors: List[Node] = []

    def get_pos(self) -> Tuple[int, int]:
        return self.row, self.col
    
    def is_empty(self):
        return self.color == BLACK
    
    def is_random(self):
        return self.color == WHITE
    
    def is_maze_path(self):
        return self.color == BROWN
    
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == GREY

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN
    
    def make_maze_path(self):
        self.color = BROWN
        
    def make_barrier(self):
        self.color = GREY

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE
    
    def make_random(self):
        self.color = WHITE
    
    def make_empty(self):
        self.color = BLACK

    def draw(self, win: 'pygame.display'):
        pygame.draw.rect(win, self.color, (self.x, self.y,SQUARE_SIZE, SQUARE_SIZE))

    def update_neighbors(self, grid: List[List['Node']]):
        
        self.neighbors = []
        # DOWN
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_barrier(): # LOWER LIMIT & BARRIER
            self.neighbors.append(grid[self.row + 1][self.col])
        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UPPER LIMIT & BARRIER
            self.neighbors.append(grid[self.row - 1][self.col])
        # RIGHT
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT LIMIT & BARRIER
            self.neighbors.append(grid[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT LIMIT & BARRIER
            self.neighbors.append(grid[self.row][self.col - 1])
    
    # Dunder methods
    def __lt__(self, other):
        return False
   
    def __gt__(self, other):
        return False
        
    def __repr__(self):
        return f"{(self.col, self.row)}"
    
    def __hash__(self):
        return hash((self.row, self.col))

