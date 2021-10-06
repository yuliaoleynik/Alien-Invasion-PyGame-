class GameStats():
    """Статистика игры"""
    def __init__(self, start_game):
        self.settings = start_game.settings
        self.reset_stats()
        self.game_active = False
        self.inst_active = False

    def reset_stats(self):
        """Инициализирует статистику"""
        self.ships_left = self.settings.ship_limit