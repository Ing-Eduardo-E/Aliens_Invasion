import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave en funcion de la bandera de movimiento"""
        if self.moving_right:
            self.rect.x +=1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)

