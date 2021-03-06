from find.generic_functions import *

# Get the information from the field with education information
## Gets the different attributes by classes ang tags
def parse_edu_field(element):
	education_obj = {}
	school_name = element.find_all('h3',class_='pv-entity__school-name')
	if len(school_name) != 1:
		raise Exception('Invalid field of school')
	education_obj['School Name'] = treat_text(school_name[0])

	# Get the graduation info of the course
	grad_descrps = element.find_all('p',class_="pv-entity__secondary-title")
	if len(grad_descrps)>0:
		grad_descrps = [get_spans_text(p) for p in grad_descrps]
		for descrpt in grad_descrps:
			education_obj[descrpt[0]] = descrpt[1]

	date_info = element.find_all('p',class_='pv-entity__dates')
	if len(date_info) >0:
		date_info = get_spans_text(date_info[0])
		education_obj[re.sub('\s\(.*\)','',date_info[0])] = date_info[1]

	description = element.find_all("p",class_="pv-entity__description")
	if len(description) >0:
		education_obj['description'] = treat_text(description[0])
	return education_obj