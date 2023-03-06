import colorgram

color = colorgram.extract('hirst.jpg', 7)

first_color = color[0]
rgb = first_color.rgb

print(rgb)
