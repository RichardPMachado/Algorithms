def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if (len(first_string) or len(second_string)) == 0:
        return False
    a = ''.join(sorted(first_string.lower()))
    b = ''.join(sorted(second_string.lower()))

    if a == b:
        return True
    else:
        False
