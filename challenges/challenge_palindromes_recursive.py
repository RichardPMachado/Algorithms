def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    first_caractere = word[low_index]
    last_caractere = word[high_index]
    if len(word) == 0 or first_caractere != last_caractere:
        return False
    if low_index > high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
