import load
import pprint
import mongo_connection
from linkedin_funcs import scrape
from secure_vars import url_test, login, password
from bots_parser.buttons_inputs import input_value

driver, wait = load.driver_chrome(url='https://www.linkedin.com/')

# Login
input_value(wait_obj=wait, text_input=login, input_css='input.login-email', element=driver)
input_value(wait_obj=wait, text_input=password, input_css='input.login-password', element=driver, enter=True)

# Add parent id to object
def add_id(p_id, add_id):
    add_id['p_id'] = p_id
    return add_id

def insert_data(driver,url_person):
    print(url_person)
    driver.get(url_person)
    if driver.current_url == r'https://www.linkedin.com/in/unavailable/':
        return
    # Receives the data about the person page
    # Gets the person general info name, position description and location
    # A lists of dicts of all of the education path,all of the jobs and all of the skills
    person_info, edu_list, jobs_list, skills_list = scrape.user_page(driver=driver,url=url_person)
    person_info['skills'] = skills_list
    person_info['url'] = url_person
    # Inserting data and getting the id
    person_id = mongo_connection.insert_data(option='people', data=person_info)

    # Adding parent id to the data
    edu_list = [add_id(add_id=edu_dict, p_id=person_id) for edu_dict in edu_list]
    jobs_list = [add_id(add_id=job_dict, p_id=person_id) for job_dict in jobs_list]

    mongo_connection.insert_data(option='education',data=edu_list)
    mongo_connection.insert_data(option='experience',data=jobs_list)


from gsheet import return_list
list_users = return_list()
users_in = [mongo_obj['url'] for mongo_obj in list(mongo_connection.get_list('people',attribute='url'))]
list_users = list((filter(lambda user: user not in users_in,list_users)))

for user_url in list_users:
    insert_data(driver=driver,url_person=user_url)