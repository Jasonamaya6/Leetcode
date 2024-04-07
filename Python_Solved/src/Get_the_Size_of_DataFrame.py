"""4/7/24  JasonAmaya

In this code file we are retrieving the amount of rows and columns and returning it in a list form

"""
from typing import List

import pandas as pd


# Players is a dataframe, so we want to count the rows and columns.
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    column_len = len(players.columns)  # Checks the amount of columns
    row_len = len(players)  # Checks the amount of rows
    print(players.shape)
    return [row_len, column_len]  # This returns the list format in [rows, columns] of the dataframe.

    # Faster way is using the players.shape which returns the row and column in tuple format
    # So return [players.shape[0], players.shape[1]] 


# Testing
ans = pd.DataFrame([[2, 3], [3, 1], [2, 1]],
                   columns=['student_id', 'age'])

print(getDataframeSize(ans))
