from secure_vars import mongodb_url
from pymongo import MongoClient
import pandas as pd
import re
from general import job_treat,treat_data_str

client = MongoClient(mongodb_url)
jobs   = client['linkedin']['experience']
people = client['linkedin']['people']
year_regexp = re.compile('([0-9]+)\sano(s)?')
month_regexp = re.compile('([0-9]+)\s(mês|meses)')


# Return the year and month of dates at the schema ('1 ano 5 meses','2 anos','1 mês') as number
# Broke in two regexp is not efficient but it's easier for error handling
def month_year_text(date_string):
	if isinstance(date_string,str) and any([char.isdigit() for char in date_string]):
		years,month = 0,0
		if year_regexp.search(date_string):
			years = float(date_string.split()[0])
		if month_regexp.search(date_string):
			month = month_regexp.search(date_string)
			month = float(month.group(1))
		return years+month/12
	return None

df_jobs = pd.DataFrame(list(jobs.find({})))
df_jobs = df_jobs.rename(columns={'Duração do emprego':'duration'})

# Transforming dates in something that can be measured
df_jobs['duration'] = df_jobs['duration'].apply(lambda dur: month_year_text(dur))

# Classifying their jobs in job areas defined in general.py
df_jobs['Job Area'] = df_jobs.title.apply(lambda value:treat_data_str(value,job_treat,'Outros'))

# Merging the people information with the jobs info
df_people = pd.DataFrame(list(people.find({'skills':{'$exists':1}},{'name':1})))
df_merged = pd.merge(df_jobs,df_people, left_on='p_id',right_on='_id')

# Getting the list of the employers that work or have worked with data
filter_worked_data = df_merged['Job Area'] == 'Data'
ids_data = list(df_merged[filter_worked_data]['p_id'].unique())
filter_ids_data = df_merged['p_id'].isin(ids_data)


all_jobs = df_merged[filter_ids_data]

# Getting other areas that the data people have worked with it
all_jobs = all_jobs[all_jobs['Job Area'] != 'Data']


df_data = df_merged[filter_worked_data]

# Count the total time that people worked in data
df_data_grouped = df_data.groupby('p_id')['duration'].sum()


# Generating a chart of all the areas
list_areas = list(set( all_jobs['Job Area'].unique()) - set('Data'))
list_areas = [gen_histogram(all_jobs[all_jobs['Job Area'] == area].groupby('name').sum()['duration'],area) for area in list_areas]


#Tempo nas áreas de
