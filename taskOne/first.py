from selenium import webdriver

driver = webdriver.Chrome("drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://learn-staging.byjus.com/login")

driver.find_element_by_xpath("//*[@id='root']/div/div/a/span[1]").click()
driver.implicitly_wait(3)
driver.find_element_by_id("enterNumber").send_keys("3333333312")
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[3]/button/div").click()
driver.implicitly_wait(5)

driver.find_element_by_name("user[password]").send_keys("123456")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@id='mobile-login-form']/div/button/div").click()
