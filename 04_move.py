# Import the pygame library
import pygame
import math

# Initialize the game engine
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensions
dimensions = (700, 500)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("Kath learning pygame")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# ---------- Main Loop of the Program ----------

while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

    # Cleare the screen
    screen.fill(WHITE)

    for i in range(200):
        radianes_x = i / 20
        radianes_y = i / 6

        x = int(75 * math.sin(radianes_x)) + 200
        y = int(75 * math.cos(radianes_y)) + 200

        pygame.draw.line(screen, RED, [x, y], [x + 5, y], 5)

    for desplazamiento_x in range(30, 300, 30):
        pygame.draw.line(screen, GREEN, [desplazamiento_x, 100], [desplazamiento_x - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [desplazamiento_x, 90], [desplazamiento_x - 10, 100], 2)

    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()
