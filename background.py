import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, player, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("image/Background1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.screen = screen
        self.player = player
        self.speed_x = 5

    def update(self):
        # Если персонаж сдвинулся на правую половину экрана, начинаем двигать фон влево
        if self.player.rect.right > self.screen.get_width() // 2:
            self.speed_x = -self.player.speed_x
        else:
            self.speed_x = 0

        # Обновляем позицию фона
        self.rect.x += self.speed_x

        # Если фон полностью вышел за границы экрана, сдвигаем его в начальную позицию
        if self.rect.right < 0:
            self.rect.left = 0