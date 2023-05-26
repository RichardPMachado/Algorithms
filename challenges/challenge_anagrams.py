def sort(lst):
    n = len(lst)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst


def is_anagram(first_string, second_string):

    a = ''.join(sort(list(first_string.lower())))
    b = ''.join(sort(list(second_string.lower())))

    if len(first_string) == 0 or len(second_string) == 0:
        return (first_string, second_string, False)

    if a == b:
        return (a, b, True)
    else:
        return (a, b, False)


print(is_anagram("atpas", "pata"))
