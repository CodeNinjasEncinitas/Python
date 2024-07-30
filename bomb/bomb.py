import pygame
import sys
import time
import random

# Set up the "game" window
pygame.init()
width, height = 600, 600
window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Black Square on White Window")

# set up text font
font_size = 72
font = pygame.font.Font(None, font_size)  # None for default font

# set up audio
pygame.mixer.init()
sounds = [
    pygame.mixer.Sound('sounds/1.wav'),
    pygame.mixer.Sound('sounds/2.wav'),
    pygame.mixer.Sound('sounds/3.wav'),
    pygame.mixer.Sound('sounds/4.wav'),
    pygame.mixer.Sound('sounds/5.wav'),
    pygame.mixer.Sound('sounds/6.wav'),
    pygame.mixer.Sound('sounds/7.wav'),
    pygame.mixer.Sound('sounds/8.wav'),
    pygame.mixer.Sound('sounds/9.wav'),
    pygame.mixer.Sound('sounds/10.wav'),
    pygame.mixer.Sound('sounds/11.wav')
]

# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    total_time = 3

    for i in range(0, total_time):
        t = total_time - i
        text_surface = font.render("Loading " + str(t), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (200, 100)
        window.fill((0, 0, 0)) # make screen black
        window.blit(text_surface, text_rect) # add white text
        pygame.display.flip() # update screen to show what we did the last 2 lines
        time.sleep(1)

    while running:
        # random sound
        sounds[random.randint(0,10)].play()
        #pygame.time.wait(int(sounds[1].get_length() * 1000))
        #random screen color
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        window.fill((r, g, b)) # make screen black
        # random text
        text = "you been hacked!!!1!11!!"
        text_surface = font.render(text, True, (255-r, 255-g, 255-b))
        text_rect = text_surface.get_rect()
        text_rect.center = (random.randint(-100,width), random.randint(-100,height))
        window.blit(text_surface, text_rect) 
        #update screen
        pygame.display.flip()
    
    running = False

pygame.quit()
sys.exit()