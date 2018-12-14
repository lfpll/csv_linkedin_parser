from bots_parser.buttons_inputs import click_everything
from bots_parser.general import scroll_all_page
from find.education import parse_edu_field
from find.jobs import *
from find.skills import parse_skill_field
from bs4 import BeautifulSoup
from time import sleep

# Scrape the user page
## Returning the lists with experience,education and skills
def user_page(driver,url):	

	# Switching for the different patterns of experience fields
	def switch_scrape_job(li_element):
		list_h3 = li_element.find_all('h3')
		if len(list_h3) > 1:
			return multiple.parse(li_element)
		elif len(list_h3) == 1:
			return parse_single_job(li_element)
		else:
			raise Exception('Not valid experience area')

	
	
	driver.get(url)

	# Load all the dynamical content of the page
	scroll_all_page(driver=driver)
	click_everything(element=driver,xpath="//a[contains(text(),'Visualizar mais') and not(contains(@style,'display:none'))]")
	click_everything(element=driver,xpath="//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")
	sleep(2)

	soup = BeautifulSoup(driver.page_source)

	# Getting the fields that are important
	experience_list = soup.find_all('h2',text=re.compile('Experiência\s+(?!\w)'))[0].find_parent('section').find_all('li',class_='pv-profile-section')
	edu_list = soup.find_all('h2',text=re.compile('Formação acadêmica.*'))[0].find_parent('section').find_all('li',class_='pv-profile-section__list-item')
	skills_list = [parse_skill_field(para.find_parent('div')) for para in soup.find_all('p',class_='pv-skill-category-entity__name')]

	edu_list = [parse_edu_field(edu_field) for edu_field in edu_list]
	experience_list = [switch_scrape_job(exp_field) for exp_field in experience_list]
		
	return edu_list,experience_list,skills_list
