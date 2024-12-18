from palin import is_palindrome

def longest_palindrome(s,num_char):

    longest = ""

    for i in range(num_char):
        for j in range(i + 1, num_char + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring

    return longest

s=input("Enter a string:")
num_char=len(s)
print("longest palindrome substring is:",longest_palindrome(s,num_char))
