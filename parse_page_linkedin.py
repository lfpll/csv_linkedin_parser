from bs4 import BeautifulSoup

# Return a valid list if is the right size
def check_if_valid(soup,tag,classes=None,size=1):
	if classes is not None:
		tags_list = soup.find_all(tag,class_=classes)
	else:
		tags_list = soup.find_all(tag)
	if len(tags_list) == size:
		return tags_list
	else:
		raise(Exception("Array bigger or smaller then expected"))


# Return the first section info
## Name, Actity, City
def parse_info_sec(info_obj,soup_obj):
	info_obj['name'] = check_if_valid(soup=soup_obj,tag='h1')[0].text
	info_obj['activity'] = check_if_valid(soup=soup_obj,tag='h2')[0].text
	info_obj['city'] = check_if_valid(soup=soup_obj,tag='h3')[0].text
	return info_obj

def get_last_div(div):
	div_list = div.findChildren('div')
	return [div for div in div_list if len(div.find_all('div')) == 0]

def single_experience(soup_obj,job_obj):
	city_class = "pv-entity__location t-14 t-black--light t-normal block" 
	job_obj['position'] = check_if_valid(soup=soup_obj,tag='h3',size=1)[0]
	job_obj['company']  = check_if_valid(soup=soup_obj,tag='h4',size=1)[0]
	job_obj['time'] 	= check_if_valid(soup=soup_obj,tag="h4",classes="display-flex",size=1)[0]
	job_obj['city'] 	= check_if_valid(soup=soup_obj,tag="h4",classes=city_class,size=1)[0]
	definition = check_if_valid(soup=soup_obj,tag="p",size=1)
	job_obj['definition'] = definition[0] if len(paragraphh) >0 else ""

# Parse the experience of linkedin
def parse_experience(info_obj,soup_obj):

	def parse_exp_block(soup_obj):

		# For people that have more than one job in a company
		## Parser method changes	
		if soup_obj.find_all('h3') == 1:
			single_experience(soup_obj)					
		else:
	for li_item in lis_companys:
		parse_exp_block

# Scroll the page of the user and clicks on the buttons to show all the data
def scroll_all_page(x = 0,last_height = driver.execute_script("return document.body.scrollHeight")):

	def click_button(xpath):
		print(xpath)
		buttons = driver.find_elements_by_xpath(xpath)
		if len(buttons) >0:
			buttons[0].click()

	click_button("//*[contains(text(),'Exibir mais') and not(contains(@style,'display:none'))]")
	if x >= last_height:
		return
	else:
		driver.execute_script("window.scrollTo(0, "+str(x)+");")
		scroll_all_page(x=x+100*random(),last_height=driver.execute_script("return document.body.scrollHeight"))



scroll_all_page()


css_info_sec = "pv-profile-section pv-top-card-section artdeco-container-card ember-view"
souṕ = BeautifulSoup(driver.page_source)
lis_companys = soup.find_all('header')[0].find_parent('section').find_all('li')