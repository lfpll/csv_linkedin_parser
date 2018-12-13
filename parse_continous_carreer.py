
# Simple normal treat_text used multiple times
def treate_text(html_tag):
	return html_tag	.text.replace('\n',' ').strip()

# Return the span text that is interesting
def get_spans_text(p_element,index= None):
	# Return a specif value or entire list depending on index
	if index is None:
		return [treate_text(span) for span in p_element.find_all('span')]
	else:
		return treat_text(p_element.find_all('span')[index].text)

def parse_job(element,user_id,company):
	job = {'company':company}

	# Title and location of the job
	job['title'] = get_spans_text(p_element=element.find('h3'),index=1)

	loc_class = 'pv-entity__location t-14 t-black--light t-normal block'
	job['location'] = get_spans_text(p_element=element.find('h4',class_=loc_class),index=1)
	
	# Takes the period and duration of this job
	job_time  = [span_text for span_text in get_spans_text(element.find('div',class_='display-flex'))]
	job[job_time[0]] = job_time[1]
	job[job_time[2]] = job_time[3]
	description = element.find_all('p')
	
	if len(description) >0:
		job['description'] = treate_text(description[0]).split('Visualizar')[0].strip()

	return job

# Parse jobs people that change works while in the same company
def parse(element,user_id):

	# The css class for the name and total time at company 
	css_class = 'pv-entity__company-details'
	attributes = [span_text for span_text in get_spans_text(element.find('div',class_=css_class))]
	
	if attributes[0] != 'Nome da empresa':
		print(attributes)
		raise Exception('This style is not what was expected')
	else:
		company_name = attributes[1]
	# Parsing the job roles that the person has worked
	role_class = 'pv-entity__role-details-container'
	child_divs = element.find_all('div',class_=role_class)

	list_of_jobs = [parse_job(div,company=company_name,user_id=user_id) for div in child_divs]
	print(list_of_jobs)
