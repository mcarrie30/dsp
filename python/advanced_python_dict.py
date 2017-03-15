
##### CODE FOR DATAFRAME IS IN advanced_python_regex.py #####


#                 ^
#                 |
#                 |
#                 |

###Question 6 ###
df['lastname'] = df['name'].str.rsplit(' ', expand=True, n=1)[1]
question6df = df.filter(['lastname','degree','title', 'email'], axis=1)
dict1 = question6df.set_index('lastname').T.to_dict('list')

###Question 7 ###
df['firstname'] = df['name'].str.split(' ', expand=True, n=1)[0]
question7df = df.filter(['firstname','lastname','degree','title', 'email'], axis=1)
question7dfsorted = question7df.sort('firstname')[0:3]
dict2 = question7dfsorted.set_index(['firstname', 'lastname']).T.to_dict('list')
dict2

###Question 8 ###
question8df = question7df.loc[0:2]
dict3 = question8df.set_index(['lastname', 'firstname']).T.to_dict('list')
dict3estion8df.set_index(['lastname', 'firstname']).T.to_dict('list')
dict3
