[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


```python

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)


#High and Low
a = [6,1]
b = [5,10]

#Convert
def convert(x):
    j = x[0]*12 + x[1]
    j = j * 2.54
    return j
    
print(dist.cdf(convert(a)) - dist.cdf(convert(b)))

```

***

```
0.342746837631
```

***

0.342746837631% of the us population is in this range
