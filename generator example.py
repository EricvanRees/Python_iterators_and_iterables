"""
Generators can be used to create easy-to-read iterators. Instead of returning a value like a normal function they yield a value. Generators are interators as well but the "next" and "iter" dunder methods are created automatically. The generator below does the exact same thing as the class that mimicks the range() builtin method with an iterator (but with less code).
"""

def my_range(start, end):
  current = start
  while current < end:
    yield current
    current += 1
    
nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))