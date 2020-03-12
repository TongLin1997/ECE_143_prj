# sort the professor base on time
def TIME_by_professor(department):
    '''
    the function is to sort the professor base on time
    :param department: input department
    :return: time spent of all professors within a department
    '''
    res = []
    for p in department.professors:
        row = []; row.append(p)
        mask = np.where(department.courses[:,2] == p)[0]
        temp = department.courses[mask]
        allTime = temp[:,6]
        avg_time = avg_gpa(allTime)
        row.append(avg_time)
        res.append(row)
    res = np.array(res)
    index = np.argsort(res[:,1].astype(np.float))[::-1]
    return res[index]
