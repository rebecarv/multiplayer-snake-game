import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, color, block_size, screen):
        super().__init__()

        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.block_size = block_size
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Spawn the food at a random position
        self.spawn()

    def spawn(self) -> None:
        """Spawns the food at a random position on the screen."""
        self.rect.x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
        self.rect.y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
