from write_rgb_image import write_rgb_image as write_image
import colorsys as cs


def convert_rgb_percentage_to_255(rgb_percentage):
    rgb_255 = map(lambda percentage: int(255 * percentage), rgb_percentage)

    return tuple(rgb_255)


def select_color(x, y, bounds, color_functions):
    def scale(val, mag=max(bounds)):
        return (val % mag) / (mag * 1.0)

    red = color_functions['red'](x, y)
    green = color_functions['green'](x, y)
    blue = color_functions['blue'](x, y)

    rgb_percentage = (scale(red), scale(green), scale(blue))

    color = convert_rgb_percentage_to_255(rgb_percentage)

    return {
        'x': x,
        'y': y,
        'color': color,
    }


'''
Some functions to try:

(x**2 + y**2) / (x + y + 1),

x % (y + 1),

y**2 + x**3,


'''

color_functions = {
    'red': (lambda x, y: x + y),
    'green': (lambda x, y: x),
    'blue': (lambda x, y: y),
}
bounds = (500, 500)
colors = [
    select_color(x, y, bounds, color_functions)
    for x in range(bounds[0])
    for y in range(bounds[1])
]

write_image(colors, bounds)
