"""4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?"""

"""after adding 20.0 we think set will be {20, 20.0} but Python checks 20==20.0, 
it gives True both are same so set doesnt have duplicate values, so length is still 1 --> 20
next adds "20", 20 is not int it is str so length of the set is 2--> {20, "20}"""

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

"""What is the type of s if s = {}?
s is a Dictionary (dict), not an integer--> In python {} Creates an empty dictionary, not an empty set.
To create empty set we use--> s = set() and for dictionary s={}
"""