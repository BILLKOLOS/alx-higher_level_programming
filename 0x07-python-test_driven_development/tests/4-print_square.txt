>>> print_square = __import__('4-print_square').print_square


#TypeError

    ### size must be an integer

    >>> print_square(True)
    Traceback (most recent call last):
    TypeError: size must be an integer

    >>> print_square("2795")
    Traceback (most recent call last):
    TypeError: size must be an integer

    >>> print_square(None)
    Traceback (most recent call last):
    TypeError: size must be an integer

    >>> print_square()
    Traceback (most recent call last):
    TypeError: print_square() missing 1 required positional argument: 'size'

    ## size can not be a float

    >>> print_square(27.95)
    Traceback (most recent call last):
    TypeError: size must be an integer

    >>> print_square(-27.95)
    Traceback (most recent call last):
    TypeError: size must be an integer



#ValueError 

    ### size must be positive

    >>> print_square(-2795)
    Traceback (most recent call last):
    ValueError: size must be >= 0

    >>> print_square(-98)
    Traceback (most recent call last):
    ValueError: size must be >= 0



#General Case

    >>> print_square(0)


    >>> print_square(1)
    #

    >>> print_square(2)
    ##
    ##

    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
