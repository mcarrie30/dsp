[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python

from __future__ import print_function, division

%matplotlib inline

import numpy as np
import pandas as pd
import nsfg
import first

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):

    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d


print(firsts.totalwgt_lb.mean())
print(others.totalwgt_lb.mean())

b_wgt = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
b_plngth = CohenEffectSize(firsts.prglngth, others.prglngth)

print(b_wgt)
print(b_plngth)

```python

### Conclusion

```
Based on Cohen's d to quantify the difference betweent the groups, it seems that the first babies tend to be lighter by very slightly. The weight computation(-.0086) show that the pregnancy weights tend to be more affected to the child number, than the length of the pregnancy(0.028) is to the child number

```
