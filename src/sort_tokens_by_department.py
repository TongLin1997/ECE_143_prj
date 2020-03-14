from Department import Department
from tokenizer import DataTokens
import pickle as pkl

'''
script that sorts tokens unique to each department
must have run create_container_structures.py first.
'''
with open('department_tokenizers.pkl', 'rb') as f:
    department_tokenizers = pkl.load(f)

depts = ['ECE','MATH','CSE','COGS']


#first, group unique tokens into each department
keys = []
for dept in depts:
    keys.append(department_tokenizers[dept].token_counts.keys())
unique_keys = []
unique_quants = []
for i in range(len(keys)):
    temp = keys[i]
    for j in range(len(keys)):
        if i == j:
            continue
        temp = [el for el in temp if el not in keys[j]]
    unique_keys.append(temp)
    quants = []
    for el in temp:
        quants.append(department_tokenizers[depts[i]].token_counts[el])
    unique_quants.append(quants)

#next, threshold unique tokens. We threshold by minimum 3 occurences.
uniques_per_dept = {}
for i in range(len(depts)):
    words = []
    lens = []
    for el, occurs in zip(unique_keys[i],unique_quants[i]):
        if occurs < 3:
            continue
        words.append(el)
        lens.append(occurs)
    uniques_per_dept[depts[i]] = [words,lens]

#finally, sort the uniques by number of occurences and print.
for el in uniques_per_dept.keys():
    uniques_per_dept[el] = sorted(zip(uniques_per_dept[el][0],uniques_per_dept[el][1]), key=lambda pair: pair[1])
    print(uniques_per_dept[el])
    
#save to file for plotting later.
with open('uniques_per_dept.pkl', 'wb') as f:
    pkl.dump(uniques_per_dept,f)