def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lst = [ltr.lower() for ltr in list(phrase) if ltr != ' ']
    lst_copy = lst.copy()
    lst.reverse()
    return lst == lst_copy
    
  

    # normalized = phrase.lower().replace(' ', '')
    # return normalized = normalized[::-1]


