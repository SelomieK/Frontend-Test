from selenium.webdriver.common.by import By
#locatord are for saving the elements of html page to be tested

class Locators():
    # --- login Page Locators ---
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button')
    PIM = (By.LINK_TEXT ,'PIM')
    ADD_EMPLOYEE = (By.LINK_TEXT,'Add Employee')
    EMPLOYEE_LIST = (By.LINK_TEXT,'Employee List')
    FNAME = (By.NAME,'firstName')
    MNAME = (By.NAME,'middleName')
    LNAME = (By.NAME,"lastName")
    IDLOCATOR = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    SEARCH_LOCATOR = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    SEARCH_BUTTON = (By.CSS_SELECTOR,'button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')
    (By.LINK_TEXT,'Leave')