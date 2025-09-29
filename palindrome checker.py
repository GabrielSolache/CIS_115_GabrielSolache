#palindrome checker
user_input_palindrome = input("Enter a string (at least 5 characters) to check if it's a palindrome: ")
if len(user_input_palindrome) < 5:
    print("String must ba at least 5 characters long.")
else:
    def isPalindrome(s):
        return s == s[::-1]

    if isPalindrome(user_input_palindrome):
        print(f"the string '{user_input_palindrome}'  is a palindrome.")
    else:
        print(f"the string '{user_input_palindrome}' is not a palindrome.")