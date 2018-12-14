from bots_parser.buttons_inputs import input_value,click_button_by_filter,click_everything
from bots_parser.general import filter_tag_by_text,scroll_all_page
from find_jobs import *
from secure_vars import url_test,password,login

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from selenium import webdriver

from random import random
import re

driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)
wait_buttons = WebDriverWait(driver,5)
driver.get('http://linkedin.com')

# Login
input_value(wait_obj=wait,text_input=login,input_css='input.login-email',element=driver)
input_value(wait_obj=wait,text_input=password,input_css='input.login-password',element=driver,enter=True)

# Test url of someone that has the pattern
driver.get(url_test)

def scroll_all_page(x = 0,last_height = driver.execute_script("return document.body.scrollHeight")):
	if x >= last_height:
		return
	else:
		driver.execute_script("window.scrollTo(0, "+str(x)+");")
		scroll_all_page(x=x+200*random(),last_height=driver.execute_script("return document.body.scrollHeight"))


# Check to if what pattern of parsing it is.
def check_continous_carreer(element):
	if len(element.find_all('h3')) >0:
		return false
	return true


scroll_all_page()
click_everything(element=driver,xpath="//a[contains(text(),'Visualizar mais') and not(contains(@style,'display:none'))]")
click_everything(element=driver,xpath="//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")


soup = BeautifulSoup(driver.page_source)
experience_list = soup.find_all('h2',text=re.compile('Experiência\s+(?!\w)'))[0].find_parent('section').find_all('li',class_='pv-profile-section')


for li_exp in experience_list:
	list_h3 = li_exp.find_all('h3')
	print('aee %s'%list_h3[0].text)
	if len(list_h3) > 1:
		print(multiple.parse(li_exp,user_id=1))
	elif len(list_h3) == 1:
		print(only_one.parse_single_job(li_exp,user_id=1))
	else:
		raise Exception('Not valid experience area')





