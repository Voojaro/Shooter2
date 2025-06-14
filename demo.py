from pygame import *
from random import randint

#background music
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')


# we need these pictures:
img_back = "galaxy.jpg" # game background
img_hero = "rocket.png" # character

# parent class for other sprites
class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)

        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# main player class
class Player(GameSprite):
    # method for controlling the sprite with keyboard arrows
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
  # the "fire" method (use the player's place to create a bullet there)
    def fire(self):
        pass

lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed   
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(40, 620)
            self.rect.y = 5
            lost += 1

# Create the window
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# create sprites
ship = Player(img_hero, 5, win_height - 60, 60, 60, 10)

enemies = sprite.Group()
for i in range(10):
    enemy = Enemy(player_image='ufo.png', 
                    player_x=randint(40, 620), 
                    player_y= 5, 
                    size_x= 80,
                    size_y= 50,
                    player_speed= randint(1, 5) )
    enemies.add(enemy)

# working font/text
font.init()
style = font.Font(None, 30)


# the "game over" variable: as soon as it is True, the sprites stop working in the main loop
finish = False
# Main game loop:
run = True # the flag is cleared with the close window button
while run:
    # the press the Close button event
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        # refresh background
        window.blit(background,(0,0))

        text_win = style.render('Scores: ', 1, (255, 255, 255))
        window.blit(text_win, (10, 5) )

        text_lose = style.render('Missed: ' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 35) )
        
        # producing sprite movements
        ship.update()
        enemies.update()

        # updating them at a new location on each iteration of the loop
        ship.reset()

        # sprite groups
        enemies.draw(window)

        display.update()


    # the loop runs every 0.05 seconds
    time.delay(50)