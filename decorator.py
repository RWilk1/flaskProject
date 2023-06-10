# Dekoratory
def uppercase_decorator(function):
    def wrap():
        text = function()
        print(text.upper())
        return text.upper()
    return wrap()

# def Hello_World():
#     return "Hello World"
#
# decorator = uppercase_decorator(Hello_World)
# print(decorator)

@uppercase_decorator
def Hello_World():
    return "Hello World"

# @decorator - czyli to nazwa do której została przypisana jakaś funkcja
# i dekorator może mieć dodatkowe właściwości