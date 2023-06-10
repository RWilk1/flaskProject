from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

# Dekoratory w Python-ie -
def plus_one(number):
    return number + 1

print(plus_one(1))

my_function = plus_one
print(my_function(5))

def plus_one(number):
    return number + 1


def call_function(function):
    number = 5
    return function(number)


print(call_function(plus_one))



