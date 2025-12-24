import pygame
from pygame import Surface
from pygame.ftfont import Font

def color_from_rgb_pc(red_pc: float, green_pc: float, blue: float) -> tuple[int, int, int]:
    return round(red_pc * 255 / 100), round(green_pc * 255 / 100), round(blue * 255 / 100)

def grey_from_int(value: int) -> tuple[int, int, int]:
    return value, value, value

class Slider:
    white: tuple[int, int, int] = (255, 255, 255)
    black: tuple[int, int, int] = (0, 0, 0)
    grey_light: tuple[int, int, int] = color_from_rgb_pc(80.6, 80.6, 80.6)
    grey_dark: tuple[int, int, int] = color_from_rgb_pc(28.1, 28.1, 28.1)
    grey_darker: tuple[int, int, int] = color_from_rgb_pc(17.9, 17.9, 17.9)

    def __init__(self, digit: int, max_digits_included: int = 9, digit_size: int = 50, transition_max_iterations: int = 25) -> None:
        self._current_digit: int = digit
        self._max_digits_included = max_digits_included
        self._digit_size = digit_size

        self._next_digit: int = digit
        self._is_transition_in_progress = False
        self._transition_current_iterator = 0
        self._transition_max_iterations = transition_max_iterations

        self._my_surface = Surface((self._digit_size, self._digit_size * (self._max_digits_included + 1)), pygame.SRCALPHA)

    def set_digit(self, digit: int):
        if digit < 0 or digit > self._max_digits_included:
            self._is_transition_in_progress = False
            return

        self._next_digit = digit

        if self._next_digit == self._current_digit:
            self._is_transition_in_progress = False
            return

        if self._next_digit != self._current_digit and not self._is_transition_in_progress:
            self._is_transition_in_progress = True
            self._transition_current_iterator = 0


    def draw(self, screen: Surface, base_pos_x: int, base_pos_y: int) -> None:
        self._my_surface.fill(pygame.SRCALPHA)

        pygame.draw.rect(self._my_surface, self.white, self._my_surface.get_rect(),
                         border_radius=round(self._digit_size / 5))

        font_normal: Font = pygame.font.SysFont('Arial', round(self._digit_size * 0.8), bold=True)
        font_current: Font = pygame.font.SysFont('Arial', round(self._digit_size * 0.9), bold=True)

        grey_level_light: int = self.grey_light[0]
        grey_level_dark: int = self.grey_dark[0]
        diff_grey_level: int = grey_level_light - grey_level_dark
        step_grey_level: int = round(diff_grey_level / self._transition_max_iterations)

        for i in range(self._max_digits_included + 1):
            text_surface: Surface = font_normal.render(str(i), True, self.grey_light)

            if i == self._current_digit:
                text_surface: Surface = font_current.render(str(i), True, self.grey_darker)

            if self._is_transition_in_progress:
                if i == self._current_digit:
                    text_surface: Surface = font_current.render(str(i), True, grey_from_int(
                        grey_level_dark + (step_grey_level * self._transition_current_iterator)))
                if i == self._next_digit:
                    text_surface: Surface = font_current.render(str(i), True, grey_from_int(
                        grey_level_light - (step_grey_level * self._transition_current_iterator)))

            self._my_surface.blit(text_surface, ((self._digit_size - text_surface.get_width()) / 2,
                                                 (self._digit_size * i) + (self._digit_size - text_surface.get_height()) / 2))

        if not self._is_transition_in_progress:
            screen.blit(self._my_surface, (base_pos_x, base_pos_y - self._current_digit * self._digit_size))
            return

        pos_y_origin: int = base_pos_y - self._current_digit * self._digit_size
        pos_y_destination: int = base_pos_y - self._next_digit * self._digit_size
        distance_to_destination: int = pos_y_destination - pos_y_origin
        step_to_destination: int = round(distance_to_destination / self._transition_max_iterations)

        screen.blit(self._my_surface, (base_pos_x, pos_y_origin + (step_to_destination * self._transition_current_iterator)))
        self._transition_current_iterator += 1

        if self._transition_current_iterator == self._transition_max_iterations:
            self._transition_current_iterator = 0
            self._is_transition_in_progress = False
            self._current_digit = self._next_digit

