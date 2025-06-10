"""
An iterable is something that can be looped over, like a list, tuples, strings, files, dictionaries, and all kinds of different objects.

if something is iterable, it needs to have a special method called __iter__()
"""

nums = [1,2,3]

"""for num in nums:
  print(num)
"""

# print all methods and attributes of nums object, including __iter__()
print(dir(nums))  

"""
A list is an iterable, but not an iterator, so what is an iterator? 

An iterator is an object with a state so that it remembers where it is during iteration. 

Iterators get their next value with a dunder "next" method.

This gives an error: print(next(nums)) as list object is not an iterator.
"""

# create iterator of nums list:
# a more cleaner way of running this: i_nums = nums.__iter__()
i_nums = iter(nums)

# confirms that i_nums is an iterator:
# prints <list_iterator object at 0x00000103E439AB90>:
# print(i_nums) 
""" prints ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__'] - including "next" and "iter" :"""
# print(dir(i_nums))

""" when an iterator runs out of values, it raises a StopIteration exception """

print(next(i_nums)) # prints 1
print(next(i_nums)) # prints 2
print(next(i_nums)) # prints 3

"""
A for loop will not give a Stopiteration exception when running out of values, but a while loop will. Handle it with a Try/Except block:

while True:
  try:
    item = next(i_nums)
    print(item)
  except StopIteration:
    break
"""