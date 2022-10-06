def swap_vowels():
    string = input('Enter a string: ')
    start = 0
    end = len(string)-1

    string: list(str) = list(string)
    
    while start < end:

        start_char, end_char = string[start], string[end]

        if (start_char in ('a','e','i','o','u')) and (end_char in ('a','e','i','o','u')):
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

        elif (start_char in ('a','e','i','o','u')) and (end_char not in ('a','e','i','o','u')):
            end -= 1

        elif (start_char not in ('a','e','i','o','u')) and (end_char in ('a','e','i','o','u')):
            start += 1

        else:
            start += 1
            end -= 1

    print(''.join(string))


if __name__ == '__main__':
    swap_vowels()



