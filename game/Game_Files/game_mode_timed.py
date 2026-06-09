import tkinter as tk
import json
import difflib
from resource_path import resource_path

class GameMode2(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.app.title("Country Guessr")

        self.configure(bg="#1b1f2a")

        self.WIDTH = 1400
        self.HEIGHT = 750
        
        self.seconds = 0
        self.game_running = True

        button_style = {
            "font": ("Arial", 12),
            "bg": "#2d3445",
            "fg": "white",
            "activebackground": "#3e4a66",
            "activeforeground": "white",
            "bd": 0,
            "cursor": "hand2",
            "width": 12
        }

        label_style = {
            "font": ("Arial", 12),
            "bg": "#1b1f2a",
            "fg": "white"
        }
        
        # ---------- TOP BAR ----------
        self.top_bar = tk.Frame(self, bg="#1b1f2a")
        self.top_bar.pack(fill="x", pady=10)

        self.back_button = tk.Button(
            self.top_bar,
            text="Back",
            command=lambda: app.show_frame("MainMenu"),
            **button_style
        )
        self.back_button.pack(side="left", padx=10)

        self.timer_label = tk.Label(self.top_bar, text="0:00", **label_style)
        self.timer_label.pack(side="right", padx=20)

        self.country_num = tk.Label(self.top_bar, text="0/197" **label_style)

        # ---------- CANVAS ----------
        self.canvas = tk.Canvas(
            self,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="#cfe8ff",
            highlightthickness=2,
            highlightbackground="#2d3445"
        )
        self.canvas.pack(pady=10)

        # ---------- INPUT ----------
        self.bottom_bar = tk.Frame(self, bg="#1b1f2a")
        self.bottom_bar.pack(pady=10)

        self.entry = tk.Entry(self.bottom_bar, font=("Arial", 14), width=30)
        self.entry.pack(side="left", padx=10)

        self.button = tk.Button(
            self.bottom_bar,
            text="Submit",
            command=self.on_button_click,
            **button_style
        )
        self.button.pack(side="left")

        # ---------- LABEL ----------
        self.label = tk.Label(self, text="", **label_style)
        self.label.pack(pady=5)

        self.country_count = 0

        self.country_names =['Afghanistan',
        'Albania',
        'Algeria',
        'Andorra',
        'Angola',
        'Antigua and Barbuda',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bhutan',
        'Bolivia',
        'Bosnia and Herzegovina',
        'Botswana',
        'Brazil',
        'Brunei',
        'Bulgaria',
        'Burkina Faso',
        'Burundi',
        'Cabo Verde',
        'Cambodia',
        'Cameroon',
        'Canada',
        'Central African Republic',
        'Chad',
        'Chile',
        'China',
        'Colombia',
        'Comoros',
        'Congo',
        'Costa Rica',
        "Cote d'Ivoire",
        'Croatia',
        'Cuba',
        'Cyprus',
        'Czechia',
        'Dem. Rep. Congo',
        'Denmark',
        'Djibouti',
        'Dominica',
        'Dominican Republic',
        'Ecuador',
        'Egypt',
        'El Salvador',
        'Equatorial Guinea',
        'Eritrea',
        'Estonia',
        'Eswatini',
        'Ethiopia',
        'Fiji',
        'Finland',
        'France',
        'Gabon',
        'Gambia',
        'Georgia',
        'Germany',
        'Ghana',
        'Greece',
        'Grenada',
        'Guatemala',
        'Guinea',
        'Guinea Bissau',
        'Guyana',
        'Haiti',
        'Honduras',
        'Hungary',
        'Iceland',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ireland',
        'Israel',
        'Italy',
        'Jamaica',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Kenya',
        'Kiribati',
        'North Korea',
        'South Korea',
        'Kosovo',
        'Kuwait',
        'Kyrgyzstan',
        'Laos',
        'Latvia',
        'Lebanon',
        'Lesotho',
        'Liberia',
        'Libya',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Madagascar',
        'Malawi',
        'Malaysia',
        'Maldives',
        'Mali',
        'Malta',
        'Marshall Islands',
        'Mauritania',
        'Mauritius',
        'Mexico',
        'Micronesia',
        'Moldova',
        'Monaco',
        'Mongolia',
        'Montenegro',
        'Morocco',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Nepal',
        'Netherlands',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigeria',
        'North Macedonia',
        'Norway',
        'Oman',
        'Pakistan',
        'Palau',
        'Palestine',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Philippines',
        'Poland',
        'Portugal',
        'Qatar',
        'Romania',
        'Russia',
        'Rwanda',
        'St. Kitts and Nevis',
        'St. Lucia',
        'St. Vincent and the Grenadines',
        'Samoa',
        'San Marino',
        'Sao Tome and Principe',
        'Saudi Arabia',
        'Senegal',
        'Serbia',
        'Seychelles',
        'Sierra Leone',
        'Singapore',
        'Slovakia',
        'Slovenia',
        'Solomon Islands',
        'Somalia',
        'South Africa',
        'South Sudan',
        'Spain',
        'Sri Lanka',
        'Sudan',
        'Suriname',
        'Sweden',
        'Switzerland',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Tanzania',
        'Thailand',
        'Timor-Leste',
        'Togo',
        'Tonga',
        'Trinidad and Tobago',
        'Tunisia',
        'Turkey',
        'Turkmenistan',
        'Tuvalu',
        'Uganda',
        'Ukraine',
        'United Arab Emirates',
        'United Kingdom',
        'USA',
        'Uruguay',
        'Uzbekistan',
        'Vanuatu',
        'Vatican',
        'Venezuela',
        'Vietnam',
        'Yemen',
        'Zambia',
        'Zimbabwe']
        
        self.name_map = {
            "Antigua and Barb.": "Antigua and Barbuda",
            "Bosnia and Herz.": "Bosnia and Herzegovina",
            "Central African Rep.": "Central African Republic",
            "Côte d'Ivoire": "Cote d'Ivoire",
            "Dominican Rep.": "Dominican Republic",
            "Eq. Guinea": "Equatorial Guinea",
            "eSwatini": "Eswatini",
            "Guinea-Bissau": "Guinea Bissau",
            "Marshall Is.": "Marshall Islands",
            "Micronesia": "Micronesia",
            "St. Kitts and Nevis": "St. Kitts and Nevis",
            "Saint Lucia": "St. Lucia",
            "St. Vin. and Gren.": "St. Vincent and the Grenadines",
            "São Tomé and Principe": "Sao Tome and Principe",
            "Solomon Is.": "Solomon Islands",
            "S. Sudan": "South Sudan",
            "United States of America" : "USA"
        }
        
        self.aliases = {
            "usa": "USA",
            "united states": "USA",
            "united states of america": "USA",
            "america": "USA",

            "uk": "United Kingdom",
            "britain": "United Kingdom",
            "great britain": "United Kingdom",

            "south korea": "South Korea",
            "north korea": "North Korea",

            "ivory coast": "Cote d'Ivoire",

            "dr congo": "Dem. Rep. Congo",
            "democratic republic of the congo": "Dem. Rep. Congo",
            "drc": "Dem. Rep. Congo", 

            "uae": "United Arab Emirates",

            "afganistan": "Afghanistan",

            "sao tome": "Sao Tome and Principe",

            "st vincent": "St. Vincent and the Grenadines",
            "st kitts": "St. Kitts and Nevis",
            "st lucia": "St. Lucia",
            "barbuda": "Antigua and Barbuda",
            "antigua": "Antigua and Barbuda",

            "bosnia": "Bosnia and Herzegovina",

            "car": "Central African Republic",

            "drc": "Dem. Rep. Congo",

            "kazakstan": "Kazakhstan",

            "kyrgystan": "Kyrgyzstan",

            "new guinea": "Papua New Guinea",
            
            "east timor": "Timor-Leste",

            "cape verde": "Cabo Verde",

            "dr": "Dominican Republic"
        }
        
        self.country_dots = {}


    def main(self):

        #Load the JSON
        with open(
        resource_path("game/Game_Files/JSON/cleaned_world.json"),
        "r",
        encoding="utf-8"
        ) as f:
            self.world = json.load(f)

        # Stores all polygon IDs for each country
        self.country_shapes = {}

        for feature in self.world["features"]:
            self.draw_country(feature)
            
            x = (feature["properties"]["label_x"] + 180) * (self.WIDTH / 360)
            y = (90 - feature["properties"]["label_y"]) * (self.HEIGHT / 180)

            dot_id = self.canvas.create_oval(
                x - 2, y - 2,
                x + 2, y + 2,
                fill="blue",
                outline=""
            )

            original_name = feature["properties"]["name"]

            country_name = self.name_map.get(
                original_name,
                original_name
            )

            self.country_dots[country_name] = dot_id
        
        self.update_timer()
        
        self.entry.bind("<Return>", self.on_button_click)
            

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

        original_name = feature["properties"]["name"]

        country_name = self.name_map.get(
            original_name,
            original_name
        )

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
    

    def on_button_click(self, event=None):
        country_name = self.entry.get().strip()

        lookup_name = country_name.lower()

        country_name = self.aliases.get(
            lookup_name,
            country_name
        )
        
        country_name = country_name[0].upper() + country_name[1:]

        #Exact match
        if country_name in self.country_names:

            self.fill_country(country_name, "red")

            self.canvas.itemconfig(
                self.country_dots[country_name],
                fill="green"
            )

            self.label.config(text="")
            self.country_count += 1
            print(country_name)

        #Close matches
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
        
        if self.country_count >= 197:
            self.game_running = False
            self.app.show_frame("WinScreen", time=self.seconds)

        self.entry.delete(0, tk.END)


    def update_timer(self):
        if self.game_running:
            self.seconds += 1

            minutes = self.seconds // 60
            seconds = self.seconds % 60

            self.timer_label.config(
                text=f"{minutes}:{seconds:02d}"
            )

            self.after(1000, self.update_timer)