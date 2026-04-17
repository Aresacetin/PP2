from datetime import datetime
import pygame

WIDTH = 1000
HEIGHT = 1000

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
clock = pygame.time.Clock()

mickey = pygame.image.load('images/mm.png')
mickey = pygame.transform.smoothscale(mickey, (250,250))
clc = pygame.image.load('images/hours.png')
clc = pygame.transform.smoothscale(clc, (1000,1000))
cursor = pygame.image.load('images/second1.png') 
cursor_f = pygame.transform.flip(cursor, True, False) 
white = (255, 255, 255)
black = (0,0,0)



def blit_rotate_around_pivot(surf, image, pos, origin_pos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - origin_pos[0], pos[1] - origin_pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    now = datetime.now()
    second = now.second
    minute = now.minute + (second / 60.0)

    angle_seconds = -(second * 6) 
    angle_minutes = -(minute * 6)


    screen.fill(black)
    pygame.draw.circle(screen , white , (500,500) , 500)
    screen.blit(clc, (0,0))

    c_w , c_h = cursor.get_size()
    blit_rotate_around_pivot(screen,cursor,(500,500),(c_w/2,c_h),angle_seconds)
    blit_rotate_around_pivot(screen,cursor_f,(500,500),(c_w/2,c_h),angle_minutes)
    screen.blit(mickey, (500-mickey.get_height()//2,500-mickey.get_width()//2))



    



    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    

    pygame.display.flip()
    clock.tick(120)
