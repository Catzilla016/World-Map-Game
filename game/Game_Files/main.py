import tkinter as tk
import json

WIDTH = 1400
HEIGHT = 800

root = tk.Tk()

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="lightblue"
)

canvas.pack()

# Load GeoJSON
with open("game/Game_Files/mapJSON.json", "r", encoding="utf-8") as f:
    world = json.load(f)

# Stores all polygon IDs for each country
country_shapes = {}

def project(lon, lat):
    """
    Convert longitude/latitude into screen coordinates

    Args:
        lon (int): the longitude coordinate
        lat (int): the latitude coordinate
    
    Returns:
        x (int): x coordinate to draw on the map
        y (int): y coordinate to draw on the map
    """

    x = (lon + 180) * (WIDTH / 360)

    y = (90 - lat) * (HEIGHT / 180)

    return x, y


def draw_country(feature):
    """
    
    """

    geometry = feature["geometry"]

    country_name = feature["properties"]["name"]

    country_shapes[country_name] = []

    if geometry["type"] == "Polygon":

        draw_polygon(
            geometry["coordinates"],
            country_name
        )

    elif geometry["type"] == "MultiPolygon":

        for polygon in geometry["coordinates"]:

            draw_polygon(
                polygon,
                country_name
            )


def draw_polygon(coords, country_name):

    for ring in coords:

        points = []

        for lon, lat in ring:

            x, y = project(lon, lat)

            points.extend([x, y])

        if len(points) >= 6:

            shape_id = canvas.create_polygon(
                points,
                fill="lightgray",
                outline="black",
                width=1
            )

            country_shapes[country_name].append(shape_id)


def fill_country(country_name, color):
    """
    Fills the colour of the country specified

    Args:
        country_name (str): the name of the country
        color (str): the desired color of the country
    
    Returns:
        None
    """

    if country_name in country_shapes:

        for shape_id in country_shapes[country_name]:

            canvas.itemconfig(
                shape_id,
                fill=color
            )

for feature in world["features"]:

    draw_country(feature)

fill_country("Zambia", "red")
fill_country("Germany", "blue")
fill_country("Guatemala", "green")

root.mainloop()