[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
from __future__ import print_function, division

%matplotlib inline

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

rand = np.random.random(1000)

pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random variate', ylabel='PMF')

```

![Picture 4.21](https://github.com/mcarrie30/dsp/blob/master/img/4.21.png)


```python
cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random variate', ylabel='CDF')

```

![Picture 4.22](https://github.com/mcarrie30/dsp/blob/master/img/4.22.png)

***

No the distribution is not perfectly uniform.
