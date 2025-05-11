import os
import argparse
import requests
from bs4 import BeautifulSoup

def safe_filename(name: str) -> str:
    """
    Sanitize the game title to create a filesystem-safe filename.
    """
    return "".join(c for c in name if c.isalnum() or c in " _-").rstrip()

def download_images(page_url: str, game_list: list, output_folder: str) -> None:
    """
    Scrape the given page URL, find images whose alt text matches one of the games
    in game_list, and download them into output_folder.
    """
    # Create output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    resp = requests.get(page_url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')
    cards = soup.find_all('div', class_='imgOver')

    for card in cards:
        img = card.find('img')
        if not img or not img.has_attr('alt') or not img.has_attr('src'):
            continue

        title = img['alt'].strip()
        if title not in game_list:
            continue

        img_url = img['src']
        # Derive file extension from URL
        ext = os.path.splitext(img_url)[1].split('?')[0] or '.jpg'
        filename = f"{safe_filename(title)}{ext}"
        filepath = os.path.join(output_folder, filename)

        if os.path.exists(filepath):
            print(f"[SKIP] Already downloaded: {title}")
            continue

        img_data = requests.get(img_url)
        img_data.raise_for_status()
        with open(filepath, 'wb') as f:
            f.write(img_data.content)
        print(f"[DOWNLOADED] {title} -> {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Download PS4 game images")
    url = "https://gamesdb.launchbox-app.com/platforms/games/50-sony-playstation-4"
    parser.add_argument('--games-file', required=True,
                        help='Path to a text file containing top 200 game titles (one per line)')
    parser.add_argument('--output', default='images',
                        help='Output directory for downloaded images')
    args = parser.parse_args()

    # Load game titles
    with open(args.games_file, 'r', encoding='utf-8') as f:
        games = [line.strip() for line in f if line.strip()]
    download_images(url, games, args.output)
    # /page/2
    for i in range(2,24):
        download_images(url + "/page/" + str(i), games, args.output)
    
if __name__ == '__main__':
    main()

