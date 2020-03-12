class Department():
    #initialize the class
    def __init__(self, name):
    '''
    this function is to initialize the class
    :param name: input the name of department
    :return:  
    '''
        self.name = name
        self.courses,self.descriptions = None,None
        self.preq,self.professors = {},None
        self.evals = None
        self.gpa_median,self.time_median = None,None
    
    # convert 93.6% to 0.936
    def stringPercentToFloat(self,percent):
    '''
    this function is to convert percent to float
    :param percent: input a string contain "%" like 93.6%
    :return: float 
    '''

        ‘’‘
        ’‘’
        return round(float(percent[:-1]) / 100,3)
    
    # load all the CAPE data into self.courses
    def loadCourses(self,file):
    '''
    this function is to load all the CAPE data into self.courses
    :param percent: input file name
    :return: 
    '''
        s = np.loadtxt(file,dtype = 'str',delimiter = "\t")
        res,evals = [],[]
        for i in range(s.shape[0]):
            row,row2 = [],[]
            course = s[i][1].split('-')
            row.append(course[0].strip()); row.append(course[1].strip())
            row.append(s[i][0]); row.append(s[i][2])
            row.append(self.stringPercentToFloat(s[i][5]))
            row.append(self.stringPercentToFloat(s[i][6]))
            row.append(float(s[i][7]))
            if (s[i][-2] != 'N/A'): row.append(float(re.findall(r'[^()]+', s[i][-2])[1]))
            else: row.append(0.0)
            if (s[i][-1] != 'N/A'): row.append(float(re.findall(r'[^()]+', s[i][-1])[1]))
            else: row.append(0.0)
            res.append(row)
            row2.append(s[i][3]); row2.append(s[i][4])
            evals.append(row2)
        self.courses = np.array(res)
        self.evals = np.array(evals)
    
    # load all the descriptions into self.description
    def loadDescription(self,filename):
    '''
    this function is to load all the descriptions into self.description
    :param percent: input file name
    :return: 
    '''
        D,res = [],[]
        with open(filename,'r',errors='ignore') as file:
            for line in file:
                if line != '\n': D.append(line)
        for i in range(len(D) // 2):
            row = []
            course = D[2*i].split('.')
            row.append(course[0].strip()); row.append(course[1].strip())
            tokens = nltk.word_tokenize(D[2*i+1].lower().strip())
            row.append(D[2*i+1].lower().strip())
            res.append(row)
        self.descriptions = np.array(res)
    
    # calculate the median GPA of the department using all the CAPE reviews (with average GPA received)
    def Median_GPA(self):
    '''
    this function is to calculate the median GPA of the department using all the CAPE reviews (with average GPA received)
    :param percent: 
    :return: median gpa
    '''
        mask = np.where(self.courses[:,-1] != '0.0')[0]
        target = self.courses[mask][:,-1].astype(np.float)
        self.gpa_median = np.median(target)
        return np.median(target)
    
    # calculate the median time spent of the department using all the CAPE reviews
    def Median_Time(self):
    '''
    this function is to calculate the median time spent of the department using all the CAPE reviews
    :param percent: 
    :return: median time spent
    '''
        mask = np.where(self.courses[:,6] != '0.0')[0]
        target = self.courses[mask][:,6].astype(np.float)
        self.time_median = np.median(target)
        return np.median(target)
        
    # discard CAPE reviews that have no match to course descriptions (course no longer offered)
    def cleanData(self):
    '''
    this function is to discard CAPE reviews that have no match to course descriptions (course no longer offered)
    :param percent: 
    :return: 
    '''
        s = np.array(list(set(self.descriptions[:,0])))
        mask = np.isin(self.courses[:,0],s)
        self.courses = self.courses[np.where(mask)]
        self.professors = np.array((list(set(self.courses[:,2]))))
        mask2 = np.where(self.courses[:,-1] == '0.0')[0]
        median = self.Median_GPA()
        self.Median_Time()
        for idx in mask2:
            self.courses[idx][-1] = str(median)
