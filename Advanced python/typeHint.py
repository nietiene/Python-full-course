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
    # -> float takes list of int and returns float
    # list[int] means in list every item is int
    return sum(numbers) / len(numbers)

def student_info() -> Dict[str, int]:
   return {"Alice": 90, "Bob": 85}

# optional type
from typing import Optional

def greet(name: Optional[str]) -> str:
   if name:
      return f"Hello {name}"
   return "Hello guest"
# here Optional can be string or none


from typing import Union

def handle_input(x: Union[int, str]) -> str:
   return str(x)

# Can accept int or str
