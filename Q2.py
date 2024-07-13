# Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.



import requests
from time import sleep

def download_with_retries(urls, retries=3):
    contents = []
    for url in urls:
        for _ in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                contents.append(response.content)
                break
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                sleep(1)
        else:
            print(f"Failed to download {url} after {retries} attempts")
            contents.append(None)
    return contents

urls = ["https://example.com", "https://nonexistent.com"]
contents = download_with_retries(urls)
print("Downloaded content:", contents)
