# program showing use of decorators in python
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):

        # we add some code
        # defore function call

        self.function()

        #  we can also add some code 
        #  after function call.

# adding class decorator to the function
@MyDecorator
def function():
    print('Geeks for Geeks')

# function()

