class Airport:
    def __init__(self, ICAO, lat, lng):
        self.ICAO = ICAO
        self.coordinates = (lat, lng)
        self.sch = False
def IsSchengenAirport(code):
    schengen_countries = ['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH','BI','LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES','LS']

    if code == "":
        return None
    if code[:2] in schengen_countries:
        return True
    else:
        return False


def SetSchengen(airport):
    airport.schengen = IsSchengenAirport(airport.ICAO)

def PrintAirport(airport):
    print("ICAO: ", airport.ICAO)
    print("Coordinates: ", airport.coordinates)
    print("Schengen: ", airport.schengen)
#Step 3
def LoadAirports(filename):
    airports = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines[1:]:
                parts = line.strip().split()

                if len(parts) != 3:
                    continue

                code = parts[0]
                lat_str = parts[1]
                lon_str = parts[2]

                # LATITUD
                lat_deg = int(lat_str[1:3])
                lat_min = int(lat_str[3:5])
                lat_sec = int(lat_str[5:7])
                lat = lat_deg + lat_min/60 + lat_sec/3600

                if lat_str[0] == 'S':
                    lat = -lat

                # LONGITUD
                lon_deg = int(lon_str[1:4])
                lon_min = int(lon_str[4:6])
                lon_sec = int(lon_str[6:8])
                lon = lon_deg + lon_min/60 + lon_sec/3600

                if lon_str[0] == 'W':
                    lon = -lon

                airport = Airport(code, lat, lon)
                airports.append(airport)

    except FileNotFoundError:
        return []

    return airports


def SaveSchengenAirports(airports, filename):
    if not airports:
        return -1

    schengen_airports = [a for a in airports if a.schengen]

    if not schengen_airports:
        return -1

    with open(filename, 'w') as file:
        file.write("CODE LAT LON\n")

        for a in schengen_airports:
            lat_dir = 'N' if a.lat >= 0 else 'S'
            lon_dir = 'E' if a.lon >= 0 else 'W'

            lat = abs(a.lat)
            lon = abs(a.lon)

            lat_deg = int(lat)
            lat_min = int((lat - lat_deg) * 60)
            lat_sec = int((((lat - lat_deg) * 60) - lat_min) * 60)

            lon_deg = int(lon)
            lon_min = int((lon - lon_deg) * 60)
            lon_sec = int((((lon - lon_deg) * 60) - lon_min) * 60)

            lat_str = f"{lat_dir}{lat_deg:02d}{lat_min:02d}{lat_sec:02d}"
            lon_str = f"{lon_dir}{lon_deg:03d}{lon_min:02d}{lon_sec:02d}"

            file.write(f"{a.code} {lat_str} {lon_str}\n")

    return 0


def AddAirport(airports, airport):
    for a in airports:
        if a.code == airport.code:
            return -1

    airports.append(airport)
    return 0


def RemoveAirport(airports, code):
    for i, a in enumerate(airports):
        if a.code == code:
            airports.pop(i)
            return 0

    return -1