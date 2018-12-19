from secure_vars import mongodb_url
from pymongo import MongoClient
from general import treat_data_str,job_treat,skill_treat
import pandas as pd
import itertools


client = MongoClient(mongodb_url)
jobs   = client['linkedin']['experience']
people = client['linkedin']['people']



# Transform a list of dicts into a list of the dicts values
def transf_lst_dict(list_skills,dict_treat,alternative=None):
	return [treat_data_str(skill['skill'],dict_treat) for skill in list_skills]


# Remove duplicates from the list
def remove_dupl(list_vals):
	return [list(set(list_val)) for list_val in list_vals]


def group_data(data):
	data.sort()
	data = [value.lower() for value in data]
	counted_positions = ([tuple((key, len(list(group)))) for key, group in itertools.groupby(data)])
	counted_positions.sort(key=lambda x:x[1],reverse=True)
	return counted_positions


df_jobs = pd.DataFrame(list(jobs.find({})))

# Filter to the jobs that are still happening
df_end = (df_jobs['Período'].str.split('–',n=1,expand=True))
df_filter = df_end[1].str.contains('.*momento.*?')
df_filter = df_filter.fillna(False)

# Generate a column classifying the data as Communication,Design...
df_jobs['Job Area'] = df_jobs.title.apply(lambda value:treat_data_str(value,job_treat,'Outros'))

# Filter to the ones that are employed
df_jobs_employed = df_jobs[df_filter]

# Cleaning people that have more than one occupation
df_emp_distinct = df_jobs_employed.drop_duplicates(subset=['p_id'],keep='last')

# Get people skills
df_people = pd.DataFrame(list(people.find({'skills':{'$exists':1}},{'skills':1})))
df_people['skills'] = df_people['skills'].apply(lambda val:transf_lst_dict(val,skill_treat))

# Merge the skills into jobs
df_job_people = pd.merge(df_emp_distinct, df_people, left_on='p_id', right_on='_id')

# Count the number of people per Area on the hackaton
count_area = df_jobs_employed.groupby('Job Area').count()
count_area = (count_area.reset_index()[['Job Area','title']]).rename(columns={'title':'Count'})

# Agglomerating to count the skills by group
counted_skills = df_job_people.groupby('Job Area')['skills'].apply(list)

# Treating the skills lists data
counted_skills = counted_skills.apply(lambda val:remove_dupl(val))
counted_skills = counted_skills.apply(lambda val:list(itertools.chain.from_iterable(val)))

# DataFrame with the skills counted
counted_skills =counted_skills.apply(lambda val :group_data(val))

# skills_count = [[skill[0]]*skill[1] for skill in counted_skills[1]]
# strings_data = ' '.join(list(itertools.chain.from_iterable(skills_count)))

