def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    # count = 0

    # def unicode_conversion(letter):
    #     return ord(letter.upper()) - 64
    
    # for ltr in word:
    #     count += unicode_conversion(ltr)
    
    # print(count)
    
    # return bool(count % 2 != 0)
    
    DIFF = ord("a") - 1
    print(DIFF)

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1