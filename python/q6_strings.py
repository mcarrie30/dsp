# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    ""
    raise NotImplementedError


def both_ends(s):
    if len(s) <= 1:
        return ''
    else:
        word = s[:2] + s[-2:]
        return word

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    ""
    raise NotImplementedError


def fix_star(s):
    firsthalf = s[0]
    twohalf = str.replace(s[1:], s[0], '*')
    return(firsthalf + twohalf)

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'

    raise NotImplementedError


def mix_up(a,b):
    first = a[0:2]
    second = b[0:2]
    a = a.replace(first, second)
    b = b.replace(second, first)
    mixup = a + " " + b
    return mixup

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'

    raise NotImplementedError



def verbing(s):
    while len(s) >= 3:
        if s[-3:] == 'ing':
            return(s + 'ly')
        if len(s) >= 3:
            return(s + 'ing')
    while len(s) < 3:
        return(s)

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'

    raise NotImplementedError


def not_bad(s):
    x = s.find('not')
    y = s.find('bad')
    if x < y:
        return(s[:x] + 'good')
    else:
        return(s)

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"

    raise NotImplementedError


def front_back(a, b):
    if len(a) % 2 == 0:
        aword = len(a) // 2
        onehalfa = a[:aword]
        twohalfa = a[aword:]
    elif len(a) % 2 != 0:
        aword = len(a) // 2 + 1
        onehalfa = a[:aword]
        twohalfa = a[aword:]
        
    if len(b) % 2 == 0:
        bword = len(b) // 2
        onehalfb = b[:bword]
        twohalfb = b[bword:]
    elif len(b) % 2 != 0:
        bword = len(b) // 2 + 1
        onehalfb = b[:bword]
        twohalfb = b[bword:]
        
    return(onehalfa + onehalfb + twohalfa + twohalfb)



    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'

    raise NotImplementedError
