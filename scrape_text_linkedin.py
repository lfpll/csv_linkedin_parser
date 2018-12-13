from input_click import input_value,click_button_by_filter,filter_tag_by_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
from random import random


driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)
wait_buttons = WebDriverWait(driver,5)
driver.get('http://linkedin.com')

# Login
login = 'luizfpll@gmail.com'
password = input('Type your password: ')

input_value(wait_obj=wait,text_input=login,input_css='input.login-email',element=driver)
input_value(wait_obj=wait,text_input=password,input_css='input.login-password',element=driver,enter=True)
driver.get('https://www.linkedin.com/in/marcelo-rosa-ab18ab/')


def click_button(xpath):
	buttons = driver.find_elements_by_xpath(xpath)
	if len(buttons) >0:
		buttons[0].click()

def scroll_all_page(x = 0,last_height = driver.execute_script("return document.body.scrollHeight")):
	click_button("//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")
	if x >= last_height:
		return
	else:
		driver.execute_script("window.scrollTo(0, "+str(x)+");")
		scroll_all_page(x=x+100*random(),last_height=driver.execute_script("return document.body.scrollHeight"))

# Check to if what pattern of parsing it is
def check_continous_carreer(element):
	if len(element.find_all('h3')) >0:
		return false
	return true

def treat_text(text):
	return text.replace('\n',' ').split()

def parse_job(element):
	job = {}
	job['title'] = element.find('h3').text
	job_time  = [ treat_text(span.text) for span in element.find('div',class_='display-flex').find_all('span')]
	job['location'] = element.find('h4',class_='pv-entity__location t-14 t-black--light t-normal block').text
	job_time[]

# Parse jobs people that change works while in the same company
def parse_continous_carrer(element,user_id):

	# The css class for the name and total time at company 
	css_class = 'pv-entity__logo company-logo'
	attributes = [ treat_text(span.text) for span in element.find('div',class_=css_class).find_all('span')]
	
	if attributes[0] != 'Nome da empresa':
		raise('This style is not what was expected')
	else:
		# Gets company and total time using dynamic keys for different languages
		company_name = attributes[1]
	# Parsing the job roles that the person has worked
	role_class = 'pv-entity__role-details-container'
	child_divs = element.find_all(role_class)


scroll_all_page()

souṕ = BeautifulSoup(driver.page_source)
lis_companys = soup.find_all('header')[0].find_parent('section').find_all('li')
# pegar pelo span hidden

