from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options  # For changing Chrome settings


def find_element(locator, wait=10):
    return WebDriverWait(driver, wait).until(EC.presence_of_element_located(locator),
                                             message="Can't find element by locator")


chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

''' Change download path
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\MyFolder"})
And driver must be like the following:
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chromeOptions)
'''

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.implicitly_wait(10)

text_box = (By.ID, 'textbox')
create_button = (By.ID, 'createTxt')
download_link = (By.ID, 'link-to-download')

find_element(text_box).send_keys('Some text')
find_element(create_button).click()
find_element(download_link).click()
time.sleep(5)

driver.quit()
