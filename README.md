# Keyword_driven_framework
UI自动化测试框架-关键字驱动

关键字驱动思想：

visit||http://www.sohu.com   
动作---->command = 'visit("http://www.sohu.com")'
eval(command)

def visit(url):

    driver.get(url)
    
