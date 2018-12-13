from input_click import input_value,click_button,click_button_by_filter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  

import itertools
from selenium import webdriver
import get_csv
import sys
import time


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1hhqywuvU_LlH-AkASWcRVcBUCOvWSZBGz1T26xAzog0'
RANGE_NAME = 'Participantes!A:A'


def fix_url(url):
	if url.find('http') >-1:
		return url
	return 'http://'+url

linkedin_list = get_csv.gen_list(credentials_file='./credentials.json',sheet_id=SPREADSHEET_ID,range=RANGE_NAME,scope=SCOPES)
linkedin_list = list(filter(lambda x:x.find('linkedin') > -1,list(itertools.chain.from_iterable(linkedin_list))))
linkedin_list = [fix_url(url) for url in linkedin_list]

chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome()
wait = WebDriverWait(driver,20)
driver.get('http://linkedin.com')

# Get the values of the element candidate
def scrape_info(candidate_obj,element):	
	candidate_obj['name'] = element.find_elements_by_css_selector('h1')
	candidate_obj['position'] = element.find_elements_by_css_selector('h2')
	candidate_obj['city'] = element.find_elements_by_css_selector('h3')

# Get the jobs of the candidate
def parse_jobs(candidate_obj,experiencia):
	h4_s = experiencias.find_elements_by_css_selector('h4')
	company,city = h4_s[0].text,h4_s[1].text
	job_function = experiencias.find_elements_by_css_selector('div.display-flex').text
	job_name = experiencias.find_element_by_css_selector('h3').text
	info 	 = experiencias.find_element_by_css_selector('h3').text
	candidate_obj['jobs'].append({'job_name':job_name,'company':company,'city':city,'job_function':job_function,'info':info})

# Login
login = 'luizfpll@gmail.com'
password = input('Input the password: ')

input_value(wait_obj=wait,text_input=login,input_css='input.login-email',element=driver)
input_value(wait_obj=wait,text_input=password,input_css='input.login-password',element=driver,enter=True)

# Add a person based on only the text filters.
def add_person(url):
	driver.get(url)	
	try:
		click_button_by_filter(element=driver,text='Conectar')
	except Exception as error:
		print(error)
		return 
	time.sleep(2)
	click_button_by_filter(element=driver,text='Enviar agora')
	time.sleep(2)


for linkedin_url in linkedin_list:
	print(linkedin_url)
	add_person(linkedin_url)
