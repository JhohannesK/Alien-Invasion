import sys
import pygame


class AlienInvasion:
    """The class to manage all game assets and behaviour."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
