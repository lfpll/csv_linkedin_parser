import load
import pprint
import mongo_connection
from bson import ObjectId
from linkedin_funcs import scrape
from secure_vars import url_test, login, password
from bots_parser.buttons_inputs import input_value

driver, wait = load.driver_chrome(url='https://www.linkedin.com/')

# Login
input_value(wait_obj=wait, text_input=login, input_css='input.login-email', element=driver)
input_value(wait_obj=wait, text_input=password, input_css='input.login-password', element=driver, enter=True)

# Receives the data about the person page
# Gets the person general info name, position description and location
# A list of dicts of the education path
# A list of dicts of all the jobs
# A list of dicts of all skills listed
person_info, edu_list, jobs_list, skills_list = scrape.user_page(driver=driver, url=url_test)
driver.close()
person_info['skills'] = skills_list
mdb_obj = mongo_connection.insert_data(option='people', data=person_info)


def add_id(p_id, add_id):
    add_id['p_id'] = p_id
    return add_id

edu_list = [add_id(add_id=edu_dict,p_id=mdb_obj) for edu_dict in edu_list]
jobs_list = [add_id(add_id=job_dict,p_id=mdb_obj) for job_dict in jobs_list]

mongo_connection.insert_data(option='education',data=edu_list)
mongo_connection.insert_data(option='experience',data=jobs_list)