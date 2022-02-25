class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuraciones de estadísticas.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Configuración de balas.
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # limite de balas en el juego

        # Configuración del alien.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction de 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

