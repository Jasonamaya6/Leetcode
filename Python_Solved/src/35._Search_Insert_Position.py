"""4/18/21  Jason Amaya

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the
index where it would be if it were inserted in order.


"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):  # First we want to loop through the list to check all individual numbers in the list.
        if nums[i] == target:  # If the number in the list is equal to the list then we return its index
            return i
        if nums[i] > target:  # If the number is greater than we return the previous i.dex before it goes over the
            # target value.
            return i

    return len(nums)  # If there are no targeted values in the list then it would be the next value out of the list
    # so we just return the length of the list.


x = [1, 3, 5, 6]
y = 2

print(searchInsert(x, y))
