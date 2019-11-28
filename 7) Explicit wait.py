from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()

driver.get('https://www.expedia.com/')

driver.find_element_by_id('tab-flight-tab-hp').click()
driver.find_element_by_id('flight-origin-hp-flight').send_keys('SFO')
driver.find_element_by_id('flight-destination-hp-flight').send_keys('NYC')
driver.find_element_by_id('flight-departing-hp-flight').send_keys('12/10/2019')
driver.find_element_by_id('flight-returning-hp-flight').send_keys(Keys.CONTROL + 'a', Keys.DELETE)
driver.find_element_by_id('flight-returning-hp-flight').send_keys('12/20/2019')
driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

Nonstop_checkbox = 'stopFilter_stops-0'
element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, Nonstop_checkbox))
)

element.click()
time.sleep(3)
driver.quit()
