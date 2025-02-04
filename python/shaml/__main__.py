# shaml/python/shaml/__main__.py
from .core import sl, ShamelessError

# Examples of how to use it
print(sl("123"))
print(sl("123.45"))
print(sl("[1, 2, '3']"))
print(sl("{ 'name':'Alice', 'age':'30' }"))
print(sl("True"))
print(sl("False"))
print(sl(123))
print(sl(123.45))
print(sl(True))
print(sl(False))
print(sl([1, 2, "3"]))
print(sl({"name": "Alice", "age": "30"}))
print(sl(None))
print(sl("hello"))
error_test = sl("error", debug=True)
if error_test:
    print("this should not print")
else:
    print(error_test, error_test.message, error_test.original_value)