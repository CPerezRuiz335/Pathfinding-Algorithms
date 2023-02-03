import pygame # type: ignore

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if pygame.K_c:
                return True
            if pygame.K_q:
                return True

def reconstruct_path(came_from, current, draw, stack = False):
    if not stack:
        current.make_path()
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()
    else:
        for n in list(came_from)[::-1]:
            n.make_path()
            draw()

def fill_black(grid, start, end):
    for row in grid:
        for node in row:
            if node is not start and node is not end:
                node.make_empty()

