import pygame

from player import Player
from background import Background
from ground import Ground

# Метод инит, указание рамок, FPS локер
pygame.init()
screen_width = (1280)
screen_height = (720)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Цвет
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (124, 10, 2)

# Кнопки
quit_button_rect = pygame.Rect(600, 10, 100, 30)
quit_button_color = (RED)
font = pygame.font.Font(None, 25)
quit_button_text = font.render("Выход", True, (WHITE))

all_sprites = pygame.sprite.Group()

player = Player(screen)

ground = Ground(0, 600, screen_width, 120, (34, 139, 34))

background = Background(screen, player, screen_width, screen_height)

all_sprites.add(background)
all_sprites.add(ground)
all_sprites.add(player)

running = True
while running:
    screen.fill((WHITE))

    # Добавление кнопки выхода, вместо нажатия на крести
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if quit_button_rect.collidepoint(event.pos):
                running = False
        if event.type == pygame.QUIT:
            running = False

    screen.fill((WHITE))

    background.update()
    all_sprites.update()

    player.update()

    player.handle_event(screen)

    all_sprites.draw(screen)
    pygame.draw.rect(screen, quit_button_color, quit_button_rect)
    screen.blit(quit_button_text, (quit_button_rect.x + quit_button_rect.width / 2 - quit_button_text.get_width() / 2, quit_button_rect.y + quit_button_rect.height / 2 - quit_button_text.get_height() / 2))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
