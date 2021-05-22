def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    for char in phrase:
        if to_swap.upper() == char:
            new_phrase = new_phrase + char.lower()
        elif to_swap.lower() == char:
            new_phrase = new_phrase + char.upper()
        else:
            new_phrase = new_phrase + char
    return new_phrase