def isPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def clean_string(s):
    output_string = ''
    for char in s:
        if char.isalnum():
            if char == ' ':
                continue
            elif char.isupper():
                char = char.lower()
                output_string += char
            else:
                output_string += char
    return output_string


set_of_strings = {
    1:'A man, a plan, a canal: Panama',
    2:'race a car',
    3:''
}

for k, v in set_of_strings.items():
    s = clean_string(v)
    if isPalindrome(s):
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')