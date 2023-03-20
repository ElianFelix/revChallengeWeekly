# python got drunk and bult in functions str() and int() are flipped
# write int_to_str() and str_to_int() functions that will 
# return the corresponding convertions
#
# ex int_to_str(4) -> "4" and str_to_int("29348") -> 29348
# bonus points if you can de_drunk python??

# takes in an integer and returns it's value representation as a string
def int_to_str(i: int) -> str:
    result = ''
    while i > 0:
        current_digit = i % 10
        result = chr(current_digit + 48) + result
        i = i // 10

    return result


# takes in a number string and returns it's numeric value
def str_to_int(s: str) -> int:
    result = 0
    digit = 0
    for e in reversed(s):
        result += (ord(e) - 48) * 10 ** digit
        digit += 1

    return result


print(int_to_str(120))
print(type(int_to_str(124)))

print(str_to_int('29348'))
print(type(str_to_int('29348')))

