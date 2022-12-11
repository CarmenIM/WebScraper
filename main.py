import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.categories import Category
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--mute-audio')


url = 'https://www.twitch.tv/directory/'
driver = webdriver.Chrome(options=chrome_options)


driver.get(url)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, './/div[contains(@data-a-id,"card")]')))

categories = []
card_elements = driver.find_elements(By.XPATH, './/div[contains(@data-a-id,"card")]')
for index,card_element in enumerate(card_elements):
# for card_element in card_elements:
    category = Category(card_element, driver=driver)
    category.extract_data()
    categories.append(category)

    if index == 1:
        break


    # break

driver.close()

output = [
    category.to_dict()
    for category in categories
]

with open('output.json', 'r') as json_file:
    json.dump(output, json_file, indent=2)