import os
import requests
import markdown2
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def extract_image_links(markdown_content):
    soup = BeautifulSoup(markdown2.markdown(markdown_content), 'html.parser')
    img_tags = soup.find_all('img')
    image_links = [img['src'].split(' ')[0] for img in img_tags]  # Split and take the first part to clean URL
    return image_links

def download_images(image_links, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    for img_url in image_links:
        img_filename = os.path.basename(urlparse(img_url).path)
        img_path = os.path.join(output_folder, img_filename)
        with open(img_path, 'wb') as img_file:
            response = requests.get(img_url, headers=headers)
            if response.status_code == 200:
                img_file.write(response.content)
                print(f"Downloaded: {img_filename}")
            else:
                print(f"Failed to download: {img_url} with status code {response.status_code}")


# Get the path of the current script
script_path = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the Markdown file
markdown_file_path = os.path.join(script_path, 'Lecture_pres.md')

# Read Markdown file
with open(markdown_file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# Extract image links from Markdown content
image_links = extract_image_links(markdown_content)

# Construct the path to the output folder
output_folder = os.path.join(script_path, 'pics')

# Download images from the extracted links
download_images(image_links, output_folder)
