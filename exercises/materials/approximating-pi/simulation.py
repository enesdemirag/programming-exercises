import random
import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

screen.fill(black)

def distance(x, y):
    return ((250-x)**2 + (250-y)**2)**0.5

inside = 0
total = 0

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x, y = random.randint(0, 500), random.randint(0, 500)

    if distance(x, y) < 250.5:
        pygame.draw.circle(screen, white, (x, y), 0, 0)
        inside += 1
    else:
        pygame.draw.circle(screen, blue, (x, y), 0, 0)
    total += 1

    pi = 4.0 * inside / total
    print(pi)
    pygame.display.update()