from pygame import *

class GameSprite(sprite.Sprite):
    ''' constructor ''' 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self, win_obj):
        self.win_obj = win_obj
        self.win_obj.blit(self.image, (self.rect.x, self.rect.y))

