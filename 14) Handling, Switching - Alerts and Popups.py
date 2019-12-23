from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def click_button(button):
    button.click()
    time.sleep(3)


chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)

button = driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')

click_button(button)
driver.switch_to_alert().accept()

click_button(button)
driver.switch_to_alert().dismiss()

time.sleep(3)
driver.quit()
