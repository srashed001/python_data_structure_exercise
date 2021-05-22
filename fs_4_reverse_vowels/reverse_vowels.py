def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    new_string = ""

    vowels = "AaEeIiOoUu"

    vowel_list = [char for char in s if char in vowels]
    print(vowel_list)

    for char in s:
        if char not in vowels:
            new_string += char
        else:
            new_vowel = vowel_list.pop()
            new_string += new_vowel
    
    print(vowel_list)

    return new_string