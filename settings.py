import pygame
from pygame import mixer

pygame.init()
mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Galactic War: Lunar Capture')

clock = pygame.time.Clock()
FPS = 60

GRAVITY = 0.45
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 3
screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
start_intro = False

moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

# load music and sounds
# pygame.mixer.music.load('audio/music2.mp3')
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1, 0.0, 5000)
jump_fx = pygame.mixer.Sound('audio/jump.wav')
jump_fx.set_volume(0.05)
shot_fx = pygame.mixer.Sound('audio/shot.wav')
shot_fx.set_volume(0.05)
grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
grenade_fx.set_volume(0.05)

start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()
restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()

pine1_img = pygame.image.load('img/Background/pine1.png').convert_alpha()
pine1_img = pygame.transform.scale(pine1_img, (500, 600))

mountain_img = pygame.image.load('img/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/Background/sky_cloud.png').convert_alpha()
sky_img = pygame.transform.scale(sky_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
main_img = pygame.image.load('img/main.png')
main_img = pygame.transform.scale(main_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
end_img = pygame.image.load('img/main.png')
end_img = pygame.transform.scale(end_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tile/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()

grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()

health_box_img = pygame.image.load('img/icons/health_box.png').convert_alpha()
ammo_box_img = pygame.image.load('img/icons/ammo_box.png').convert_alpha()
grenade_box_img = pygame.image.load('img/icons/grenade_box.png').convert_alpha()
item_boxes = {
    'Health': health_box_img,
    'Ammo': ammo_box_img,
    'Grenade': grenade_box_img
}

BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)

font = pygame.font.SysFont('Futura', 30)
