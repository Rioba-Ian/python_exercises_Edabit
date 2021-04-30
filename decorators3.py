class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        # we can add some code before function call

        self.function(*args, **kwargs)

        # we can also add some code after function call

# adding class decorator to the function
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))

function("geeks_for_geeks", "hello")