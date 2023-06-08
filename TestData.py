from selenium import webdriver


class TestData():
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    UNAME = "Admin"
    PWD = "admin123"
    MAIN_TITLE = "OrangeHRM"
    ADD_EMP = "Add Employee"
    LOGIN_EXPECTED_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    PIM_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList" 
    fname = 'Abebe'
    mname = 'Beso'
    lname = 'Bela'
    SEARCH_BY_NAME = 'Abebe Beso Bela'
    _ID = '2723'