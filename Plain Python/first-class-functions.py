def square(x):
    return x*x

f = square

print(square)
print(f(square(5)))

# If a function accepts other function as argument or return a function as output, 
# It becomes a HIGHER-LEVEL FUNCTION
# ------------------------------------------------------------------------------------

def cube(x):
    return x*x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1,2,3,4,5])
print(squares)

# ------------------------------------------------------------------------------------

def logger(msg):
    def log_message():
        print("Log : ", msg)
    return log_message
      
log_hi = logger("Hi!")
log_hi()

print(logger)
print(log_hi)

# ------------------------------------------------------------------------------------

def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}")
    return wrap_text

# bir değere atanabildiği için ve farklı bir fonksyiondan returnu edilebildiği için
# wrar_text fonksiyonu first-class-function'dır. 

print_h1 = html_tag('h1')

print_h1('Test headline!')
print_h1('Another headline!')

print_p = html_tag('p') # tag için atama yapılıyor
print_p("Test paragraph!") # kullanım için ise return wrap_text fonksyionu oldugu icin,
# bu fonksyionun argümanı input olarak veriliyor ve cık tı elde ediliyor.
