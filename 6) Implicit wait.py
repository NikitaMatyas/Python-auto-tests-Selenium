from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

"""
driver.set_network_conditions(
    offline=False,
    latency=5,  # additional latency (ms)
    download_throughput=50 * 1024,  # maximal throughput
    upload_throughput=500 * 1024)  # maximal throughput
"""

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

assert 'Welcome: Mercury Tours' in driver.title

driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')

driver.find_element_by_name('login').click()

driver.quit()
