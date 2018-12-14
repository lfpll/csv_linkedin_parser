import load 
from linkedin_funcs import scrape,add_list
from secure_vars import url_test
driver = load.driver_chrome()
print(scrape.user_page(driver=driver,url=url_test))