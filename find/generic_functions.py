import re 
space = re.compile('\s+')

def treate_text(html_tag):
	return re.sub(space,' ',html_tag.text.replace('\n',' ').strip())

# Return the span text that is interesting
def get_spans_text(p_element,index= None):
	# Return a specif value or entire list depending on index
	if index is None:
		return [treate_text(span) for span in p_element.find_all('span')]
	else:
		return treate_text(p_element.find_all('span')[index])
