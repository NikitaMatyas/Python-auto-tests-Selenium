from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.implicitly_wait(10)

driver.find_element_by_id('RESULT_TextField-1').send_keys('Hello World')

time.sleep(3)

driver.quit()
