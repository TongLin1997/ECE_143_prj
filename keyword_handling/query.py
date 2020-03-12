from Department import Department
from tokenizer import DataTokens
import pickle as pkl

def query_func(q1,q2 = None,filename = 'department_tokenizers.pkl'):
    '''
    Keyword Query.This function returns a dictionary based on department. Each entry is a list of classes.
    inputs:
        q1: 1 word query as string
        q2: 1 word additional query as string or None.
            Passing None is equivalent to querying q1 as 1 word.
        filename: path to tokenizer.DataTokens class in a pkl.
    '''
    with open('department_tokenizers.pkl', 'rb') as f:
        department_tokenizers = pkl.load(f)

    if q2 is None:
        q2 = q1
    
    depts = ['ECE','MATH','CSE','COGS']

    classes = {}
    #search the token_locations for occurences of the queried token.
    for dept in depts:
        if q1 not in department_tokenizers[dept].token_locations.keys():
            classes[dept] = None
            continue
        if q2 not in department_tokenizers[dept].token_locations.keys():
            classes[dept] = None
            continue
        temp1 = department_tokenizers[dept].token_locations['machine']
        temp2 = department_tokenizers[dept].token_locations['learning']
        classes[dept] = list(set([el for el in temp1 if el in temp2]))
    return classes


#script that generates the machine learning courses
if __name__== "__main__":
    classes = query_func('machine','learning','department_tokenizers.pkl')
    with open('machine_learning_classes.pkl', 'wb') as f:
        pkl.dump(classes,f)