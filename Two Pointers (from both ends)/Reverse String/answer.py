def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    """
    set_of_strings in case of value for a key should have 
    both string to check and valid reversal 
    """
set_of_strings = {
    1:(["h","e","l","l","o"], ["o","l","l","e","h"]),
    2:[["H","a","n","n","a","h"], ["h","a","n","n","a","H"]]
}

for k,(to_reverse, reversed) in set_of_strings.items():
    reverseString(to_reverse)
    if to_reverse == reversed:
        print("String is correctly reversed")
    else:
        print("String is not correctly reversed")

