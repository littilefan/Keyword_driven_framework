import os
import time
import traceback

from Conf.ProjVar import PageElementLocator_file_path
from Util.Dir import make_time_dir, TimeUtil
from Util.ParseConfig import read_ini_file_option
from selenium import webdriver
from Util.ObjectMap import find_element
from Util.ParseConfig import *

driver = ""

def is_xpath(exp):
    if ("//" in exp) or ("[" in exp) or ("@" in exp):
        return True
    return False


def get_element(driver,locator_exp):
    print("当前定位的section和option:",locator_exp)
    section_name = locator_exp.split(",")[0]
    option_name = locator_exp.split(",")[1]
    element_locator = read_ini_file_option(
        PageElementLocator_file_path, section_name, option_name)
    element = find_element(
        driver, element_locator.split(">")[0], element_locator.split(">")[1])
    return element

def open_browser(browser_name):
    global driver
    if "ie" in browser_name.lower():
        driver  = webdriver.Ie(executable_path="E:\\browserDriver\\IEDriverServer")
    elif "chrome" in browser_name.lower():
        driver  = webdriver.Chrome(executable_path="E:\\browserDriver\\chromedriver")
    else:
        driver = webdriver.Firefox(executable_path="E:\\browserDriver\\geckodriver")
    return driver

def visit(url):
    global driver
    driver.get(url)

def input(xpath_exp,content):
    global  driver
    if is_xpath(xpath_exp):
        element = driver.find_element_by_xpath(xpath_exp)
        element.send_keys(content)
    else:
        element = get_element(driver,xpath_exp)
        element.send_keys(content)

def click(xpath_exp):
    global  driver
    if is_xpath(xpath_exp):
        element = driver.find_element_by_xpath(xpath_exp)
        element.click()
    else:
        element = get_element(driver,xpath_exp)
        element.click()

def sleep(seconds):
    time.sleep(float(seconds))

def assert_word(expected_word):
    global  driver
    assert expected_word in driver.page_source

def switch_to(xpath_exp):
    global driver
    if is_xpath(xpath_exp):
        driver.switch_to.frame(driver.find_element_by_xpath(xpath_exp))
    else:
        element = get_element(driver,xpath_exp)
        driver.switch_to.frame(element)

def switch_back():
    global driver
    driver.switch_to.default_content()

def quit():
    global  driver
    driver.quit()

def take_pic(driver):
    print("***************",driver)
    try:
        '''
        调用get_screenshot_as_file(filename)方法，对浏览器当前打开页面
        进行截图,并保为C盘下的screenPicture.png文件。
        '''
        file_path = make_time_dir()
        pic_path = os.path.join(file_path,TimeUtil().get_chinesetime()+".png")
        result = driver.get_screenshot_as_file(pic_path)
        print(result)
    except IOError as e:
        print(e)

if __name__ =="__main__":
    #driver = login("testman1980","wulaoshi1978")
    #open_browser("ie")
    #open_browser("firefox")
    try:
        open_browser("chrome")
        visit("http://mail.126.com")
        # click("126mail_login,loginPage.loginlink")
        switch_to("126mail_login,loginPage.frame")
        input("126mail_login,loginPage.username","testman2020")
        input("126mail_login,loginPage.password","wulaoshi1978")
        click("126mail_login,loginPage.loginbutton")
        # switch_back()
        # sleep(10)
        # assert_word("通讯录")
        # click("126mail_homePage,homePage.addressbook")
        # sleep(1)
        # click("126mail_addContactsPage,addContactsPage.createContactsBtn")
        # input("126mail_addContactsPage,addContactsPage.contactPersonName","张三")
        # input("126mail_addContactsPage,addContactsPage.contactPersonEmail","33r23r2@qq.com")
        # click("126mail_addContactsPage,addContactsPage.starContacts")
        # input("126mail_addContactsPage,addContactsPage.contactPersonMobile","1111111111")
        # input("126mail_addContactsPage,addContactsPage.contactPersonComment","评论内容")
        # click("126mail_addContactsPage,addContactsPage.savecontacePerson")
        # sleep(5)
    except AssertionError as e:
        print("断言失败")
    except Exception as e:
        print("出现异常了",e)
        print("异常失败")
        traceback.print_exc();
    finally:
        quit()
