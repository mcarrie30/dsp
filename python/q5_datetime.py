# Hint:  use Google to find python function

####a) 

from datetime import datetime
start = datetime.strptime('01-02-2013', '%m-%d-%Y')
end = datetime.strptime('07-28-2015', '%m-%d-%Y')
print(end-start)

####b)  
start2 = datetime.strptime('12312013', '%m%d%Y')
end2 = datetime.strptime('05282015', '%m%d%Y')
print(end2-start2)

####c)
start3 = datetime.strptime('15-Jan-1994', '%d-%b-%Y')
end3 = datetime.strptime('14-Jul-2015', '%d-%b-%Y' )
print(end3-start3) 