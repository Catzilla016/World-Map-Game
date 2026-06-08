import tkinter as tk
import json
import difflib
import random

class GameMode3(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.app.title("Country Guessr")

        self.configure(bg="#1b1f2a")

        self.WIDTH = 1400
        self.HEIGHT = 800

        # ---------- STATE ----------
        self.round = 0
        self.game_running = True
        self.seconds = 0

        # ---------- STYLE ----------
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

        self.out_of_label = tk.Label(self.top_bar, text="0/7", **label_style)
        self.out_of_label.pack(side="left", padx=20)

        self.timer_label = tk.Label(self.top_bar, text="0:00", **label_style)
        self.timer_label.pack(side="right", padx=20)

        # ---------- CANVAS FRAME ----------
        self.canvas_frame = tk.Frame(self, bg="#1b1f2a")
        self.canvas_frame.pack()

        self.canvas = tk.Canvas(
            self.canvas_frame,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="#cfe8ff",
            highlightthickness=2,
            highlightbackground="#2d3445"
        )
        self.canvas.pack(pady=10)

        # ---------- INPUT AREA ----------
        self.bottom_bar = tk.Frame(self, bg="#1b1f2a")
        self.bottom_bar.pack(pady=10)

        self.entry = tk.Entry(
            self.bottom_bar,
            font=("Arial", 14),
            width=30
        )
        self.entry.pack(side="left", padx=10)

        self.button = tk.Button(
            self.bottom_bar,
            text="Submit",
            command=self.on_button_click,
            **button_style
        )
        self.button.pack(side="left")

        # ---------- FEEDBACK ----------
        self.label = tk.Label(self, text="", **label_style)
        self.label.pack(pady=5)


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
        
        #TODO ADD MORE ALIASES!!!!
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

            "uae": "United Arab Emirates"
        }
        


    def main(self):
        self.canvas.pack()
        self.button.pack()
        self.entry.pack()
        self.label.pack()
        self.out_of_label.pack()
        self.timer_label.pack()
        self.back_button.pack()

        #Load the JSON
        with open("game/Game_Files/JSON/cleaned_world.json", "r", encoding="utf-8") as f:
            self.world = json.load(f)

        # Stores all polygon IDs for each country
        self.country_shapes = {}
        
        self.choose_country()
        
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

        all_rings = []

        min_x = float("inf")
        max_x = float("-inf")
        min_y = float("inf")
        max_y = float("-inf")

        if geometry["type"] == "Polygon":
            polygons = [geometry["coordinates"]]

        elif geometry["type"] == "MultiPolygon":
            polygons = geometry["coordinates"]

        for polygon in polygons:
            for ring in polygon:

                projected_ring = []

                for lon, lat in ring:

                    x, y = self.project(lon, lat)

                    projected_ring.append((x, y))

                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

                all_rings.append(projected_ring)

        country_width = max_x - min_x
        country_height = max_y - min_y

        scale_x = (self.WIDTH * 0.8) / country_width
        scale_y = (self.HEIGHT * 0.8) / country_height

        scale = min(scale_x, scale_y)

        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        canvas_center_x = self.WIDTH / 2
        canvas_center_y = self.HEIGHT / 2

        for ring in all_rings:

            transformed_points = []

            for x, y in ring:

                new_x = (
                    (x - center_x) * scale
                    + canvas_center_x
                )

                new_y = (
                    (y - center_y) * scale
                    + canvas_center_y
                )

                transformed_points.extend([new_x, new_y])

            if len(transformed_points) >= 6:

                self.canvas.create_polygon(
                    transformed_points,
                    fill="",
                    outline="black",
                    width=3
                )


    def on_button_click(self, event=None):
        country_name = self.entry.get().strip()

        lookup_name = country_name.lower()

        country_name = self.aliases.get(
            lookup_name,
            country_name
        )
        
        country_name = country_name.strip().lower()
        country_name = self.aliases.get(country_name, country_name)

        # Exact match
        if country_name.lower() == self.answer.lower():

            self.label.config(text="")
            
            if self.round == 7:
                self.app.show_frame("WinScreen", time=self.seconds)
                self.game_running = False
            else:
                self.round += 1
                self.out_of_label.config(
                    text=f"{self.round}/7"
                )
                self.canvas.delete("all")
                self.country_shapes.clear()
                self.choose_country()
                self.entry.delete(0, tk.END)

        # Close matches
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


    def update_timer(self):
        if self.game_running:
            self.seconds += 1

            minutes = self.seconds // 60
            seconds = self.seconds % 60

            self.timer_label.config(
                text=f"{minutes}:{seconds:02d}"
            )

            self.after(1000, self.update_timer)


    def choose_country(self):
        feature = self.world["features"][random.randint(0, len(self.world["features"]))]

        self.draw_country(feature)

        original_name = feature["properties"]["name"]

        self.answer = self.name_map.get(
            original_name,
            original_name
        )
        
        #DEBUGGING CUZ I SUCK AT GEOGRAPHY
        print(self.answer)

