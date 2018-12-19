from secure_vars import mongodb_url
from pymongo import MongoClient
import pandas as pd
from general import treat_data_str,edu_treat
import plotly.graph_objs as go


client = MongoClient(mongodb_url)
education = client['linkedin']['education']
people = client['linkedin']['people']

# Check if the education is curently happening
def split_date(date_str,split_str='–',only_num=False):
	date_list = date_str.split(split_str)
	if only_num:
		list(map(int,date_list))
	return date_list


# Dict of education
df_edu = pd.DataFrame(list(education.find()))

# Classify the level of education of each people
df_edu = df_edu.dropna(subset=['Diploma'])

df_edu['class_edu'] = df_edu.Diploma.apply(lambda dip: treat_data_str(dip,edu_treat,alternative=0,sort_list=True))
df_class_edu = df_edu[['p_id','class_edu','Diploma']].dropna()


# Get the max level of education for each people
df_max_edu = df_edu.groupby(['p_id'])['class_edu'].max()
df_max_edu = df_max_edu.reset_index()

# Get the current state of the graduation\formation
per_drop = ~df_edu['Período'].isna() & df_edu.Período.dropna().str.contains('–')
df_edu = df_edu[per_drop]

# Split dates
dates = df_edu.Período.str.split('–',n=1,expand=True)
df_edu['end'] = dates[1]
df_edu.end = df_edu['end'].astype(int)
df_edu.drop(columns=['Período'],inplace=True)

# Check to see if the ending date is bigger then current date
# 1 - For Active
# 0 - It Already ended
df_edu.loc[df_edu['end'] > 2018,'state'] = 1
df_edu.loc[df_edu['end'] <= 2018,'state'] = 0

# Merging the together to get the people that are still studying
df_max_edu['cat'] = 1
df_joined = df_edu.join(df_max_edu.set_index(['p_id','class_edu']),on=['p_id','class_edu'])
df_studys_max = df_joined.dropna(subset=['cat'])

# Joining to the people list to evaluate if the data is right by their names
df_people = pd.DataFrame(list(people.find({'skills':{'$exists':1}},{'name':1})))
merged = df_people.merge(df_studys_max,left_on='_id',right_on='p_id')
merged.drop_duplicates(subset=['p_id','class_edu'],inplace=True)

# Separating the data that I wan't to plot
merged_tread = merged[merged['class_edu'] ==0][['class_edu','state','name','p_id']]
graduated = merged[merged['state']==0].groupby(['class_edu']).count()
still_stud = merged[merged['state']==1].groupby(['class_edu']).count()
graduated = graduated[['cat']]
still_stud = still_stud[['cat']]


trace1 = go.Bar(
    x=['Outros','Técnico','Graduação','Pós-Graduação','Mestrado','Doutorado'],
    y=list(still_stud['cat']),
    name='Cursando'
)
trace2 = go.Bar(
    x=['Outros','Técnico','Graduação','Pós-Graduação','Mestrado','Doutorado'],
    y=list(graduated['cat']),
    name='Finalizado'
)

import plotly
trace1 = go.Bar(
    x=['Outros','Tecnologia','Graduação','Pós-Graduação','Mestrado','Doutorado'],
    y=list(still_stud['cat']),
    name='Cursando'
)
trace2 = go.Bar(
    x=['Outros','Tecnologia','Graduação','Pós-Graduação','Mestrado','Doutorado'],
    y=list(graduated['cat']),
    name='Finalizado'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group',
	bargap=0.30,
	bargroupgap=0.3,
	title='Formação dos Participantes',
	titlefont=dict(
			family='Roboto',
            size=30,
        ),
	yaxis=dict(
titlefont=dict(
			family='Roboto',
            size=18,
        ),
		title = 'Número de pessoas',
        tickfont=dict(
			family='Roboto',
            size=18,
        )
    ),
	xaxis=dict(
	        tickfont=dict(
			family='Roboto',
	            size=18,
	        )
	    ),
	legend=dict(
	        x=0.1,
	        y=0.5,
		font=dict(
			family='Roboto',
			size=22,
		),
	    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig,filename='bar_chart_studies')