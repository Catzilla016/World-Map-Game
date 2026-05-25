import tkinter as tk
import json

class gameMode1():
    def __init__(self):
        self.WIDTH = 1400
        self.HEIGHT = 800
        self.root = tk.Tk()
        self.button = tk.Button(self.root, text="Submit", width=25, command=self.on_button_click)
        self.entry = tk.Entry(self.root)
        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="lightblue"
            )

    def main(self):
        self.canvas.pack()
        self.button.pack()
        self.entry.pack()

        #Load the JSON
        with open("game/Game_Files/cleaned_world.json", "r", encoding="utf-8") as f:
            self.world = json.load(f)

        # Stores all polygon IDs for each country
        self.country_shapes = {}

        for feature in self.world["features"]:
            self.draw_country(feature)

        self.root.mainloop()
            

    def project(self, lon, lat):
        """
        Convert longitude/latitude into screen coordinates

        Args:
            lon (int): the longitude coordinate
            lat (int): the latitude coordinate
        
        Returns:
            x (int): x coordinate to draw on the map
            y (int): y coordinate to draw on the map
        """

        x = (lon + 180) * (self.WIDTH / 360)

        y = (90 - lat) * (self.HEIGHT / 180)

        return x, y


    def draw_country(self, feature):
        """
        Draws the country based on the feature type.
        If the feature is Polygon, then the coordinates of 
        the country are passed into the draw function.
        Else, the entire polygon is passed.
        
        Args:
            feature (dict): the features of the specifies country
        
        Returns:
            None
        """

        geometry = feature["geometry"]

        country_name = feature["properties"]["name"]

        self.country_shapes[country_name] = []

        if geometry["type"] == "Polygon":

            self.draw_polygon(
                geometry["coordinates"],
                country_name
            )

        elif geometry["type"] == "MultiPolygon":

            for polygon in geometry["coordinates"]:

                self.draw_polygon(
                    polygon,
                    country_name
                )


    def draw_polygon(self, coords, country_name):
        """
        Append the coordinates and the corresponding 
        country name into country_shapes.

        Args:
            coords (list): list of coordinates of each point to draw
            country_name (str): name of the coutry
        
        Return:
            None
        """

        for ring in coords:

            points = []

            for lon, lat in ring:

                x, y = self.project(lon, lat)

                points.extend([x, y])

            if len(points) >= 6:

                shape_id = self.canvas.create_polygon(
                    points,
                    fill="lightgray",
                    outline="black",
                    width=1
                )

                self.country_shapes[country_name].append(shape_id)


    def fill_country(self, country_name, color):
        """
        Fills the colour of the country specified

        Args:
            country_name (str): the name of the country
            color (str): the desired color of the country
        
        Returns:
            None
        """

        if country_name in self.country_shapes:

            for shape_id in self.country_shapes[country_name]:

                self.canvas.itemconfig(
                    shape_id,
                    fill=color
                )
    
    def on_button_click(self):
        country_name = self.entry.get()

        self.fill_country(country_name, "red")

        self.entry.select_clear()

game_instance = gameMode1()
game_instance.main()