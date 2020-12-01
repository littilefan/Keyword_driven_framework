import time
import traceback
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

def find_element(driver,locate_method,locate_exp):
    try:
        element = WebDriverWait(driver, 10).until \
        (lambda x: x.find_element(locate_method,locate_exp))
    except TimeoutException as e:
        print("*******:",locate_method,locate_exp)
        # 捕获NoSuchElementException异常
        traceback.print_exc()
        raise e
    return element



def find_elements(driver,locate_method,locate_exp):
    try:
        elements = WebDriverWait(driver, 2).until \
        (lambda x: x.find_elements(locate_method,locate_exp))
    except TimeoutException as e:
        # 捕获NoSuchElementException异常
        traceback.print_exc()
        raise e
    return elements

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    driver.get("https://www.sogou.com")
    input_box = find_element(driver,"id","query")
    input_elements = find_elements(driver, "xpath", "//input")
    print(len(input_elements))
