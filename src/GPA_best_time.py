import numpy as np;
def GPA_best_time(department):
    '''
    the function is to calculate the best courses within a department base on average GPA
    :param department: input year
    :return: returns the best courses within a department base on average GPA
    '''
    all_courses = np.array((list(set(department.courses[:,0]))))
    res = []
    for p in all_courses:
        row = []; row.append(p)
        mask = np.where(department.courses[:,0] == p)[0]
        temp = department.courses[mask]
        time_span = temp[:,6]
        avg_time = avg_gpa(time_span)
        row.append(avg_time)
        res.append(row)
    res = np.array(res)
    index = np.argsort(res[:,1].astype(np.float))[::-1]
    return res[index]