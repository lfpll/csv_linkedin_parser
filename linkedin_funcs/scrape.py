from bots_parser.buttons_inputs import click_everything
from find.generic_functions import treat_text
from bots_parser.general import scroll_all_page
from find.education import parse_edu_field
from find.jobs import parse_multiple_jobs,parse_single_job
from find.skills import parse_skill_field
from bs4 import BeautifulSoup
from time import sleep
import re
import collections


# Scrape the user page
## Returning the lists with experience,education and skills
def user_page(driver, url):
    def general_info(element):

        person = dict()
        person['name'] = treat_text(element.find('h1', 'pv-top-card-section__name'))
        person['description'] = treat_text(element.find('h2', 'pv-top-card-section__headline'))
        person['location'] = treat_text(element.find('h3', 'pv-top-card-section__location'))

        return person

    # Switching for the different patterns of experience fields
    def switch_scrape_job(li_element):
        list_h3 = li_element.find_all('h3')
        if len(list_h3) > 1:
            return parse_multiple_jobs(li_element)
        elif len(list_h3) == 1:
            return parse_single_job(li_element)
        else:
            raise Exception('Not valid experience area')

    def flatten(list_lists_dict):
        flattend = []
        for item in list_lists_dict:
            if isinstance(item, list):
                flattend.extend(item)
            else:
                flattend.append(item)
        return flattend

    # Load all the dynamical content of the page
    scroll_all_page(driver=driver)
    click_everything(element=driver,xpath="//*[contains(text(),'Visualizar mais') and not(contains(@style,'display:none'))]")
    click_everything(element=driver,xpath="//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")

    soup = BeautifulSoup(driver.page_source,'lxml')

    # Div with the top info about the user
    gen_info_dict = general_info(element=soup)

    # Getting the fields that are important
    experience_list = soup.find_all('h2', text=re.compile('Experiência\s+(?!\w)'))[0].find_parent('section').find_all(
        'li', class_='pv-profile-section')
    edu_list = soup.find_all('h2', text=re.compile('Formação acadêmica.*'))[0].find_parent('section').find_all('li',
                                                                                                               class_='pv-profile-section__list-item')
    skills_list = [parse_skill_field(para.find_parent('div')) for para in
                   soup.find_all('p', class_='pv-skill-category-entity__name')]

    edu_list = flatten([parse_edu_field(edu_field) for edu_field in edu_list])

    experience_list = flatten([switch_scrape_job(exp_field) for exp_field in experience_list])

    return gen_info_dict, edu_list, experience_list, skills_list
