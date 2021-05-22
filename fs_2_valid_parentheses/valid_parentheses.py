def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # return bool(parens[0] == "(" and parens[-1] ==")" and parens.count('(') == parens.count(')'))

    count = 0

    counter = []

    for p in parens:
        print(count)
        if p == '(':
            count += 1
            counter.append(count)
        elif p == ')':
            count -= 1
            counter.append(count)
            

        # fast fail: too many right parens
        if count < 0:
            return False
    print(counter)

    return count == 0