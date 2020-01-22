from selenium import webdriver
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)
driver.maximize_window()

driver.save_screenshot('C:\\ScreenshotTest\\HomePage.png')
''' Or .get_screenshot_as_file '''
''' WebElements have a .screenshot() method that works similarly, but only captures the selected element '''

driver.quit()
