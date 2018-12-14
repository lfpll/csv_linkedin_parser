from secure_vars import url_test,password,login
from bots_parser.buttons_inputs import input_value,click_everything
from bots_parser.general import scroll_all_page
from find_jobs import *
from skills import parse_skill
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(driver,20)
wait_buttons = WebDriverWait(driver,5)
driver.get('http://linkedin.com')

# Login
input_value(wait_obj=wait,text_input=login,input_css='input.login-email',element=driver)
input_value(wait_obj=wait,text_input=password,input_css='input.login-password',element=driver,enter=True)

# Test url of someone that has the pattern
driver.get(url_test)

scroll_all_page(driver=driver)
click_everything(element=driver,xpath="//a[contains(text(),'Visualizar mais') and not(contains(@style,'display:none'))]")
click_everything(element=driver,xpath="//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")
sleep(2)



experience_list = soup.find_all('h2',text=re.compile('Experiência\s+(?!\w)'))[0].find_parent('section').find_all('li',class_='pv-profile-section')
edu_list = soup.find_all('h2',text=re.compile('Formação acadêmica.*'))[0].find_parent('section').find_all('li',class_='pv-profile-section__list-item')
skills_list = [parse_skill(para.find_parent('div')) for para in soup.find_all('p',class_='pv-skill-category-entity__name')]

# for edu in edu_list:
# 	print(parse_edu_field(edu,1))

# for li_exp in experience_list:
# 	list_h3 = li_exp.find_all('h3')
# 	if len(list_h3) > 1:
# 		print(multiple.parse(li_exp,user_id=1))
# 	elif len(list_h3) == 1:
# 		print(only_one.parse_single_job(li_exp,user_id=1))
# 	else:
# 		raise Exception('Not valid experience area')

driver.close()




