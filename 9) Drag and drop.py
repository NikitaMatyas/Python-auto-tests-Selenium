from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.w3schools.com/html/html5_draganddrop.asp')
driver.implicitly_wait(5)

element = driver.find_element_by_id('drag1')
target = driver.find_element_by_id('div2')

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
time.sleep(3)

driver.quit()
