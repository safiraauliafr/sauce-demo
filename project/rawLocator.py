from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()


driver.get('https://www.saucedemo.com/')
driver.find_element_by_id('user-name').send_keys('standard_user')
driver.find_element_by_id('password').send_keys('secret_sauce')
driver.find_element_by_id('login-button').click()
driver.implicitly_wait(3)

# add to chart
driver.find_element_by_xpath('//img[@alt="Sauce Labs Backpack"]').click()
driver.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
driver.find_element_by_class_name('shopping_cart_link').click()
driver.find_element_by_id('checkout').click()

# fill your information
driver.find_element_by_id('first-name').send_keys('Safira')
driver.find_element_by_id('last-name').send_keys('Aulia')
driver.find_element_by_id('postal-code').send_keys('17125')
driver.find_element_by_id('continue').click()
driver.find_element_by_id('finish').click()

# assert thank you 
title = driver.find_element_by_class_name('complete-header').text

assert title in "THANK YOU FOR YOUR ORDER"




# driver.close()
# driver.quit()

print('Tested')



