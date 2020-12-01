import os
from Util.DateAndTime import *
from Conf.ProjVar import *

def make_dir(dir_path):
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            print("创建目录 %s 成功" %dir_path)
        except:
            print("创建目录 %s 不成功" %dir_path )

def make_time_dir():
    date = TimeUtil().get_chinesedate()
    dir_path = os.path.join(proj_path,"ScreenPics")
    dir_path = os.path.join(dir_path,date)
    dir_path =  os.path.join(dir_path,str(TimeUtil().get_hour()))
    make_dir(dir_path)
    return dir_path

if __name__ == "__main__":
    make_time_dir()
