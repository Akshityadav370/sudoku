import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Define the dimensions of the window and the grid
WINDOW_SIZE = 540
GRID_SIZE = WINDOW_SIZE // 9
FPS = 30

# Sudoku board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def draw_board(screen):
    screen.fill(WHITE)
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, BLACK, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if board[i][j] != 0:
                font = pygame.font.Font(None, 40)
                text = font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE / 2, i * GRID_SIZE + GRID_SIZE / 2))
                screen.blit(text, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Sudoku Solver")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    row, col = y // GRID_SIZE, x // GRID_SIZE
                    print("Clicked cell:", row, col)  # Replace this with your logic to input numbers

        draw_board(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
