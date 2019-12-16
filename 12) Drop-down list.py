from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.implicitly_wait(10)

element = driver.find_element_by_id('RESULT_RadioButton-9')
dropdown = Select(element)

dropdown.select_by_visible_text('Morning')
time.sleep(2)

dropdown.select_by_value('Radio-1')
time.sleep(2)

dropdown.select_by_index(0)
time.sleep(2)

# Available options
for opt in dropdown.options:
    print(opt)

# Available options in visible text
for opt in dropdown.options:
    print(opt.text)

# Count of options
print('Number of options:', len(dropdown.options))

driver.quit()
