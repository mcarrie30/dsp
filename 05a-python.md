# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they are both sequences. Lists and tuples differ in that tuples are immutable. This allows tuples to be more code safe because the data cannot be changed which also allows tuples to be used as dictionary keys. Tuples tend to be much faster than lists because the objects inside are a constant set of values. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they both are a set of values. Sets and lists are different in that sets are an unordered set of items, while lists are ordered. Lists can also have repeats, while sets can't. Furthermore sets are an unordered collection and must be hashable.    
I might use a list if I am collecting student health and weight measurement data because values might repeat and i may care about order; however, if I am attempting to find out how many out of the 50 states the students come from I might use a set because I don't care about the order nor the quantity of students from each individual state.    
Performance differs significantly between finding elements in a set or a list. In a list finding an element is proportional to how long the list is because the algorithm searches one by one; however, in a set, a hash table lookup finds the element.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is a method of creating an anonymous function. An anonymous function might be used for memory management. A specific reason a lambda might be used is when manipulating and filtering dataframes, many functions may be used. Too many variables and functions may adversely create memory leakage. An example of lamda in the argument sorted:    

```
shopping_list = [('Gatorade', 'Green Juice', 'Granola Bars'), ('Color Pencils', 'Clam Chowder', 'Chairs'), ('Tylenol', 'Time Watch', 'Teddy Bear')] 

sorted(shopping_list, key=lambda x: x[2][1])
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allows python programmers to create complex and elegant lists using mathematical notations. Map and filters are methods applied to lists that can manipulate functions to create desired result.   
For example:


**List Comprehension**
listcomp = [2**i for i in range(10)]

**Map**
n = range(0,10)
listmap = list(map(lambda i: 2**i, n))

**Filter**
def f():
	return([2**i for i in range(10)])

list(filter(f(), range(0,513)))

**Set Comprehension**
f = {x for x in range(0,10)}

**Dictionary Comprehension**
mydictionary = dict([(i, 'oclock') for i in range(1,10)])


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





