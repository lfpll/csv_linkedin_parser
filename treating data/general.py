import re

# Convert the string matched with dict regexp value for the dict key
def treat_data_str(job_str,dict_treat,alternative = None,sort_list = False):
	list_to_iterate = dict_treat.items()

	#Method added do prioritize higher rank search
	if sort_list:
		list_to_iterate = [tuple((int(key),value)) for key,value in list_to_iterate]
		list_to_iterate.sort(key=lambda val:val[0],reverse=True)

	for key,regexp in list_to_iterate:
		if regexp.search(job_str.lower()):
			return key
	if alternative == None:
		return job_str
	else:
		return alternative

job_treat = {'Educação': re.compile('pesquisa|academ|estudante|bolsista|pesquisador|profess|corpo docente|educac'),
	 'Design': re.compile("designer|ux/ui|inovação|(^|\W)ux($|\W)|(^|\W)ui($|\W)"),
	 'Comunicação\Marketing': re.compile(
		 "comunicação|redator|marketing|mídias sociais|digital|social media|canais digitais"),
	 'Data': re.compile('(^|\W)Modeling($|\W)|(^|\W)data($|\W)|(^|\W)dados($|\W)|analytics|language processing analyst|artificial intelligence specialist|business intelligence|(^|\W)bi($|\W)'),
	 'IT': re.compile('oracle|programador|software|algoritmos|informática|(^|\W)PHP($|\W)|(^|\W)sql($|\W)|(^|\W)ti($|\W)|(^|\W)dba($|\W)|developer|desenvolvedor|analista de sistemas|desenvolviment.*software|qlikview|tecnologia da informação|technology consultant|desenvolvimento')}

skill_treat = {'python':re.compile('python'),'sql':re.compile('sql'),'etl':re.compile('(^|\W)etl'),'user experience':re.compile('user experience'),'Front-end':re.compile('front-end'),'CSS':re.compile('Cascading Style Sheets \(CSS\)|^CSS$|^CSS3$')}


bach_str = '(^|\W)design(\W+|$)|(^|\W)enginee\w+|bacha\w+|grado|bache\w+(\W+|$)|licenciatura|graduação|ciência(s?) da computação|desenho industrial|análise e desenvolvimento de sistemas|superior|(^|\W)engenhei\w+|engenharia(\W+|$)'
mast_str = '(^|\W)mestre|mestrad\w+|master|bsc(\W+|$)'
doc_str  = '(^|\W)doutorado(\W+|$)'
tecn_str = '(^|\W)técnic\w+(\W+|$)|(^|\W)tecnologia(\W+|$)|(^|\W)t\wcn\wlogo(\W+|$)'
post_str = '(^|\W)academia de inte.*|(post(-|\s+)grad\w+|especialização|pós-gradução|pós(-|\s+)graduação|mba|especialista)(\W+|$)'
others_str = 'ensino médio|ensino fundamental'
edu_treat = {5: re.compile(doc_str), # doutorado
			4: re.compile(mast_str), # mestrado
			3: re.compile(post_str), # graduação
	        2: re.compile(bach_str), # técnico
            1: re.compile(tecn_str), # técnologo
             0:re.compile(others_str)} # nenhum dos anteriores achados


month_num = {'abr':4,
 'ago':8,
 'dez':12,
 'fev':2,
 'jan':1,
 'jul':7,
 'jun':6,
 'mai':5,
 'mar':3,
 'nov':11,
 'out':10,
 'set':9}
