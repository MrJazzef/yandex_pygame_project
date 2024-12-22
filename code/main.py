import pygame
import sys
from scenes import *

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Block Blast")
        self.screen = pygame.display.set_mode(SIZE)
        self.surf = pygame.Surface(SIZE, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.current_scene = PlayScene(self.surf)

    def event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            self.current_scene.event(event)

    def render(self):
        self.surf.fill((159, 79, 255))
        self.current_scene.render()
        self.screen.blit(self.surf, (0, 0))
        pygame.display.flip()


def main():
    game = Game()
    while True:
        for event in pygame.event.get():
            game.event(event)
        game.render()
        game.clock.tick(FPS)


if __name__ == "__main__":
    main()
