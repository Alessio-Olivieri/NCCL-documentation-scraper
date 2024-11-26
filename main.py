import os
import requests
import time
from bs4 import BeautifulSoup

# URL of the main documentation page
main_url = "https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Function to fetch the content of a URL
def fetch_url_content(url, session = None):
    if session == None:
        response = requests.get(url, headers = headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    else:
        print("utilizing same session")
        response = session.get(url, headers = headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    
# Function to save content to a file
def save_content_to_file(content, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        # Check if the file is not empty to add a newline before appending
        if file.tell() != 0:
            file.write('\n')
        file.write(content)

# enable logging
# import logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

session = requests.Session()

# Fetch the main page content
main_page_content = fetch_url_content(main_url, session)


# Parse the main page content
soup = BeautifulSoup(main_page_content, 'html.parser')

index = soup.find("div", class_="toctree-wrapper compound")

# Find all the <a> tags
links = index.find_all('a', href=True)

# Extract the href attributes
hrefs = [link['href'] for link in links if "#" not in link["href"]]
print(hrefs)

for link in hrefs:
    page_content = fetch_url_content("https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/_sources/" + link[:-4] +"rst.txt",
                                     session)
    save_content_to_file(page_content, "data.txt")
    time.sleep(1)
    print("processed " + link)