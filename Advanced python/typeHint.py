# allows you to specifiy the excepted data types 
# allows you to specifiy datatype for function parameters, function return values, variable

def greet(name: str) -> str:
    return "Hello" + name

age: int = 20
price: float = 9.99
is_valid: bool = True

# multiple parameter
def add(x: int, y: int) -> int:
  return x * y


# also you can use typing module
from typing import List, Tuple, Dict

def average(numbers: List[int]) -> float:
   return sum(numbers) / len(numbers)

def student_info() -> Dict[staticmethod, int]