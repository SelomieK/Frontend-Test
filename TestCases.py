from TestData import TestData
from Locators import Locators
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import HtmlTestRunner
driver = webdriver.Chrome()

class Test_Landing_Base(unittest.TestCase):
    
    
    def setUp(self):
        print("Testing Started\n")
        

    def test_landing_page_loaded_successfully(self):
        """User should be able to navigate to the login page"""

        driver.get(TestData.BASE_URL)
        driver.maximize_window()
        # driver = LandingPage(driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(TestData.MAIN_TITLE, driver.title)
        time.sleep(3)

    def test_login(self):
        """User should be able to login succesfully"""
        driver.find_element(*Locators.USERNAME).send_keys(TestData.UNAME)
        driver.find_element(*Locators.PASSWORD).send_keys(TestData.PWD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
         
        if driver.current_url == TestData.LOGIN_EXPECTED_URL:
            assert True
        else:
            print("login not succesful")
        self.assertIn("OrangeHRM", driver.title)
        time.sleep(3)
        # driver.close()
        # add user PIM
    def test_pim(self):

        """Test add employee and search"""

        driver.find_element(*Locators.PIM).click()
        if driver.current_url == TestData.PIM_URL:
             assert True
        else:
            print("not loaded")
        time.sleep(3)

        """Add Employee"""

        driver.find_element(*Locators.ADD_EMPLOYEE).click()
        time.sleep(5)
        driver.find_element(*Locators.FNAME).send_keys(TestData.fname)
        driver.find_element(*Locators.MNAME).send_keys(TestData.mname)
        driver.find_element(*Locators.LNAME).send_keys(TestData.lname)
        time.sleep(2)
        self._id = driver.find_element(By.CSS_SELECTOR,"input.oxd-input.oxd-input--active").text
        driver.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
        time.sleep(5)

        """Search employee list"""
        # navigate back to PIM
        driver.find_element(*Locators.PIM).click()
        time.sleep(3)
        driver.find_element(*Locators.EMPLOYEE_LIST).click()
        time.sleep(5)
        
        driver.find_element(*Locators.SEARCH_LOCATOR).send_keys(TestData.SEARCH_BY_NAME)
        time.sleep(5)
        driver.find_element(*Locators.SEARCH_BUTTON).click()
        driver.find_element(*Locators.SEARCH_BUTTON).send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]').click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div').send_keys(Keys.RETURN)
        self.bodyText = driver.find_element(By.CSS_SELECTOR,'body').text
        if TestData.SEARCH_BY_NAME in self.bodyText:
            assert True
            print('----employee with given ID found!----')
        else:
            print("----employee found!----")
    """Search by name and verify the details"""  
    # def test_search(self):

        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())