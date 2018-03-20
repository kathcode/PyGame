# CLOSE THE WINDOW

# Import the pygame library
import pygame

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
    for event in pygame.event.get(): # Listen event from the user
        if event.type == pygame.QUIT: # User click on close button
            close_window = True # Close window

    # Limited to 20 frames per second
    clock.tick(20)