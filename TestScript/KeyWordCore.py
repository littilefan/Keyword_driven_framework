from Util.Excel import *
from Util.Log import info
from Util.TakePic import take_pic
from Conf.ProjVar import *
from Action.Action import  *
from Util.DateAndTime import *

"""
test_case_info_sheet = "126账号"
test_result_sheet = "测试结果"
index_col_no = 0
test_case_description_col_no = 1
test_steps_sheet_name_col_no =2
is_test_executed_flag_col_no = 3
test_time_col_no =4
test_result_col_no =5

test_step_index_col_no = 0
test_step_description_col_no =1
keyword_col_no=2
locator_col_no =3
value_col_no =4
is_test_step_executed_flag_col_no = 5
test_step_time_col_no =6
test_result =7
"""
def get_test_info(excel_file_path,sheet_name):
    wb = ExcelUtil(excel_file_path)
    wb.set_sheet_by_name(sheet_name)
    return wb.get_sheet_all_data()

def execute_test_case():
    # print(get_test_info(test_data_file_path,test_case_info_sheet))
    wb = ExcelUtil(test_data_file_path)
    test_cases = get_test_info(test_data_file_path, test_case_info_sheet)

    for testcase in test_cases[1:]:
        test_step_sheet_name = testcase[test_steps_sheet_name_col_no]
        if "y" in testcase[is_test_executed_flag_col_no].lower():
            # print("要执行的sheet name:",test_step_sheet_name)
            test_steps_info = get_test_info(test_data_file_path, test_step_sheet_name)
            # print("所有的测试步骤：",test_steps_info)
            wb.set_sheet_by_name(test_result_sheet)
            wb.write_a_line_in_sheet(test_steps_info[0], fgcolor="CD9B9B") #写测试结果表头
            for test_step in test_steps_info[1:]:
                flag = True
                test_step_description = test_step[test_case_description_col_no]
                keyword = test_step[keyword_col_no]
                locator = test_step[locator_col_no]
                value = test_step[value_col_no]
                if "y" in test_step[is_test_step_executed_flag_col_no].lower():

                    if locator is None and value is None:
                        command = keyword + "()"
                    elif locator is not None and value is None:
                        command = "%s('%s')" % (keyword, locator)
                    elif locator is None and value is not None:
                        command = "%s('%s')" % (keyword, value)
                    else:
                        command = "%s('%s','%s')" % (keyword, locator, value)
                    print("------------:", command)
                    test_step[test_step_time_col_no] = TimeUtil().get_chinesedatetime()
                    try:
                        temp = eval(command)
                        if "open_browser" in command:
                            driver = temp
                        test_step[test_step_result_col_no] = "成功"
                    except AssertionError as e:
                        print("断言失败")
                        flag = False
                        test_step[test_step_result_col_no] = "断言失败"
                        take_pic(driver)
                        wb.write_a_line_in_sheet(test_step, font_color="red")
                        break
                    except Exception as eak:
                        print("突发异常")
                        flag = False
                        test_step[test_step_result_col_no] = "异常失败"
                        take_pic(driver)  #Action文件中的drive变量是""
                        wb.write_a_line_in_sheet(test_step, font_color="red")
                        break
                    wb.write_a_line_in_sheet(test_step, font_color="green")
                    wb.set_sheet_by_name(test_result_sheet)

            testcase[test_time_col_no] = TimeUtil().get_chinesedatetime()
            if flag is True:
                print("所有测试步骤执行成功")
                testcase[test_result_col_no] = "成功"
                wb.write_a_line_in_sheet(test_cases[0], fgcolor="CD9B9B")
                wb.write_a_line_in_sheet(testcase, font_color="green")
            else:
                print("测试步骤出现执行失败")
                testcase[test_result_col_no] = "失败"
                wb.write_a_line_in_sheet(test_cases[0], fgcolor="CD9B9B")
                wb.write_a_line_in_sheet(testcase, font_color="red")
            wb.save()

        else:
            print("不执行的sheet name:", test_step_sheet_name)


