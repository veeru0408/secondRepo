
from selenium import webdriver


driver = webdriver.Chrome("drivers/chromedriver.exe")
#driver.get("https://learn-staging.byjus.com/login")
driver.get("https://www.facebook.com/")


driver.implicitly_wait(5)
driver.find_element_by_id("email").send_keys("veeruk@gmail.com")
driver.implicitly_wait(5)

driver.find_element_by_name("pass").send_keys("Veeru")
driver.implicitly_wait(5)


#driver.find_element_by_xpath("//*[@id='u_0_d_g5']").click()
#driver.find_element_by_xpath("//button[@name=‘login’]").click()
#driver.find_element_by_name("login").click()
driver.find_element_by_xpath("//*[contains(text(),‘Log In’)]").click()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome('drivers/chromedriver.exe')
#
# driver.set_page_load_timeout("10")
# driver.get("https://learn-staging.byjus.com/login")
# driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
# driver.find_element_by_id("enterNumber").send_keys("11111")
#
# driver.find_element_by_class_name("nextButtonLanding").click()

