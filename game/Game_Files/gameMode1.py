import tkinter as tk
import json
import difflib

class gameMode1():
    def __init__(self):
        self.WIDTH = 1400
        self.HEIGHT = 800
        self.root = tk.Tk()
        self.button = tk.Button(self.root, text="Submit", width=25, command=self.on_button_click)
        self.entry = tk.Entry(self.root)
        self.label = tk.Label(self.root, text='')
        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="lightblue"
            )
        self.country_names = [
    'afghanistan',
    'albania',
    'algeria',
    'andorra',
    'angola',
    'antigua and barb.',
    'argentina',
    'armenia',
    'australia',
    'austria',
    'azerbaijan',
    'bahamas',
    'bahrain',
    'bangladesh',
    'barbados',
    'belarus',
    'belgium',
    'belize',
    'benin',
    'bhutan',
    'bolivia',
    'bosnia and herz.',
    'botswana',
    'brazil',
    'brunei',
    'bulgaria',
    'burkina faso',
    'burundi',
    'cabo verde',
    'cambodia',
    'cameroon',
    'canada',
    'central african rep.',
    'chad',
    'chile',
    'china',
    'colombia',
    'comoros',
    'congo',
    'costa rica',
    "côte d'ivoire",
    'croatia',
    'cuba',
    'cyprus',
    'czechia',
    'dem. rep. congo',
    'denmark',
    'djibouti',
    'dominica',
    'dominican rep.',
    'ecuador',
    'egypt',
    'el salvador',
    'eq. guinea',
    'eritrea',
    'estonia',
    'eswatini',
    'ethiopia',
    'fiji',
    'finland',
    'france',
    'gabon',
    'gambia',
    'georgia',
    'germany',
    'ghana',
    'greece',
    'grenada',
    'guatemala',
    'guinea',
    'guinea-bissau',
    'guyana',
    'haiti',
    'honduras',
    'hungary',
    'iceland',
    'india',
    'indonesia',
    'iran',
    'iraq',
    'ireland',
    'israel',
    'italy',
    'jamaica',
    'japan',
    'jordan',
    'kazakhstan',
    'kenya',
    'kiribati',
    'north korea',
    'south korea',
    'kosovo',
    'kuwait',
    'kyrgyzstan',
    'laos',
    'latvia',
    'lebanon',
    'lesotho',
    'liberia',
    'libya',
    'liechtenstein',
    'lithuania',
    'luxembourg',
    'madagascar',
    'malawi',
    'malaysia',
    'maldives',
    'mali',
    'malta',
    'marshall is.',
    'mauritania',
    'mauritius',
    'mexico',
    'micronesia',
    'moldova',
    'monaco',
    'mongolia',
    'montenegro',
    'morocco',
    'mozambique',
    'myanmar',
    'namibia',
    'nauru',
    'nepal',
    'netherlands',
    'new zealand',
    'nicaragua',
    'niger',
    'nigeria',
    'north macedonia',
    'norway',
    'oman',
    'pakistan',
    'palau',
    'palestine',
    'panama',
    'papua new guinea',
    'paraguay',
    'peru',
    'philippines',
    'poland',
    'portugal',
    'qatar',
    'romania',
    'russia',
    'rwanda',
    'st. kitts and nevis',
    'saint lucia',
    'st. vin. and gren.',
    'samoa',
    'san marino',
    'são tomé and principe',
    'saudi arabia',
    'senegal',
    'serbia',
    'seychelles',
    'sierra leone',
    'singapore',
    'slovakia',
    'slovenia',
    'solomon is.',
    'somalia',
    'south africa',
    's. sudan',
    'spain',
    'sri lanka',
    'sudan',
    'suriname',
    'sweden',
    'switzerland',
    'syria',
    'taiwan',
    'tajikistan',
    'tanzania',
    'thailand',
    'timor-leste',
    'togo',
    'tonga',
    'trinidad and tobago',
    'tunisia',
    'turkey',
    'turkmenistan',
    'tuvalu',
    'uganda',
    'ukraine',
    'united arab emirates',
    'united kingdom',
    'united states of america',
    'uruguay',
    'uzbekistan',
    'vanuatu',
    'vatican',
    'venezuela',
    'vietnam',
    'yemen',
    'zambia',
    'zimbabwe']

    def main(self):
        self.canvas.pack()
        self.button.pack()
        self.entry.pack()
        self.label.pack()

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
        country_name = self.entry.get().lower()

        #Exact match
        if country_name in self.country_names:
            self.fill_country(country_name, "red")
            self.label.config(text="")

        else:
            matches = difflib.get_close_matches(
                country_name,
                self.country_names,
                n=1,
                cutoff=0.6
            )

            if matches:
                corrected_name = matches[0]
                self.label.config(
                    text=f"Did you mean '{corrected_name}'?"
                )

            else:
                self.label.config(
                    text="Country not found"
                )

        self.entry.delete(0, tk.END)

game_instance = gameMode1()
game_instance.main()