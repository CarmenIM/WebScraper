from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time


class Channel:
    def __init__(self, element, driver):
        self._element = element
        self._driver = driver
        self._title = None
        # self._image = None
        self._followers = None
        self._viewers = None
        self._time = None

    def extract_data(self):
        link_element = self._element.find_element(By.TAG_NAME, 'a')

        self._driver.execute_script(f'window.open("{link_element.get_attribute("href")}")')
        self._driver.switch_to.window(self._driver.window_handles[-1])

        WebDriverWait(self._driver, 1200).until(
            EC.presence_of_element_located((By.XPATH, './/div[@role="presentation"]/following-sibling::p[1]')))
        # time.sleep(5)

        self._title = self._driver.find_element(By.XPATH, './/h1[contains(@class,"tw-title")]').text
        self._followers = self._driver.find_element(By.XPATH, './/section[@id="live-channel-about-panel"]//span//span').text
        self._viewers = self._driver.find_element(By.XPATH, './/div[@role="presentation"]/following-sibling::p[1]').text
        self._time = self._driver.find_element(By.XPATH, './/span[contains(@class,"live-time")]').text
        print(self._title, self._followers, self._viewers, self._time)

        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def to_dict(self):
        return {
            'Channel Title': self._title,
            # 'Image channel': self._image,
            'Channel Followers': self._followers,
            'Channel Viewers': self._viewers,
            'Time live': self._time
        }
