import argparse
from multiprocessing import Process
import os
import time
import requests

URLS = [
    'https://rare-gallery.com/uploads/posts/379137-4k-wallpaper.jpg',
    'https://thenerdstash.com/wp-content/uploads/2022/08/tft.jpg',
    'https://wow.blizzwiki.ru/images/8/8a/Warcraft_III_TFT_Scourge_Undead_Campaign.jpg',
    'https://i.pinimg.com/736x/c6/41/72/c64172cfc8f8908d06e731999c8ab195.jpg',
    'https://wow.blizzwiki.ru/images/b/b4/Warcraft_III_TFT_Blood_Elf_Human_Campaign.jpg',
    'https://c4.wallpaperflare.com/wallpaper/474/542/557/blizzard-entertainment-pc-gaming-red-eyes-fantasy-girl-fan'
    '-art-hd-wallpaper-preview.jpg',
    'https://www.lenbaget.ru/wp-content/uploads/2021/11/full_20387.jpg'
]

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


def img_saver(url):
    response = requests.get(url)
    filename = f'{url.split("/")[-1]}'
    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


processes = []
start_time = time.time()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    # for url in args.url_list: # for args via cmd
    for url in URLS:
        process = Process(target=img_saver, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')
