from find.generic_functions import *

# Parse job li with one single job at the company
## There is hidden spans like <span id=key1>elem1</span><span id=key2>elem2</span>
## The list gives the values of the obj and the keys for future data quality checking
def parse_single_job(li_element,company=None):
	job = {}

	# Get the company name
	if company is None:
		title = treat_text(li_element.find('h3'))
		job['title'] = title
		comp_list = get_spans_text(p_element=li_element.find_all('h4')[0])
		job[comp_list[0]] = comp_list[1]
	else:
		title = get_spans_text(p_element=li_element.find('h3'))
		job[title[0]] = title[1]
		job['Nome da Empresa'] = company

	# Get the location of the job
	loc_class = 'pv-entity__location t-14 t-black--light t-normal block'
	location  =  li_element.find('h4',class_=loc_class)
	if isinstance(location,list) and len(location) >0:
		loc_list = get_spans_text(p_element=location)
		job[loc_list[0]] = loc_list[1]
	else:
		job['location'] = None

	# Parse Duration
	duration_spans = li_element.find_all('div',class_='display-flex')
	if len(duration_spans) >0:
		duration_spans  = [span_text for span_text in get_spans_text(duration_spans[0])]
		job[duration_spans[0]] = duration_spans[1]
		job[duration_spans[2]] = duration_spans[3]

	description = li_element.find_all('p')
	# Parse Description
	if isinstance(description,list) and len(description) >0:
			job['description'] = treat_text(description[0]).split('Visualizar')[0]

	return job

# Parse jobs of people that change works while in the same company
def parse_multiple_jobs(li_element):

	# The css class for the name and total time at company 
	css_class = 'pv-entity__company-details'
	attributes = [span_text for span_text in get_spans_text(li_element.find('div',class_=css_class))]
	
	if attributes[0] != 'Nome da empresa':
		raise Exception('This style is not what was expected')
	else:
		company_name = attributes[1]

	# Parsing the job roles that the person has worked
	role_class = 'pv-entity__role-details-container'
	child_divs = li_element.find_all('div',class_=role_class)

	list_of_jobs = [parse_single_job(div,company=company_name) for div in child_divs]
	return list_of_jobs
	



