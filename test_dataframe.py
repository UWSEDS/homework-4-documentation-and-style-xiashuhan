"""
The module should check the following properties of the given DataFrame:
    1.If the DataFrame contains only the columns that you specified as the second argument.
    2.If the values in each column have the same python type.
    3.If there are at least 10 rows in the DataFrame.
The module should also:
    a.Check that all columns have values of the corect type.
    b.Check for nan values.
    c.Verify that the dataframe has at least one row.
"""

def test_create_dataframe(dataframe, col_list):
    '''
    :param dataframe: DataFrame whose properties are being checked.
    :param col_list: The list of column names that the given DataFrame should have.
    :return: True if conditions 1, 2, 3 hold; False otherwise.
    '''

    # Verify that the dataframe has at least one row.
    if dataframe.shape[0] == 0:
        raise ValueError("Empty dataframe")
    # Check for nan values.
    if dataframe.isna().any().any():
        raise ValueError("NaN values in the dataframe")
    # Check that all columns have values of the corect type.
    for i in range(dataframe.shape[1]):
        for j in range(dataframe.shape[0]):
            if type(dataframe.iloc[j, i]) != type(dataframe.iloc[0, i]):
                raise ValueError("Wrong value types")
    # Return True if conditions 1, 2, 3 hold, return False otherwise.
    if list(dataframe.columns) == col_list and dataframe.shape[0] >= 10:
        return True
    return False
