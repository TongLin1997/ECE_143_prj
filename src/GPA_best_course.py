import numpy as np;
def GPA_best_course(department):
    '''
    the function is to calculate the best courses within a department base on average GPA
    :param department: input department
    :return: returns best courses within a department base on average GPA
    '''
    all_courses = np.array((list(set(department.courses[:,0]))))
    res = []
    for p in all_courses:
        row = []; row.append(p)
        mask = np.where(department.courses[:,0] == p)[0]
        temp = department.courses[mask]
        actual_gpa,expected_gpa = temp[:,-1],temp[:,-2]
        avg1,avg2 = avg_gpa(actual_gpa),avg_gpa(expected_gpa)
        row.append(avg1); row.append(avg2)
        res.append(row)
    res = np.array(res)
    index = np.argsort(res[:,1].astype(np.float))[::-1]
    return res[index]