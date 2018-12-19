from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def transf_tup_count(list_tuples):
	dict_skills = {}
	for tuple in list_tuples:
		if len(tuple[0])>3:
			key = str.capitalize(tuple[0])
		else:
			key = str.upper(tuple[0])
		dict_skills[key] = tuple[1]
	return dict_skills

dict_skills  = transf_tup_count(data)


def transform_format(val):
	if val == 0:
		return 255
	else:
		return val

db_mask = np.array(Image.open("./db_@.png"))
# for i in range(len(db_mask)):
# 	transformed_db_mask[i] = list(map(transform_format, db_mask[i]))
#

wordcloud = WordCloud(width=1600,height=1000 ,max_words=50,background_color="white",mask=db_mask).generate_from_frequencies(frequencies=dict_skills)
wordcloud.to_file("./db_c.png")

