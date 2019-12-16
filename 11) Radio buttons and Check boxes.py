from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.implicitly_wait(10)

status = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]').is_selected()  # Male radio button
print(status)

button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')
driver.execute_script("arguments[0].click();", button)  # If other elements covers radio button
time.sleep(3)

status = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]').is_selected()  # Male radio button
print(status)

driver.find_element_by_id('RESULT_CheckBox-8_0').click()
time.sleep(3)

driver.quit()
