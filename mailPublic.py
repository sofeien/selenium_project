class Mail():
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("http://mail.126.com/")
        self.driver.implicitly_wait(10)
    def log_in(self,name,password):
        self.driver.find_element_by_css_selector("#lbNormal").click()
        self.driver.switch_to.frame("x-URS-iframe")
        self.driver.find_element_by_css_selector("input[name='email']").send_keys(name)
        self.driver.find_element_by_css_selector("input[name='password']").send_keys(password)
        self.driver.find_element_by_id("dologin").click()
        self.driver.switch_to.default_content()
    def log_out(self):
        self.driver.find_element_by_css_selector("#_mail_component_41_41 > a:nth-child(1)").click()
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    from selenium import webdriver
    import time
    from selenium.webdriver.support.ui import WebDriverWait

    driver = webdriver.Firefox()
    mail_driver = Mail(driver)
    username="123456"
    password="123465"
    mail_driver.log_in(username,password)
    name = WebDriverWait(driver,10).until(lambda d: d.find_element_by_id("spnUid"))
    assert name.text == "123456"
    mail_driver.log_out()
        
