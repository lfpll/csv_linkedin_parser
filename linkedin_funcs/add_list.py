from bots_parser.buttons_inputs import click_button_by_filter
import itertools
import sys
import time

first_button_text = 'Conectar'
secnd_button_text =	'Enviar agora'

# Receives a list of urls and add everybody 
def people(driver,linkedin_url_list):

	def add_person(url):
		driver.get(url)	
		try:
			click_button_by_filter(element=driver,text=first_button_text)
		except Exception as error:
			print(error)
			return 
		time.sleep(2)
		click_button_by_filter(element=driver,text=secnd_button_text)
		time.sleep(2)


	for linkedin_url in linkedin_url_list:
		print(linkedin_url)
		add_person(linkedin_url)
