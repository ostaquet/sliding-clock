import math
from datetime import datetime

import pygame
import sys

from pygame import Surface
from pygame.time import Clock

from slider import Slider


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width: int = 800
    screen_height: int = 600
    screen: Surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sliding Clock")

    # Set up the clock for controlling frame rate
    clock: Clock = pygame.time.Clock()
    fps: int = 60

    current_time = datetime.now()
    hour: int = current_time.hour
    minute: int = current_time.minute
    second: int = current_time.second

    digit_size: int = 50
    interspace: int = 15

    slider1: Slider = Slider(math.floor(hour / 10), max_digits_included=2, digit_size=digit_size)
    slider2: Slider = Slider(hour % 10, max_digits_included=9, digit_size=digit_size)

    slider3: Slider = Slider(math.floor(minute / 10), max_digits_included=5, digit_size=digit_size)
    slider4: Slider = Slider(minute % 10, max_digits_included=9, digit_size=digit_size)

    slider5: Slider = Slider(math.floor(second / 10), max_digits_included=5, digit_size=digit_size)
    slider6: Slider = Slider(second % 10, max_digits_included=9, digit_size=digit_size)

    # Game loop
    running = True
    while running:
        # 1. Process events/inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update game state
        current_time = datetime.now()
        hour: int = current_time.hour
        minute: int = current_time.minute
        second: int = current_time.second

        slider1.set_digit(math.floor(hour / 10))
        slider2.set_digit(hour % 10)
        slider3.set_digit(math.floor(minute / 10))
        slider4.set_digit(minute % 10)
        slider5.set_digit(math.floor(second / 10))
        slider6.set_digit(second % 10)

        # 3. Render/draw
        screen.fill((0, 0, 0))

        # Draw game objects here
        base_pos_x: int = round((screen.get_width() - (6 * digit_size) - (7 * interspace)) / 2)
        base_pos_y: int = round((screen_height - digit_size) / 2)

        pygame.draw.line(screen, (255, 255, 255), (0, base_pos_y + digit_size / 2), (screen_width, base_pos_y + digit_size / 2))

        slider1.draw(screen, base_pos_x + (0 * (digit_size + interspace)), base_pos_y)
        slider2.draw(screen, base_pos_x + (1 * (digit_size + interspace)), base_pos_y)
        slider3.draw(screen, base_pos_x + (2 * (digit_size + interspace) + interspace), base_pos_y)
        slider4.draw(screen, base_pos_x + (3 * (digit_size + interspace) + interspace), base_pos_y)
        slider5.draw(screen, base_pos_x + (4 * (digit_size + interspace) + 2 * interspace), base_pos_y)
        slider6.draw(screen, base_pos_x + (5 * (digit_size + interspace) + 2 * interspace), base_pos_y)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(fps)

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()