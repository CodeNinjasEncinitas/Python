import random
import time
import pygame

pygame.init()

# setup framerate
clock = pygame.time.Clock()
framerate = 60

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Airplane Game")
background_color = (130, 170, 230)  # RGB values for light blue


# Setup airplane
class Airplane():
    image = "airplane.png"
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (200, 150))
    x = 50
    y = 100
    yspeed = 0
    terminal_velocity = 5
    gravity = .5
    lift = .9
    rect = image.get_rect()
    width, height = rect.width, rect.height
    def create_mask(self):
        return pygame.mask.from_surface(self.image)

    def check_collision(self, other):
        offset = (other.x - self.x, other.y - self.y)
        return self.create_mask().overlap(other.create_mask(), offset)

airplane = Airplane()

# Setup cloud 
class Cloud():
    image = "cloud.png"
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (200, 150))
    speed = 4.0
    rect = image.get_rect()
    width = rect.width
    height = rect.height
    x = 800
    y = random.randint(0,600-height)
    def create_mask(self):
        return pygame.mask.from_surface(self.image)

    def check_collision(self, other):
        offset = (other.x - self.x, other.y - self.y)
        return self.create_mask().overlap(other.create_mask(), offset)

    

cloud = Cloud()



# Interval Timer
interval = 100
timer = interval

# setup score and its text
font = pygame.font.Font(None, 36)
score = 0
highscore = 0

running = True

while running:

    clock.tick(framerate)
    timer -= 1
    if timer == 0:
        timer = interval

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the left mouse button or other keys is being held down
    mouse_buttons = pygame.mouse.get_pressed()
    left_button_pressed = mouse_buttons[0]  # Index 0 corresponds to the left button
    keys = pygame.key.get_pressed()

    if left_button_pressed or keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
        # Do something when the left button is being held down
        airplane.yspeed -= airplane.lift

    # airplane gravity
    airplane.yspeed += airplane.gravity
    if airplane.yspeed > airplane.terminal_velocity:
        airplane.yspeed = airplane.terminal_velocity

    airplane.y += airplane.yspeed

    # airplane must stay in screen
    if airplane.y < 0:
        airplane.yspeed = 0
        airplane.y = 0
    if airplane.y > screen_height - airplane.height:
        airplane.yspeed = 0
        airplane.y = screen_height - airplane.height

    # Draw the airplane on the screen
    screen.fill(background_color)
    screen.blit(airplane.image, (airplane.x, airplane.y))

    # move and draw cloud 
    cloud.speed += .003
    cloud.x -= cloud.speed
    screen.blit(cloud.image, (cloud.x, cloud.y))
    if cloud.x < 0-cloud.width:
        cloud.x = 800
        cloud.y = random.randint(0,600-cloud.height)

    # check for collision between airplane and cloud
    collision_result = airplane.check_collision(cloud)
    if collision_result:
        print("Collision with cloud!")
        score = 0
        airplane.y = 100
        cloud.x = 800
        cloud.y = random.randint(0,600-cloud.height)
        cloud.speed = 4.0

    #score
    score += 1
    if score > highscore:
        highscore = score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    highscore_text = font.render(f"High Score: {highscore}", True, (255, 255, 255))
    screen.blit(highscore_text, (560, 10))

    pygame.display.flip()

#pygame.quit()