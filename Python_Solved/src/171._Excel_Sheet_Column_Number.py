""" May 4 2024  Jason Amaya 

Given a string columnTitle that represents the column 
title as appears in an Excel sheet, return its corresponding column numbe

"""


class Solution(object):
    def titleToNumber(self, columnTitle : str) -> int:
        """
        :type columnTitle: str
        :rtype: int
        """
        # Create a list containing the uppercase alphabet
        alpha = list(string.ascii_uppercase)
        
        # Initialize the column number to 0
        columnNumber = 0
        
        # Iterate through each character in the column title
        for i in columnTitle:
            # Convert the character to its corresponding number
            num = alpha.index(i) + 1
            # Update the column number by multiplying it by 26 and adding the contribution of the current character
            columnNumber = columnNumber * 26 + num
        
        # Return the final column number
        return columnNumber
