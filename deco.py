"""
Decorators in Python:

- flask @app.route
- @pytest.fixture
- @property, @staticmethod (classes)
- @lru_cache

# decorators are a tool to avoid classes and subclasses
"""
from my_decos import log, timestamp
import time
from functools import lru_cache


# define functions using the decorator later
@timestamp
@log
@lru_cache(maxsize=100)  # <--- stores a,b and the results of add(a, b)
def add(a, b):
    time.sleep(5)
    return a + b

@log
def mul(a, b):
    return a * b


add(3, 4)

add(4, 4)



mul(3, 4)
