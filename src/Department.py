import numpy as np
import re



class Department():
    '''
    Data structure that manages course names, descriptions, and CAPE data
    Input:  name: department name as str.
    '''
    def __init__(self, name):
        self.name = name
        self.courses, self.descriptions = None, None

    def stringPercentToFloat(self, percent):
        return round(float(percent[:-1]) / 100, 3)

    def loadCourses(self, file):
        '''
        Function that loads CAPE data into the class. This data will be separated by course name.
        Input file: path to CAPE data text file.
        '''
        s = np.loadtxt(file, dtype='str', delimiter="\t")
        res = []
        for i in range(s.shape[0]):
            row = []
            course = s[i][1].split('-')
            row.append(course[0].strip());
            row.append(course[1].strip())
            row.append(s[i][0]);
            row.append(s[i][2])
            row.append(self.stringPercentToFloat(s[i][5]))
            row.append(self.stringPercentToFloat(s[i][6]))
            row.append(float(s[i][7]))
            if (s[i][-2] != 'N/A'):
                row.append(float(re.findall(r'[^()]+', s[i][-2])[1]))
            else:
                row.append(0.0)
            if (s[i][-1] != 'N/A'):
                row.append(float(re.findall(r'[^()]+', s[i][-1])[1]))
            else:
                row.append(0.0)
            res.append(row)
        self.courses = np.array(res)

    def loadDescription(self, filename):
        '''
        Function that loads course descriptions into the class. This data will be separated by course name.
        Input file: path to course description text file.
        '''
        D, res = [], []
        with open(filename, 'r', errors='ignore') as file:
            for line in file:
                if line != '\n': D.append(line)
        for i in range(len(D) // 2):
            row = []
            course = D[2 * i].split('.')
            row.append(course[0].strip());
            row.append(course[1].strip())
            row.append(D[2 * i + 1].strip())
            res.append(row)
        self.descriptions = np.array(res)

    def cleanData(self):
        '''
        script that cleans some of the CAPE data based on empty entries.
        '''
        s = np.array(list(set(self.descriptions[:, 0])))
        mask = np.isin(self.courses[:, 0], s)
        self.courses = self.courses[np.where(mask)]