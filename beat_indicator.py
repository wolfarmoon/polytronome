import pygame


# 0 beginning of animation, 1 the end of it.
def easeInOutCubic(t):
    t *= 2
    if t < 1:
        return t * t * t / 2
    else:
        t -= 2
        return (t * t * t + 2) / 2


def interpolatePoints(point_a, point_b, completeness):
    x1, y1 = point_a[0], point_a[1]
    x2, y2 = point_b[0], point_b[1]

    t = easeInOutCubic(completeness)

    x = x1 + (x2 - x1) * t
    y = y1 + (y2 - y1) * t

    return (x, y)


class BeatIndicator:
    def __init__(self, screen, width, color):
        self.color = color
        self.screen = screen
        self.width = width
        self.pos = ()

    def update(self, points, completeness):
        self.pos = interpolatePoints(points[0], points[1], completeness)
        

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.width * 2)
