class GameStats:
    """Sigue las estadísticas de Alien Invasión"""

    def __init__(self, ai_game):
        """Inician las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Inicia Aliens Invasión en estado inactivo.
        self.game_active = False

    def reset_stats(self):
        """Inicialización de las estadísticas que pueden cambiar durante el juego"""
        self.ships_left = self.settings.ship_limit
