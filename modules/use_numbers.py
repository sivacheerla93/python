import numbers_module  # or
from numbers_module import *  # or
from numbers_module import iseven  # or
import numbers_module as nm  # using as alias to module

print(numbers_module.iseven(15))
print(iseven(10))
print(nm.iseven(20))
