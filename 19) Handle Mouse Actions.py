from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
driver.maximize_window()

actions = ActionChains(driver)

# Mouse Hover
age_field = driver.find_element_by_xpath('//*[@id="age"]')
actions.move_to_element(age_field)

# Get Placeholder value
# findElement(By.xpath("//input[@placeholder='Gender']")).getAttribute("placeholder")

# Double Click
button = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
actions.double_click(button).perform()
time.sleep(3)

# Right Click
actions.context_click(button).perform()
time.sleep(3)

# Drag and Drop
source = driver.find_element_by_xpath('//*[@id="draggable"]')
target = driver.find_element_by_xpath('//*[@id="droppable"]')
actions.drag_and_drop(source, target).perform()
time.sleep(3)

driver.quit()
