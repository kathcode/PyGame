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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

    # Cleare the screen
    screen.fill(WHITE)

    # Draw a green LINE on the screen from(0, 0)
    # to (100, 100) and 5 pixels thick.
    pygame.draw.line(screen, GREEN, [10, 10], [10, 200], 5)

    # Rectangle
    pygame.draw.rect(screen, BLACK, [25, 10, 100, 190], 2)

    # Elipse
    pygame.draw.ellipse(screen, RED, [25, 10, 100, 190], 2)

    # Triangle
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()
