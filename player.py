import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        # Загружаем изображение
        self.images = [
            pygame.image.load("image/Wlak.player/WALK1.png").convert_alpha(),
            pygame.image.load("image/Wlak.player/WALKRIGHT.png"),
            pygame.image.load("image/Wlak.player/WALK2LEFT.png").convert_alpha(),
            pygame.image.load("image/Wlak.player/SED1.png"),
        ]
        self.image = self.images[0] # Указываем какое изобраение будет стоять первым
        self.rect = self.image.get_rect()

        # Назначаем скорость и корды персонажу
        self.rect.x = 50
        self.rect.y = screen.get_height() - self.rect.height - 50
        self.speed_x = 0
        self.speed_y = 0
        self.screen = screen

        # Направление движение спрайта
        self.direction = 'idle'

        self.jump_height = 100  # Высота прыжка
        self.jump_speed = 10    # Скорость прыжка
        self.is_jumping = False # Флаг прыжка

        self.gravity = 5

# Функция обноления движений персонажа
    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.speed_y = self.gravity

        if self.speed_y > 10:
            self.speed_y = 10

        if self.is_jumping:
            if self.jump_height > 0 and self.jump_height <= 100:
                self.speed_y = -self.jump_speed
                self.jump_height -= self.jump_speed
            else:
                self.is_jumping = False
                self.jump_height = 0

        if self.speed_x > 0:
            self.image = self.images[1]
            self.direction = 'right'
        elif self.speed_x < 0:
            self.image = self.images[2]
            self.direction = 'left'
        else:
            self.image = self.images[0]
            self.direction = 'idle'



# Функция управления на клавиши
    def handle_event(self, screen):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.jump_height = 100

        if keys[pygame.K_a]:
            self.speed_x = -1
            self.direction = 'left'
        elif keys[pygame.K_d]:
            self.speed_x = 1
            self.direction = 'right'
        else:
            self.speed_x = 0
            self.speed_y = 0

