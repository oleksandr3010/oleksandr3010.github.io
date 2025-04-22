import csv
import math

# port centre coordinates
H = (-4.856967627496093, 39.82971936588512)
B = (-4.0413490398274465, 39.65183988932852)
I = (10.151440, 49.437508)
M = (-7.841504711428559, 39.753557016437114)
S = (-13.165519833694335, 37.05607246507563)
zanz_lat, zanz_long = -6.1659, 39.2026

# list of produce
produce = [
    "Chillies",
    "Cloves (Z'bar) New",
    "Cloves (Z'bar) Old",
    "Cloves (Pemba) New",
    "Cloves (Pemba) Old",
    "Cloves Stems",
    "Copra",
    "Gum Copal",
    "Hides",
    "Hippo-teeth",
    "Ivory",
    "Rhino-horns",
    "Rubber",
    "Sim Sim",
    "Tortoise shells",
    "Wax"
]

# radius of the offset circle, in degrees (~0.005° ≈ 500 m)
OFFSET_RADIUS = 0.01 # around 1 km around the port

def get_offset_coords(port_lat, port_long, product_name, radius=OFFSET_RADIUS):
    # Compute a small offset around (port_lat, port_long) based on product index.
    idx = produce.index(product_name)
    angle = 2 * math.pi * idx / len(produce)
    lat_off = radius * math.cos(angle)
    long_off = radius * math.sin(angle)
    return port_lat + lat_off, port_long + long_off

def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # write header
        writer.writerow([
            "date", "origin_port", "product", "total_weight", "numerical_weight",
            "port_lat", "port_long", "prod_lat", "prod_long", "zanz_lat", "zanz_long", "zanz_prod_lat",
            "zanz_prod_long"
        ])

        current_date = ""
        for row in reader:
            # if first cell isn't a product, it's the date/header row
            if row[0] not in produce:
                current_date = row[0]
                continue

            # determine which port block we're in by column index
            col = 1
            while col <= 15:
                # assign port name and base coords
                if col <= 3:
                    origin_port = "H.H. Dominions"
                    base_lat, base_long = H
                elif col <= 6:
                    origin_port = "British East Africa"
                    base_lat, base_long = B
                elif col <= 9:
                    origin_port = "Italian Benadir Ports"
                    base_lat, base_long = I
                elif col <= 12:
                    origin_port = "Mafia and other East African Ports"
                    base_lat, base_long = M
                else:
                    origin_port = "Southern Ports"
                    base_lat, base_long = S

                product = row[0]

                # if no tonnage for this port block, skip ahead
                if row[col] == "":
                    col += 3
                else:
                    # parse weights
                    fras_weight = float(row[col])
                    lbs_weight = float(row[col + 1]) / 35
                    numerical_weight = round(fras_weight + lbs_weight, 3)
                    total_weight = row[col + 2] # as a string

                    # compute product‑specific offset coords
                    prod_lat, prod_long = get_offset_coords(base_lat, base_long, product)
                    zanz_prod_lat, zanz_prod_long = get_offset_coords(zanz_lat, zanz_long, product)

                    # write out the row
                    writer.writerow([
                        current_date,
                        origin_port,
                        product,
                        total_weight,
                        numerical_weight,
                        base_lat,
                        base_long,
                        prod_lat,
                        prod_long,
                        zanz_lat,
                        zanz_long,
                        zanz_prod_lat,
                        zanz_prod_long
                    ])

                    # move past this block
                    col += 3

if __name__ == "__main__":
    process_csv("data.csv", "formatted.csv")
