[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python

%matplotlib inline
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label) 
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)  
    new_pmf.Normalize()
    return new_pmf

bias = BiasPmf(pmf, label='bias')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, bias])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

```


![Picture 3.1](https://github.com/mcarrie30/dsp/blob/master/img/3.1_Img.png)

```python
print('Pmf:', pmf.Mean())
print('Bias:', bias.Mean())
```

***

Pmf: 1.02420515504
Bias: 2.40367910066