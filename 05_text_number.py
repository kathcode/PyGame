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
dimensions = (600, 300)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("Kath learning pygame")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# Select the font and size
font = pygame.font.Font(None, 25)

# The text, if it's softened, color
text = font.render("Kath learning pygame", True, RED)

number = font.render(" - " + str(25032018), True, BLACK)
# ---------- Main Loop of the Program ----------
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

    # Cleare the screen
    screen.fill(WHITE)

    # ---------- HERE GOES THE CODE ----------

    # Set the text in the screen
    screen.blit(text, [180, 10])

    # Add number
    screen.blit(number, [360, 10])

    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()
