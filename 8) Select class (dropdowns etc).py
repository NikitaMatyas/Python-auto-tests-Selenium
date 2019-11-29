from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()

driver.get('http://demo.guru99.com/test/newtours/register.php')
driver.implicitly_wait(10)

driver.implicitly_wait(10)
country = Select(driver.find_element_by_name('country'))
# Also can be element.select_by_index
# element.select_by_visible_text
country.select_by_value('AUSTRALIA')

# element.select_all()
# element.deselect_all()
# element = select.options
# To submit from the DOM - element.submit()

time.sleep(5)

driver.quit()
