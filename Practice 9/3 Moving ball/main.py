import pygame

pygame.init()

WIDTH=1000
HEIGHT=1000

screen = pygame.display.set_mode((WIDTH,HEIGHT))

white = (255,255,255)
red = (255, 0, 0)

running = True

RADIUS = 25
x = 500
y = 500
movement_speed = 20

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += movement_speed
    if keys[pygame.K_LEFT]: 
        x -= movement_speed
    if keys[pygame.K_DOWN]:
        y += movement_speed
    if keys[pygame.K_UP]:
        y -= movement_speed

    if x - RADIUS < 0:
        x = RADIUS
    if x + RADIUS > WIDTH:
        x = WIDTH - RADIUS
    if y - RADIUS < 0:
        y = RADIUS
    if y + RADIUS > HEIGHT:
        y = HEIGHT - RADIUS
        
    screen.fill(white)
    pygame.draw.circle(screen , red , (x,y) , RADIUS)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()