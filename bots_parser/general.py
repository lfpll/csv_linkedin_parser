from random import random

# Return button by filter function
def filter_tag_by_text(element,text,element_name,notSingle=True):
	tag_list = element.find_elements_by_css_selector(element_name)
	tag_list 	= list(filter(lambda single_elem: single_elem.text.find(text) >-1,tag_list))
	if notSingle:
		return tag_list
	if len(tag_list) == 0:
		return tag_list
	else:
		raise(Exception('Nothing found'))


# Scroll all the way to the bottom of the page
## Loads all the data of dynamical rendered pages
def scroll_all_page(driver):

	def scroll_recursive(x = 0,last_height = driver.execute_script("return document.body.scrollHeight")):
		if x >= last_height:
			return
		else:
			driver.execute_script("window.scrollTo(0, "+str(x)+");")
			scroll_recursive(x=x+100*random(),last_height=driver.execute_script("return document.body.scrollHeight"))

	scroll_recursive()