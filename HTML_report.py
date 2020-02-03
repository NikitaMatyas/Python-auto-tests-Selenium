from selenium import webdriver
import pytest
import time


class TestOrangeHRM:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()

    @pytest.fixture()
    def teardown(self):
        yield
        self.driver.quit()

    def test_home_page_title(self, setup, teardown):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        assert self.driver.title == 'OrangeHRM'
        time.sleep(3)

    def test_login(self, setup, teardown):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(3)
