>>> say_my_name = __import__('3-say_my_name').say_my_name


#TypeError

    ### first_name and last_name must be strings

    >>> say_my_name(True)
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name("Max", 2795)
    Traceback (most recent call last):
    TypeError: last_name must be a string

    >>> say_my_name(None)
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name()
    Traceback (most recent call last):
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'



#General Case

    >>> say_my_name("Max")
    My name is Max 

    >>> say_my_name("Holberton", "School")
    My name is Holberton School
