def green(fn):
    def wrapper():
        return "green "+fn()+" green"
    return wrapper

def red(fn):
    def wrapper():
        return "red "+fn()+" red"
    return wrapper

def blue(fn):
    def wrapper():
        return "blue "+fn()+" blue"
    return wrapper

@blue
@red
@green

def write():
    return 'hello world'

print(write())
