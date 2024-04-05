# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   25-03-2024 11:09:08 PM       23:09:08
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 25-03-2024 11:38:46 PM       23:38:46
import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/?couponCode=HOLI24"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element with class 'intro-asset--img-aspect--3gluH'
intro_asset = soup.find(class_='intro-asset--img-aspect--3gluH')

# Find the img tag within the intro_asset
if intro_asset:
    img_tag = intro_asset.find('img')
    if img_tag:
        # Extract srcset attribute
        srcset = img_tag.get('srcset')
        if srcset:
            # Split srcset by comma to separate URLs and resolutions
            sources = srcset.split(',')
            # Iterate over sources to find the highest resolution image URL
            highest_resolution_url = None
            highest_resolution = 0
            for source in sources:
                url, resolution = source.strip().split(' ')
                resolution = int(resolution[:-1])  # remove 'w' at the end and convert to int
                if resolution > highest_resolution:
                    highest_resolution_url = url
                    highest_resolution = resolution
            print("Highest resolution image URL:", highest_resolution_url)
        else:
            print("No srcset attribute found.")
    else:
        print("No img tag found within the specified class.")
else:
    print("No element found with class 'intro-asset--img-aspect--3gluH'.")
