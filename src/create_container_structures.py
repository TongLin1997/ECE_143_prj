from Department import Department
from tokenizer import DataTokens
import pickle as pkl
'''
This file creates two data structures and saves them to a file.
The first structure contains all department data, CAPES and Descriptions. (Department structure)
The second structure contains description data that is tokenized and sorted by course.
'''

#dictionary for the file paths.
file_dict = {'ECE': ['../raw_data/ECE_Description.txt','../raw_data/ECE_CAPE.txt'],
            'MATH': ['../raw_data/MATH_Description.txt','../raw_data/MATH_CAPE.txt'],
            'CSE': ['../raw_data/CSE_Description.txt','../raw_data/CSE_CAPE.txt'],
            'COGS': ['../raw_data/COGS_Description.txt','../raw_data/COGS_CAPE.txt']}


#create dictionary to contain structures.
departments = {}
for el in file_dict.keys():
    departments[el] = Department(el)
    departments[el].loadDescription(file_dict[el][0])
    departments[el].loadCourses(file_dict[el][1])

#save the dictionary
with open('departments.pkl', 'wb') as f:
    pkl.dump(departments,f)

with open('departments.pkl', 'rb') as f:
    departments = pkl.load(f)

#tokenizer structure that to be used for queries later on.
department_tokenizers = {}
for el in departments.keys():
    department_tokenizers[el] = DataTokens()
    for course in departments[el].descriptions:
        department_tokenizers[el].desc2token(course[1] + ' ' + course[2],course[0])

with open('department_tokenizers.pkl', 'wb') as f:
    pkl.dump(department_tokenizers,f)