# Insert value in html input type
# There is two options if its by xpath and if it is by css_selector
## text_input  -> Values of text to be inserted on the <input>
## input_css or input_xpath -> The values of the selectors on their respective formats
## wait_obj -> The wait object of webdriver
def input_value(wait_obj,text_input,element=driver,input_css=None,input_xpath=None,enter=False):

	if input_css is not None:
		wait_obj.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,input_css)))
		input_elements = element.find_elements_by_css_selector(input_css)
		# Handling if there is more then one input with the same css_selecotr
		if len(input_elements) != 1:
			raise(Exception('This css_selector has 0 or more than 1 inputs in the page'))

	elif input_xpath is not None:
		wait_obj.until(EC.presence_of_all_elements_located(By.XPATH,input_xpath))
		input_elements = element.find_elements_by_xpath(input_xpath)
		if len(input_elements) != 1:
			raise(Exception('This xpath has 0 or more than 1 inputs in the page'))

	else:
		raise( Exception('There is no css_selector or xpath_selector'))

	input_elements[0].click()
	input_elements[0].send_keys(text_input)

	if enter:
		input_elements[0].send_keys(Keys.ENTER)


# Click a html button with specific css tag or xpath o
def click_button(button_css=None,button_xpath=None,element=driver):
	if button_css is not None:
		button_elements = element.find_elements_by_css_selector(button_css)
		if len(button_elements) >0:
			raise(Exception('This css_selector has 0 or more than 1 button_css in the page'))
	elif button_xpath is not None:
		button_elements = element.find_elements_by_css_selector(button_xpath)
		if len(button_elements) >0:
			raise(Exception('This xpath has 0 or more than 1 buttons in the page'))
	else:
		raise( Exception('There is no css_selector or xpath_selector'))



