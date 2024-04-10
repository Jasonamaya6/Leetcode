""" 4/10/24  JasonAmaya

Checking if the letter is a palindrome.

"""


def isPalindrome(s: str) -> bool:  # This is going to return bool (T or F) if it is a palindrome
    """
    :type s: str
    :rtype: bool
    """
    letter = []  # First I initialized a variable where I will insert numbers and the letters.

    if len(s) == 0:  # Now we set the base where if there is a empty string we just return true.
        return True

    for i in s:  # Now we are going to loop through each individual character in the string inputted.
        if i.isalnum():  # i.isalnum() checks if the individual string is a valid number or alphabet number
            letter.append(i.lower())  # If the condition is true then to append it to the list that we created

    # At this point we should have some sort of list that has something in it

    rev = letter[::-1]  # Here we initialize a variable where we reverse the order of the list we created

    return rev == letter
    # Now in this condition it will output a (T or F) to check if all the letter in the string is a palindrome.


x = "   "

print(isPalindrome(x))
