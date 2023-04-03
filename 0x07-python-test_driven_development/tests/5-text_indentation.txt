>>> text_ind = __import__('5-text_indentation').text_indentation


#TypeError

    ### text must be a string

    >>> text_ind()
    Traceback (most recent call last):
    TypeError:

    >>> text_ind(None)
    Traceback (most recent call last):
    TypeError: text must be a string

    >>> text_ind(True)
    Traceback (most recent call last):
    TypeError: text must be a string

    >>> text_ind('0')
    Traceback (most recent call last):
    TypeError: text must be a string

    >>> text_ind(1024)
    Traceback (most recent call last):
    TypeError: text must be a string



#General Case

    >>> text_ind(".")
    <BLANKLINE>

    >>> text_ind("?")
    <BLANKLINE>

    >>> text_ind(":")
    <BLANKLINE>

    >>> text_ind(":a:")
    <BLANKLINE>
    a
    <BLANKLINE>

    >>> text_ind(".Holberton:School?")
    <BLANKLINE>
    Holberton
    <BLANKLINE>
    School
    <BLANKLINE>
