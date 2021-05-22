def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst = list(phrase)
    lst.reverse()

    return "".join(lst)

    # return phrase[::-1]
    # will loop through and reassign phrase backwards

