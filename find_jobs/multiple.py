import re
from find_jobs.only_one import parse_single_job,treate_text,get_spans_text


space = re.compile('\s+')


# Parse jobs people that change works while in the same company
def parse(li_element,user_id):
	# The css class for the name and total time at company 
	css_class = 'pv-entity__company-details'
	attributes = [span_text for span_text in get_spans_text(li_element.find('div',class_=css_class))]
	
	if attributes[0] != 'Nome da empresa':
		print(attributes)
		raise Exception('This style is not what was expected')
	else:
		company_name = attributes[1]
	# Parsing the job roles that the person has worked
	role_class = 'pv-entity__role-details-container'
	child_divs = li_element.find_all('div',class_=role_class)

	list_of_jobs = [parse_single_job(div,company=company_name,user_id=user_id) for div in child_divs]
	return list_of_jobs
	
