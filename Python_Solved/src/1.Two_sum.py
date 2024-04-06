""" 4/6/24  JasonAmaya


In this code we want to find two indexes from the list (nums) that equal to the desired sum which is our (target)'

EXAMPLE:
    nums: [1,5,3] target: 8 -----> [1,2]
    nums: [1,4,10] target: 20 -----> []
    nums: [9,2,90,2,1,4] target: 11 -----> [0,1]

First what we do is set up our function called twoSum and by good habits we define the parameters : by value

"""


def twoSum(nums: list[int], target: int):
    result = []  # We create a variable with an empty list that we will eventually use.

    for i in range(len(nums)):  # Now we create a loop for the first instance where it will regularly go through
        for j in range(i + 1, len(nums)):  # Now we use j to trail against i, so it will be looping ahead of i this is
            # how we check the lists
            if nums[i] + nums[
                j] == target:  # Now we check the actual value within the list to see if the two numbers = the target.
                result.append(i)  # If the statement is true then we append the i
                result.append(j)  # And also append the j

    return result  # If the statment was true then the result list will come with number else it will return am empty list.


print(twoSum([1, 23, 4], 24))
