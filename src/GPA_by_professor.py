import numpy as np;
def GPA_by_professor(department):
    '''
    the function is to calculate the average GPA of all the professors within a department
    :param department: input department
    :return: average GPA of all professors within a department
    '''
    res = []
    for p in department.professors:
        row = []; row.append(p)
        mask = np.where(department.courses[:,2] == p)[0]
        temp = department.courses[mask]
        actual_gpa,expected_gpa = temp[:,-1],temp[:,-2]
        avg1,avg2 = avg_gpa(actual_gpa),avg_gpa(expected_gpa)
        row.append(avg1);row.append(avg2)
        res.append(row)
    res = np.array(res)
    index = np.argsort(res[:,1].astype(np.float))[::-1]
    return res[index]