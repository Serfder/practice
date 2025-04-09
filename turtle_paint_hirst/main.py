# import colorgram

# colors = colorgram.extract('hirst.jpg', 30)
# colors_rgb = []

# for color in colors:
#    r = color.rgb[0]
#    g = color.rgb[1]
#    b = color.rgb[2]
#    colors_rgb.append((r, g, b))

    
color_list = [(202, 156, 95), (119, 162, 194), (150, 64, 96), (158, 82, 53), (219, 230, 239), (64, 99, 145), (166, 154, 52), (62, 123, 87), (191, 135, 158), (130, 183, 160), (188, 90, 122), (224, 203, 125), (131, 27, 47), (200, 95, 72), (82, 156, 132), (78, 24, 54), (43, 53, 105), (154, 209, 193), (139, 37, 31), (96, 122, 174), (77, 153, 165), (226, 168, 189), (38, 39, 79), (27, 64, 44), (154, 208, 216), (82, 40, 31), (33, 83, 59)]

# 10x10 painting, dot_width=20, space_btw_dot=50

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
origin = -(50 * 5)


for y in range(10):
    for x in range(10):
        tim.penup()
        tim.setposition((x * 50) + origin, (y * 50) + origin)
        tim.pendown()
        color = random.choice(color_list)
        tim.dot(20, color)

tim.screen.mainloop()
