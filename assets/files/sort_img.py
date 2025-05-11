import os
import csv
import shutil

# Define the path to the CSV file
GAME_FILE = os.path.join(os.path.dirname(__file__), 'games.csv')

class Game:
    def __init__(self, name, genre5, genre7, genreAll):
        self.name = name
        self.genre5 = genre5
        self.genre7 = genre7
        self.genreAll = genreAll

def main():
    games = []
    genre5_list = set()
    genre7_list = set()

    # Read TSV file using \t as delimiter
    with open(GAME_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Game Name'].strip()
            genre5 = row['5-Genre Category'].strip()
            genre7 = row['7-Genre Category'].strip()
            genreAll = row['Specific Genre'].strip()

            genre5_list.add(genre5)
            genre7_list.add(genre7)
            games.append(Game(name, genre5, genre7, genreAll))

    # Create directories for genre5 and genre7
    for genre in genre5_list:
        os.makedirs(os.path.join('genre5', genre), exist_ok=True)

    for genre in genre7_list:
        os.makedirs(os.path.join('genre7', genre), exist_ok=True)

    # Copy game image files
    for game in games:
        src_path = os.path.join('ps4_images', game.name)
        dst_path_5 = os.path.join('genre5', game.genre5, game.name)
        dst_path_7 = os.path.join('genre7', game.genre7, game.name)

        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path_5)
            shutil.copy(src_path, dst_path_7)
        else:
            print(f"Warning: File not found - {src_path}")

if __name__ == '__main__':
    main()
