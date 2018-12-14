from generic_functions import treate_text

def parse_skill(element):
	text = treate_text(element.find('p'))
	span = element.find_all('span',class_='pv-skill-category-entity__endorsement-count')
	if len(span) >0:
		count = treate_text(span[0])
		return {'skill':text,'value': count}
	return {'skill':text}

