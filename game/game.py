import pygame # type: ignore
from .node import Node
from .constants import *
from .algorithms import astar, idastar, rrt, dfs, bfs, iddfs, dijkstra, gbfs, bidirectional
from .mazes import dfs_maze, bfs_maze


class Game:
    def __init__(self, win: 'pygame.display'):
        self._init()
        self.win = win

    def _init(self):
        self.grid = [[Node(i,j) for j in range(COLS)] for i in range(ROWS)]
        self.start = None
        self.end = None
        self.maze = False
    
    
    def _draw_grid(self):
        for i in range(ROWS):
            pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (HEIGHT, i * SQUARE_SIZE), 4)
            for j in range(COLS):
                pygame.draw.line(self.win, BLACK, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, WIDTH), 4)
    
    def draw(self):
        self.win.fill(BLACK)
        
        for row in self.grid:
            for node in row:
                node.draw(self.win)
        
        self._draw_grid()
        pygame.display.update()
        
        
    def paint(self, x: int, y: int):
        try:
            node = self.grid[x][y]
        except IndexError:
            return
        
        if not self.start and node != self.end:
            self.start = node
            node.make_start()

        elif not self.end and node != self.start:
            self.end = node
            node.make_end()

        elif node != self.end and node != self.start:
            node.make_barrier()
        
    def erase(self, x: int, y: int):
        try:
            node = self.grid[x][y]
        except IndexError:
            return
            
        if node == self.start:
            self.start = None

        elif node == self.end:
            self.end = None
        
        node.reset()
    
    def algorithm(self, option: str):
        def update():
            for row in self.grid:
                for node in row:
                    node.update_neighbors(self.grid)

        if option == 'MAZE' and not self.maze:
            update()
            dfs_maze(self.grid, self.draw)
            self.maze = True
            
        elif self.end and self.start:
            update()
            if option == 'ASTAR':
                astar(self.draw, self.grid, self.start, self.end)
            
            elif option == 'RRT':
                rrt(self.draw, self.grid, self.start, self.end)
            
            elif option == 'DFS':
                dfs(self.draw, self.start, self.end)
            
            elif option == 'BFS':
                bfs(self.draw, self.start, self.end)
            
            elif option == 'IDDFS':
                iddfs(self.draw, self.grid, self.start, self.end, 2*len(self.grid))
            
            elif option == 'DIJKSTRA':
                dijkstra(self.draw, self.grid, self.start, self.end)
            
            elif option == 'GREEDYBFS':
                gbfs(self.draw, self.grid, self.start, self.end)

            elif option == 'BIDIRECTIONAL':
                bidirectional(self.draw, self.start, self.end)

            elif option == 'IDASTAR':
                idastar(self.draw, self.start, self.end)