def GPA_by_department(department):
    '''
    the function is to calculate the average GPA of a specific department
    :param department: input department
    :return: average gpa of actual gpa, average gpa of expected gpa
    '''
    actual_gpa = department.courses[:,-1].astype(np.float)
    expected_gpa = department.courses[:,-2].astype(np.float)
    return avg_gpa(actual_gpa),avg_gpa(expected_gpa)