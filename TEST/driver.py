from selenium import webdriver

def test():
    # driver=webdriver.Chrome("C:/Users/da/AppData/Local/Google/Chrome/Application/chromedriver.exe")
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    # driver.get('https://www.baidu.com')
    # print("----"*10)
    driver.get('https://tgtest.taogongscm.com/console/?ctl=passport')
    driver.maximize_window()
    driver.find_element_by_name('uname').send_keys('lint236')
    driver.find_element_by_name('password').send_keys('Dunan123')
    driver.find_element_by_css_selector('.btn.btn-success.uppercase').click()
    driver.implicitly_wait(10)
    text = driver.find_element_by_link_text("您好")
    print(text)
    try:
        driver.implicitly_wait(10)
        text.getText().contains('您好')
        print('Login success')
    except:
        print('Not found!')
        pass


test()