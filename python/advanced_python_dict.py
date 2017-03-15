
##### CODE FOR DATAFRAME IS IN advanced_python_regex.py #####


#                 ^
#                 |
#                 |
#                 |

###Question 6 ###
df['lastname'] = df['name'].str.rsplit(' ', expand=True, n=1)[1]
question6df = df.filter(['lastname','degree','title', 'email'], axis=1)
dict1 = question6df.set_index('lastname').T.to_dict('list')
print(dict1)

###Question 7 ###
df['firstname'] = df['name'].str.split(' ', expand=True, n=1)[0]
question7df = df.filter(['firstname','lastname','degree','title', 'email'], axis=1)
dict2 = question7df.set_index(['firstname', 'lastname']).T.to_dict('list')
dict2

###Question 8 ###
dict3 = question7df.set_index(['lastname', 'firstname']).T.to_dict('list')
dict3
