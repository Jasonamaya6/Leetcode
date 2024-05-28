""" May 28, 2024,  Jason Amaya

Return True if the the list of integers contain any duplicates.
"""


# Within this function it loops through each int and checks all through the list to see if numbers match (Brute 
# Forcing).
def containsDuplicate(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i in range(len(nums)):  # Loops through the first iteration 
        for j in range(i, len(nums)):  # Now loops through the second start from the i.
            if nums[i] == nums[j]:  # Checking if numbers match
                return True  # If they do then return True
    return False  # Else Return false


# Within this function it simply uses the set() function which makes the list variables independent so no repeating.
def containdup(nums): 
    setter = set(nums)  # Created a variable where it sets.
    return len(setter) != len(nums)  # Checking if the lengths of them match if they don't it returns True.


print(containdup([1, 2, 3, 1]))
