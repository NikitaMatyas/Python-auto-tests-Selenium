from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://newtours.demoaut.com/')
driver.implicitly_wait(10)

# How many links on a page
links = driver.find_elements(By.TAG_NAME, 'a')
print('Number of links:', len(links))

# Available links
for link in links:
    print(link)

# Available links as text
for link in links:
    print(link.text)

# Click on the links
driver.find_element(By.LINK_TEXT, 'REGISTER').click()
time.sleep(3)

# driver.find_element(By.PARTIAL_LINK_TEXT, 'REG').click()

driver.quit()
