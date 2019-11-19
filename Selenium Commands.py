from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get("https://google.com")

print(driver.current_url)
print(driver.title)
# print(driver.page_source)

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]').click()
time.sleep(5)

driver.get("https://www.google.com/search?q=utc+now&oq=utc+now&aqs=chrome..69i64j0l7.8275j0j7&sourceid=chrome&ie=UTF-8")
driver.back()
time.sleep(3)
driver.forward()
time.sleep(5)

# driver.close()  # Close the browser window that the driver has focus of
driver.quit()  # Closes all browser windows and safely ends the session / destroy the web driver instance
