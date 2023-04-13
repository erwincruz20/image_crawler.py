import os
import requests
from bs4 import BeautifulSoup


def download_images(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        image_url = image['src']
        if 'http' not in image_url:
            image_url = url + image_url
        response = requests.get(image_url)
        filename = os.path.join(folder_path, os.path.basename(image_url))
        with open(filename, 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    url = input("Enter website URL: ")
    folder_path = input("Enter folder path: ")
    download_images(url, folder_path)
