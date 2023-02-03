import pygame # type: ignore
from game import *
from typing import Tuple

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

## print info
print('A: A* algorithm')
print('B: BFS algorithm')
print('C: clean board')
print('D: DFS algorithm')
print('F: Greedy Best First Search algorithm')
print('I: IDDFS algorithm')
print('J: IDA* algorithm')
print('K: Dijkstra algorithm')
print('L: Bidirectional')
print('M: create maze')
print('R: RRT algorithm')


def get_clicked_pos(pos: Tuple[int, int]) -> Tuple[int, int]:
    y, x = pos
    row = int(y / SQUARE_SIZE)
    col = int(x / SQUARE_SIZE)
    return row, col


def main():
    game = Game(WIN) 
    run = True
    
    while run:
        game.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                game.paint(row, col)
                
                
            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                game.erase(row, col)

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        run = False

                    case pygame.K_a:
                        game.algorithm('ASTAR')
                
                    case pygame.K_r:
                        game.algorithm('RRT')
                
                    case pygame.K_m:
                        game.algorithm('MAZE')
                    
                    case pygame.K_d:
                        game.algorithm('DFS')
                
                    case pygame.K_b:
                        game.algorithm('BFS')
                    
                    case pygame.K_i:
                        game.algorithm('IDDFS')
                
                    case pygame.K_k:
                        game.algorithm('DIJKSTRA')
                
                    case pygame.K_f:
                        game.algorithm('GREEDYBFS')

                    case pygame.K_l:
                        game.algorithm('BIDIRECTIONAL')

                    case pygame.K_j:
                        game.algorithm('IDASTAR')
                
                    case pygame.K_c:
                        game._init()
    
    pygame.quit()

main()
