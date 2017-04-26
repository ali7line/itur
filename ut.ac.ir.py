from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_info(*args):
    browser = webdriver.PhantomJS()
    browser.implicitly_wait(5)
    browser.get('http://acct.ut.ac.ir')

    username_input , password_input, *_ = browser.find_elements_by_tag_name('input')
    username, password = args
    password += '\n'

    username_input.send_keys(username)
    password_input.send_keys(password)

    user_ = browser.find_elements_by_class_name("Form_Content_Row_Right_2Col_light")
    print("{} : {}".format(user_[0].text, user_[1].text))

    browser.quit()


if __name__ == '__main__':
    if len(argv) == 3:
        _, username, password = argv
        get_info(username, password)
    else:
        raise "input user pass as input ;)"
