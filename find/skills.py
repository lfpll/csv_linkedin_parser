from find.generic_functions import treat_text

def parse_skill_field(element):
	text = treat_text(element.find('p'))
	span = element.find_all('span',class_='pv-skill-category-entity__endorsement-count')
	if len(span) >0:
		count = treat_text(span[0])
		return {'skill':text,'indications': count}
	return {'skill':text}

