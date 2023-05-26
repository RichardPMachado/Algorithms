def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    a = ''.join(sorted(first_string.lower()))
    b = ''.join(sorted(second_string.lower()))
    if (len(a) or len(a)) == 0:
        return (a, b, False)

    if a == b:
        return (a, b, True)
    else:
        return (a, b, False)

# print(is_anagram("pata", ""))
