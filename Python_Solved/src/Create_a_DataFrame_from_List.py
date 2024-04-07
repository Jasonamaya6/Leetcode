"""4/7/24  JasonAmaya


Starting the introduction to pandas form leetcode.


basic start working with data frames I think of it like a spreadsheet only in python."""

# Import both list and pandas to create
from typing import List

import pandas as pd


# We are creating a dataframe from the following list[list[int]] and we are naming the columns
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    ans = pd.DataFrame(student_data, columns=['student_id', 'age'])  # pd.DataFrame(<variable>, columns=[<give name>]
    return ans


print(createDataframe([[1, 2], [2, 15], [3, 4]]))
