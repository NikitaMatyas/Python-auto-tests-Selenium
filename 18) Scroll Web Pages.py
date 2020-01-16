from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
driver.maximize_window()

# Scroll down the page by pixel
driver.execute_script('window.scrollBy(0, 1000)', '')
time.sleep(3)

# Scroll down the page till element found
element = driver.find_element_by_xpath('//*[@id="HTML1"]/h2')
driver.execute_script('arguments[0].scrollIntoView();', element)
time.sleep(3)

# Scroll to end of the page
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
time.sleep(3)

driver.quit()
