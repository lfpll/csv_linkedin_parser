from pymongo import MongoClient
from secure_vars import mongodb_url

# Insert the jobs on mongodb
def insert_data(option,data):
	client = MongoClient(mongodb_url)
	if option == 'education':
		coll = client['linkedin']['education']
		ins_val = coll.insert_many(data)
	elif option == 'experience':
		coll = client['linkedin']['experience']
		ins_val = coll.insert_many(data)
	elif option == 'people':
		coll = client['linkedin']['people']
		ins_val = coll.insert(data)
	else:
		raise Exception('This option doens\'t exist.')
		
	client.close()
	return ins_val


