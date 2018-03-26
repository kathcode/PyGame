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
# Dictionary of events
events = {
    pygame.QUIT: "The user requested to leave.",
    pygame.KEYDOWN: "The user pressed a key.",
    pygame.KEYUP: "The user released a key.",
    pygame.MOUSEBUTTONDOWN: "The user pressed a mouse button"
}
while not close_window:
    for event in pygame.event.get():
        # If the event is in the event dictionary
        if event.type in events:
            # Print the message
            print(events[event.type])
            # Close
            if event.type == pygame.QUIT:
                close_window = True

    # Cleare the screen
    screen.fill(WHITE)

    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()
