#encoding=utf-8
import configparser

def read_ini_file_all_sections(ini_file_path):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path,encoding="utf-8-sig")
    return cf.sections()

def read_ini_file_section_all_options(ini_file_path,section_name):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding="utf-8-sig")
    return cf.options(section_name)

def read_ini_file_option(ini_file_path,section_name,option_name):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding="utf-8-sig")
    try:
        value = cf.get(section_name,option_name)
    except:
        print ("the specific seciton or the specific option doesn't exit!")
        return None
    else:
        return value

if __name__ == "__main__":
    ini_file_path = r"E:\2020_4_data_driven_framework\Conf\PageElementLocator.ini"
    print(read_ini_file_all_sections(ini_file_path))
    print(read_ini_file_section_all_options(ini_file_path,'126mail_addContactsPage'))
    print(read_ini_file_option(ini_file_path,'126mail_addContactsPage','addcontactspage.contactpersonemail'))
