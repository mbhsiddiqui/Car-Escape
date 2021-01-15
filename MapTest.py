from Map import Map
import pygame, random, sys


pygame.init()

screen = pygame.display.set_mode([500,500])

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

map1 = Map(6, 6)
print(map1.getPath(5, 5, 4, 1))
print(map1.findPath(input(), False))
