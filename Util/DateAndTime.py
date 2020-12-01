import time
import datetime
import locale

class TimeUtil:
    def __init__(self, curtime=None):
        self.curtime = curtime

    def get_timestemp(self):
        return time.time()

    def get_date(self):
        return time.strftime("%Y-%m-%d")

    def get_time(self):
        return time.strftime("%H:%M:%S")

    def get_datetime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def get_chinesedate(self):
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        strTime = time.strftime("%Y年%m月%d日", time.localtime())
        return strTime

    def get_chinesetime(self):
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        strTime = time.strftime("%H时%M分%S秒", time.localtime())
        return strTime

    def get_chinesedatetime(self):
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        strTime = time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime())
        return strTime

    def compute_date(self, day_interval):
        # 获取今天的日期
        today = datetime.date.today()
        # 在今天的日期上再减10天
        if isinstance(day_interval, int) and day_interval >= 0:
            return today + datetime.timedelta(days=day_interval)
        elif isinstance(day_interval, int) and day_interval < 0:
            return today - datetime.timedelta(days=abs(day_interval))

    def timestamp_to_date(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            return None
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        time_tuple = time.localtime(timestamp)

        return str(time_tuple[0]) + "年" + str(time_tuple[1]) + "月" + str(time_tuple[2]) + "日"

    def timestamp_to_time(self, timestamp):
        if not isinstance(timestamp, (int, float)):
            return None
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        time_tuple = time.localtime(timestamp)
        return str(time_tuple[3]) + "时" + str(time_tuple[4]) + "分" + str(time_tuple[5]) + "秒"

    def timestamp_to_datetime(self, timestamp):
        return self.timestamp_to_date(timestamp) + self.timestamp_to_time(timestamp)

    def get_hour(self):
        return time.localtime().tm_hour

if __name__ == "__main__":
    t = TimeUtil()
    print(t.get_timestemp())
    print(t.get_date())
    print(t.get_time())
    print(t.get_datetime())
    print(t.get_chinesedate())
    print(t.get_chinesetime())
    print(t.get_chinesedatetime())
    print(t.compute_date(10))
    print(t.compute_date(-10))
    print(t.timestamp_to_date(1333333333))
    print(t.timestamp_to_time(1333333333))
    print(t.timestamp_to_datetime(1333333333))
    print(t.get_hour())

