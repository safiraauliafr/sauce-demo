class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.product_xpath  = '//img[@alt="Sauce Labs Backpack"]'
        self.addToChart_id  = 'add-to-cart-sauce-labs-backpack'
        self.cart_name      = 'shopping_cart_link'
        self.checkout_id    = 'checkout'
        self.firstName_id   = 'first-name'
        self.lastName_id    = 'last-name'
        self.zipCode_id     = 'postal-code'
        self.continue_id    = 'continue'
        self.finish_id      = 'finish'
        self.title_name     = 'complete-header'

    def click_product(self):        
        self.driver.find_element_by_id(self.addToChart_id).click()
        self.driver.find_element_by_xpath(self.product_xpath).click()
        self.driver.find_element_by_class_name(self.cart_name).click()
        self.driver.find_element_by_id(self.checkout_id).click()

    def fill_firstName(self, firstName):
        self.driver.find_element_by_id(self.firstName_id).send_keys(firstName)

    def fill_lastName(self, lastName):
        self.driver.find_element_by_id(self.lastName_id).send_keys(lastName)

    def fill_zipCode(self, zipCode):        
        self.driver.find_element_by_id(self.zipCode_id).send_keys(zipCode)

    def continue_shopping(self):
        self.driver.find_element_by_id(self.continue_id).click()
        self.driver.find_element_by_id(self.finish_id).click()
