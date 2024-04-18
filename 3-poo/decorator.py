def my_decorator(func):
  def wrapper():
    print("antes da funçaõ")
    func()
    print("depois da função")
  
  return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@my_decorator
def hello():
  print("Hello henry")

@split_string
@uppercase_decorator
def uppercase_name():
  return "henry"


hello()

print(uppercase_name())