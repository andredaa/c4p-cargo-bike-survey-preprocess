
def get_district_for_neighborhood(neighborhood):
    neighborhood = neighborhood.strip()
    for district in districts:
        if neighborhood.lower().strip().replace(" ", "") in \
                map(lambda x:x.lower().strip().replace(" ", ""), districts[district]):
            return neighborhood, district

    return neighborhood, "unbekannt"


def get_neighborhood_for_zipcode(zipcode):
    return zipcodes[zipcode]


zipcodes = {
    20457:"HafenCity",
    22765:"Ottensen",
    22605:"Othmarschen",
    22299:"Winterhude"
}


districts = {
   "Hamburg-Mitte": [
       "Hamburg-Altstadt",
       "HafenCity",
       "Neustadt",
       "St. Pauli",
       "St. Georg",
       "Hammerbrook",
       "Borgfelde",
       "Hamm",
       "Horn",
       "Billstedt",
       "Billbrook",
       "Rothenburgsort",
       "Veddel",
       "Wilhelmsburg",
       "Kleiner Grasbrook",
       "Steinwerder",
       "Waltershof",
       "Finkenwerder",
       "Neuwerk"
    ],
   "Altona": [
       "Altona-Altstadt",
       "Sternschanze",
       "Altona-Nord",
       "Ottensen",
       "Bahrenfeld",
       "Groß Flottbek",
       "Othmarschen",
       "Lurup",
       "Osdorf",
       "Nienstedten",
       "Blankenese",
       "Iserbrook",
       "Sülldorf",
       "Rissen",
    ],
   "Eimsbüttel": [
       "Eimsbüttel",
       "Rotherbaum",
       "Harvestehude",
       "Hoheluft-West",
       "Lokstedt",
       "Niendorf",
       "Schnelsen",
       "Eidelstedt",
       "Stellingen",
    ],
   "Wandsbek": [
       "Eilbek",
       "Wandsbek",
       "Marienthal",
       "Jenfeld",
       "Tonndorf",
       "Farmsen-Berne",
       "Bramfeld",
       "Steilshoop",
       "Wellingsbüttel",
       "Sasel",
       "Poppenbüttel",
       "Hummelsbüttel",
       "Lemsahl-Mellingstedt",
       "Duvenstedt",
       "Wohldorf-Ohlstedt",
       "Bergstedt",
       "Volksdorf",
       "Rahlstedt"
    ],
   "Harburg": [
       "Harburg",
       "Neuland",
       "Gut Moor",
       "Wilstorf",
       "Rönneburg",
       "Langenbek",
       "Sinstorf",
       "Marmstorf",
       "Eißendorf",
       "Heimfeld",
       "Moorburg",
       "Altenwerder",
       "Hausbruch",
       "Neugraben-Fischbek",
       "Francop",
       "Neuenfelde",
       "Cranz"
    ],
   "Bergedorf": [
       "Lohbrügge",
       "Bergedorf",
       "Curslack",
       "Altengamme",
       "Neuengamme",
       "Kirchwerder",
       "Ochsenwerder",
       "Reitbrook",
       "Allermöhe",
       "Billwerder",
       "Moorfleet",
       "Tatenberg",
       "Spadenland",
       "Neuallermöhe"
    ],
   "Hamburg-Nord": [
       "Hoheluft-Ost",
       "Eppendorf",
       "Groß Borstel",
       "Alsterdorf",
       "Winterhude",
       "Uhlenhorst",
       "Hohenfelde",
       "Barmbek-Süd",
       "Dulsberg",
       "Barmbek-Nord",
       "Ohlsdorf",
       "Fuhlsbüttel",
       "Langenhorn"
    ]
}
