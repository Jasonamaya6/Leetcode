"""4/8/24  JasonAmaya


Data selecting where I create two functions :

1) For the first one I want to retrieve all student_id that == a specific id and output the following
columns specified

2) Next, making a function that adds a new column with a specific values in them.

"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Many ways to retrieve the data however I provided two that are simple.
    return students.loc[students["student_id"] == 2, ['age']]  # 1
    # return students.query("student_id == 101") [['name','age']] # 2


ans = pd.DataFrame([[2, 3], [3, 1], [2, 1]],
                   columns=['student_id', 'age'])

print(selectData(ans))  # Outputs --> 3, 1


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Go into the employees data frame and add bonus and set the column = to double the salary.
    employees['bonus'] = 2 * employees.salary
    return employees
