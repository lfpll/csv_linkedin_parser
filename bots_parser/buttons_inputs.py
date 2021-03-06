from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# Insert value in html input type
# There is two options if its by xpath and if it is by css_selector
## text_input  -> Values of text to be inserted on the <input>
## input_css or input_xpath -> The values of the selectors on their respective formats
## wait_obj -> The wait object of webdriver
def input_value(wait_obj,text_input,element,input_css=None,input_xpath=None,enter=False):

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
def click_button(wait_obj,element,button_css=None,button_xpath=None):

	if button_css is not None:
		wait_obj.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,button_css)))
		button_elements = element.find_elements_by_css_selector(button_css)
		if len(button_elements) != 1 :
			raise(Exception('This css_selector has 0 or more than 1 button_css in the page'))

	elif button_xpath is not None:
		wait_obj.until(EC.presence_of_all_elements_located((By.XPATH,button_xpath)))
		button_elements = element.find_elements_by_css_selector(button_xpath)
		if len(button_elements) != 1 :
			raise(Exception('This xpath has 0 or more than 1 buttons in the page'))
			
	else:
		raise( Exception('There is no css_selector or xpath_selector'))

		button_elements[0].click()

# Click one button by his text 
## Using on some sites that hide the tags and xpath is not working.
def click_button_by_filter(element,text,element_name='button'):
	button_list = element.find_elements_by_css_selector(element_name)
	filt_list 	= list(filter(lambda butt_elem: butt_elem.text.find(text) >-1,button_list))
	if len(filt_list) > 0:
		return filt_list[0].click()
	else:
		raise(Exception("Button can't be clicked"))

# Click everything that is passed by xpath
## Solve problems with not visible buttons
def click_everything(element,xpath):
	tent =0
	while tent<4:
		buttons = list(element.find_elements_by_xpath(xpath))
		if len(buttons) >0:
			try:
				[element.execute_script("arguments[0].click();", button) for button in buttons]
				break
			except Exception as e:
				print(e)
		sleep(2)
		tent += 1

