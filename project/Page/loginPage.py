class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_id = 'user-name'
        self.password_id = 'password'
        self.login_btn   = 'login-button'

    def enter_uname(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn).click()