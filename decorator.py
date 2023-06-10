# Dekoratory
def uppercase_decorator(function):
    def wrap():
        text = function()
        return text.upper()
    return wrap()

def Hello_World():
    return "Hello World"

decorator = uppercase_decorator(Hello_World)
print(decorator)

