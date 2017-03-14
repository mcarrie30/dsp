import numpy as np
import pandas as pd
import re

### Question 1 ###

df = pd.read_csv('faculty.csv')

df.rename(columns={' title':'title', ' degree':'degree',' email': 'email'}, inplace=True)
df["degree"] = df["degree"].map(str.strip)

# Show different unique degrees
list(df['degree'].unique())

df = df.replace('Ph.D', 'Ph.D')
df = df.replace('Sc.D.', 'Sc.D')
df = df.replace('Ph.D.', 'Ph.D')
df = df.replace(['Ph.D.'], ['Ph.D'], regex = True)
df = df.replace(['PhD'], ['Ph.D'], regex = True)
df = df.replace(['ScD'], ['Sc.D'], regex = True)

list1 = list(df['degree'])

list2 = []
def listing(x):
    for i in x:
        if len(i) > 5:
            list2.append(i)
    return(list2)

listing(list1)

def un_list(x):
    newlist = []
    for i in x:
        newlist += i.split(' ')
    return(newlist)

list3 = un_list(list2)
final_list = list1 + list3

final_list = list(filter(lambda x: len(x) < 5, final_list))
final_list = list(filter(lambda x: x != '0', final_list))

degree_df = pd.DataFrame(final_list)
degree_df.groupby(0).size()


#JD       1
#M.S.     1
#MA       1
#MD       1
#MPH      2
#MS       1
#Ph.D    31
#Sc.D     6
#dtype: int64



### Question 2 ###
list(df['title'].unique())
df = df.replace([' is '], [' of '], regex = True)
df.groupby('title').size()

#title
#Assistant Professor of Biostatistics    12
#Associate Professor of Biostatistics    12
#Professor of Biostatistics              13
#dtype: int64



### Question 3 ####
email_list = list(df['email'])
print(email_list)



### Question 4 ###
df['domain'] = df.email.str.extract('(@.+)', expand=True)
df.groupby('domain').size()

#domain
#@cceb.med.upenn.edu     1
#@email.chop.edu         1
#@mail.med.upenn.edu    23
#@upenn.edu             12
#dtype: int64
