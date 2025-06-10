"""
You can add "next" and "iter" methods to your classes and make them iterable as well.

The following code shows an example of that, and behaves like the built-in range() function.
"""

class MyRange:
  
  def __init__(self, start, end):
    self.value = start
    self.end = end
    
  def __iter__(self):
    return self

  def __next__(self):
    if self.value >= self.end:
      raise StopIteration
    current = self.value
    self.value += 1
    return current
  
nums = MyRange(1, 10)

print(next(nums))

