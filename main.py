import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def scrape_image(url):
    src = get_src(url)
    download_image(src)


def get_src(url):
    driver = get_driver(url)
    src = driver.find_element(By.CSS_SELECTOR, "._aagv img").get_attribute("src")
    driver.quit()
    return src

def download_image(src):
    data = requests.get(src).content
    with open('img.jpg','wb') as f:
        f.write(data) 

def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options)
    driver.implicitly_wait(0.5)

    driver.get(url)

    return driver


if __name__ == "__main__":
    param_length = len(sys.argv) - 1
    if param_length == 0:
        sys.exit("Missing required parameter \"Post URL\".")
    if param_length > 1:
        sys.exit(f"Function takes only 1 parameter, but {param_length} were entered.")

    url = sys.argv[1]
    if not "instagram.com/p/" in url:
        sys.exit("Invalid URL entered")
    scrape_image(url)