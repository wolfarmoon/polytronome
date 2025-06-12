import pygame
import math
import beat_indicator


def generate_poligon_verts(offset, sides, radius):
    x = offset[0]
    y = offset[1]

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
        self.spb = 60 / bpm

        self.cspb = 0

        self.current_beat = 1

        self.verices = generate_poligon_verts(
            [
                pygame.display.get_window_size()[0] / 2,
                pygame.display.get_window_size()[1] / 2,
            ],
            self.time_signature,
            100,
        )

        self.beat_in = beat_indicator.BeatIndicator(screen, width, color)

    def draw(self):
        # Draw the base shape
        pygame.draw.polygon(
            self.screen,
            self.pt_color,
            self.verices,
            self.width,
        )

        self.beat_in.draw()

        # Draw the point
        # I may use a linear function to make it seem to move along the sides.
        # it will move from A to B, depending the shape, may move from vert1 to vert2, vert2 to vert3, vert3 to vert1

    def tick(self, dt):
        self.cspb += dt

        if self.cspb > self.spb:
            self.cspb -= self.spb
            self.current_beat += 1
            self.sounds[1].play()

        # fuck! I've been here 1 hour.

        if self.current_beat >= len(self.verices):
            self.current_beat = 0
            self.sounds[0].play()

        a = self.verices[self.current_beat - 1]
        b = self.verices[self.current_beat]

        t = self.cspb / self.spb

        self.beat_in.update([a, b], t)
