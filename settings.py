class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Inicializa las configuraciones estáticas del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuración de la nave.
        self.ship_limit = 3

        # Configuración de balas.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 # limite de balas en el juego

        # Configuración del alien.
        self.fleet_drop_speed = 10

        # Rápidez con la que se acelera el juego.
        self.speedup_scale = 1.1

        # lo rápido que aumenta el valor en puntos de los aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa las configuraciones que cambian durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        # fleet_direction de 1 representa la derecha; -1 representa la izquierda.
        self.fleet_direction = 1

        # Puntuación.
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta las configuraciones de velocidad y los valores en puntos de los aliens."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)