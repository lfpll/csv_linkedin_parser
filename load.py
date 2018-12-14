from bots_parser.general import scroll_all_page
from secure_vars import url_test,password,login
from bots_parser.buttons_inputs import input_value,click_everything
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def driver_chrome():
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_options=options)
	wait = WebDriverWait(driver,20)
	wait_buttons = WebDriverWait(driver,5)
	driver.get('http://linkedin.com')

	# Login
	input_value(wait_obj=wait,text_input=login,input_css='input.login-email',element=driver)
	input_value(wait_obj=wait,text_input=password,input_css='input.login-password',element=driver,enter=True)

	# Test url of someone
	driver.get(url_test)

	return driver