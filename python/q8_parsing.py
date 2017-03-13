# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np
import pandas as pd


def readfile(x):
    df = pd.read_csv(x)
    df['difference'] = (abs(df['Goals'] - df['Goals Allowed']))
    return df.loc[df['difference'].idxmin()][0]

readfile('football.csv')

# Answer is Aston Villa with a difference of 1
