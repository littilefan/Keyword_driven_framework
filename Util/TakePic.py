from Conf.ProjVar import *
from Util.Dir import *
from Util.DateAndTime import *
from selenium import webdriver
def take_pic(driver):
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

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="e:\\chromedriver")
    driver.get("http://www.sohu.com")
    take_pic(driver)