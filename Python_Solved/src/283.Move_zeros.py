"""4/10/24  JasonAmaya

Retrieving all the 0 and moving them into the back of the list

"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zeroes = nums.count(0)  # First we initialize the (zeroes)  in order to use it for the future
    for i in nums[:]:  # The nums[:] is the important part [:] the colin tells the computer to duplicate the list
        #and keeps the copy of the orignal list.
        if i == 0:  # After we check the condition checking which i = 0.
            nums.remove(i)  # If we have detected one we remove it using remove().

    nums.extend([0] * zeroes)  # Now here is where the zeros variable comes in hand, after removing the zeros
    # we need to replace them and put them back in the back we do so by using the extent function which
    # we specify the number 0 * by the amount of 0 we removed.


x = [2, 0, 0, 2, 3, 0, 0, 3]

moveZeroes(x)

print(x)
