from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
driver.maximize_window()

driver.switch_to.frame(0)

file_path = 'C://Users/anduser/testfile.txt'
driver.find_element_by_id('RESULT_FileUpload-10').send_keys(file_path)
time.sleep(5)

driver.quit()
