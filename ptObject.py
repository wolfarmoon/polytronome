import pygame
import math
import beat_indicator


def generate_poligon_verts(center, sides, radius):
    x = center[0]
    y = center[1]

    vertices = []

    for i in range(sides):
        x_i = radius * math.cos(((2 * math.pi * i) / sides) + (math.pi * 3) / 2)
        y_i = radius * math.sin(((2 * math.pi * i) / sides) + (math.pi * 3) / 2)
        vertices.append((x_i + x, y_i + y))

    return vertices


class PolytronomeObject:
    def __init__(
        self,
        screen,
        sounds: tuple[pygame.mixer.Sound],
        radius,
        width,
        color,
        time_signature,
        bpm,
    ):
        self.screen = screen
        self.sounds = sounds

        self.radius = radius
        self.width = width
        self.pt_color = color
        self.time_signature = time_signature
        # Seconds per beat
        self.base_spb = 60 / bpm

        self.current_spb = 0

        self.current_beat = 1

        self.vertices = generate_poligon_verts(
            [
                pygame.display.get_window_size()[0] / 2,
                pygame.display.get_window_size()[1] / 2,
            ],
            self.time_signature,
            100,
        )

        self.beat_indicator = beat_indicator.BeatIndicator(screen, width, color)

    def draw(self):
        # Draw the base shape
        pygame.draw.polygon(
            self.screen,
            self.pt_color,
            self.vertices,
            self.width,
        )

        self.beat_indicator.draw()

    def update(self, dt):
        self.current_spb += dt

        if self.current_spb > self.base_spb:
            self.current_spb -= self.base_spb
            self.current_beat += 1
            self.sounds[1].play()

        # fuck! I've been here 1 hour.

        if self.current_beat >= len(self.vertices):
            self.current_beat = 0
            self.sounds[0].play()

        a = self.vertices[self.current_beat - 1]
        b = self.vertices[self.current_beat]

        t = self.current_spb / self.base_spb

        self.beat_indicator.update([a, b], t)
