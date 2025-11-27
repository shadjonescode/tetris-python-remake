import pygame
import sys

# Initialize Pygame
pygame.init()

# Grid settings
COLS = 10
ROWS = 20
BLOCK_SIZE = 30   # Each cell is 30x30 pixels

# Window settings
WINDOW_WIDTH = COLS * BLOCK_SIZE
WINDOW_HEIGHT = ROWS * BLOCK_SIZE
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris Remake")

def create_board():
    # 0 will mean "Empty" cells for now
    board = []
    for _ in range(ROWS):
        row = [0] * COLS
        board.append(row)
    return board

def draw_board(surface, board):
    # Fill the screen black first
    surface.fill((0, 0, 0))

    # Loop over every cell and draw a square outline
    for row in range(ROWS):
        for col in range(COLS):
            x = col * BLOCK_SIZE
            y = row * BLOCK_SIZE
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, (40, 40, 40), rect, 1)   # 1 = outline

piece_shape = [(0,0), (1,0), (2,0), (3,0)]
piece_row = 0
piece_col = 3
piece_color = (0, 255, 255)    # Light blue color

def draw_piece(surface, shape, row, col, color):
    for cell_row, cell_col in shape:
        # 1. Combine piece posistion with cell offset
        actual_row = row + cell_row
        actual_col = col + cell_col

        # 2. convert board cell to pixel coordinates
        x = actual_row * BLOCK_SIZE
        y = actual_col * BLOCK_SIZE

        # 3. Make a rectangle at that spot
        rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

        # 4. Draw the filled block
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (40, 40, 40), rect, 1)

# Set up the clock for frame rate
clock = pygame.time.Clock()

# Create the board (2D grid of 0s)
board = create_board()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board (grid)
    draw_board(WINDOW, board)

    # Draw the current piece
    draw_piece(WINDOW, piece_shape, piece_row, piece_col, piece_color)

    # Update the display
    pygame.display.update()

    # Control frame rate (60 FPS)
    clock.tick(60)

pygame.quit()
sys.exit()
