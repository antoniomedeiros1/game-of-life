import time

import numpy as np
import pygame

TILE = 15
RES = WIDTH, HEIGTH = 1600, 900
W, H = WIDTH//TILE, HEIGTH//TILE
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

INFINIT = [[40, 18], [40, 19], [41, 18], [41, 19], [53, 15], [52, 16], [54, 16], [51, 17], [55, 17], [56, 17], [51, 18], [51, 19], [52, 20], [55, 18], [55, 19], [54, 20], [56, 20], [53, 21], [57, 18], [57, 19], [57, 20], [58, 18], [58, 19], [
    58, 21], [59, 19], [59, 21], [60, 20], [63, 17], [63, 18], [63, 22], [63, 23], [64, 17], [64, 19], [64, 21], [64, 23], [65, 18], [65, 19], [65, 20], [65, 21], [65, 22], [66, 19], [66, 20], [66, 21], [67, 20], [74, 20], [74, 21], [75, 20], [75, 21]]


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2])-cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode(RES)

    # cells = np.zeros((H, W))
    cells = np.array([[1 if not (i*j) % 17 else 0 for i in range(W)]
                     for j in range(H)])
    # cells = np.array([[1 if [i, j] in INFINIT else 0 for i in range(W)]for j in range(H)])

    screen.fill(COLOR_GRID)
    update(screen, cells, TILE)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, TILE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//TILE, pos[0]//TILE] = 1
                update(screen, cells, TILE)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, TILE, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == "__main__":
    main()
