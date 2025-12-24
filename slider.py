import pygame
from pygame import Surface
from pygame.ftfont import Font

def color_from_rgb_pc(red_pc: float, green_pc: float, blue: float) -> tuple[int, int, int]:
    return round(red_pc * 255 / 100), round(green_pc * 255 / 100), round(blue * 255 / 100)


class Slider:
    white: tuple[int, int, int] = (255, 255, 255)
    black: tuple[int, int, int] = (0, 0, 0)
    grey_light: tuple[int, int, int] = color_from_rgb_pc(80.6, 80.6, 80.6)
    grey_dark: tuple[int, int, int] = color_from_rgb_pc(28.1, 28.1, 28.1)
    grey_darker: tuple[int, int, int] = color_from_rgb_pc(17.9, 17.9, 17.9)

    def __init__(self, current_digit: int, max_digits_included: int = 9, digit_size: int = 50) -> None:
        self._current_digit: int = current_digit
        self._max_digits_included = max_digits_included
        self._digit_size = digit_size
        self._my_surface = Surface((self._digit_size, self._digit_size * (self._max_digits_included + 1)), pygame.SRCALPHA)

    def set_current_digit(self, current_digit: int):
        if current_digit < 0 or current_digit > self._max_digits_included:
            return
        self._current_digit: int = current_digit

    def get_current_digit(self) -> int:
        return self._current_digit

    def draw(self, screen: Surface, base_pos_x: int, base_pos_y: int) -> None:
        self._my_surface.fill(pygame.SRCALPHA)

        pygame.draw.rect(self._my_surface, self.white, self._my_surface.get_rect(),
                         border_radius=round(self._digit_size / 5))

        font_normal: Font = pygame.font.SysFont('Arial', round(self._digit_size * 0.8), bold=True)
        font_current: Font = pygame.font.SysFont('Arial', round(self._digit_size * 0.9), bold=True)

        for i in range(self._max_digits_included + 1):
            text_surface: Surface = font_normal.render(str(i), True, self.grey_light)
            if i == self._current_digit:
                text_surface: Surface = font_current.render(str(i), True, self.grey_darker)
            self._my_surface.blit(text_surface, ((self._digit_size - text_surface.get_width()) / 2,
                                                 (self._digit_size * i) + (self._digit_size - text_surface.get_height()) / 2))

        screen.blit(self._my_surface, (base_pos_x, base_pos_y - self._current_digit * self._digit_size))
