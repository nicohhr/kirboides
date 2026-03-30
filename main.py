import sys

import pygame

import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # initializing groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # initializing asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # initialize player
    player.Player.containers = (updatable, drawable)
    p1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # initializing shots
    Shot.containers = (shots, updatable, drawable)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing time and time variation variable
    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            # check colision with the player
            if asteroid.collides_with(p1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        # Pausing game every 1/60th of a second
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
