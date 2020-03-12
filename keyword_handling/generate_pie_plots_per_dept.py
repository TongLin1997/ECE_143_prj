from Department import Department
from tokenizer import DataTokens
import pickle as pkl
import numpy
import plotly.graph_objects as plt

'''
Script that generates pie plots of the top 10 unique keywords in every department.
Most of this is data cleaning.
'''

with open('uniques_per_dept.pkl', 'rb') as f:
    uniques_per_dept = pkl.load(f)

depts = ['ECE','MATH','CSE','COGS']

#need to clean out garbage entries. i.e. "prerequisites"
cleaned = {}
cleaned['ECE'] = uniques_per_dept['ECE'][-20:]
cleaned['ECE'].pop(-9)
cleaned['ECE'].pop(-3)
cleaned['MATH'] = uniques_per_dept['MATH'][-20:]
cleaned['MATH'].pop(-8)
cleaned['MATH'].pop(-7)
cleaned['MATH'].pop(-6)
cleaned['MATH'].pop(-5)
cleaned['MATH'].pop(-2)
cleaned['MATH'].pop(-1)
cleaned['MATH'].pop(-8)
cleaned['MATH'].pop(-9)
cleaned['MATH'].pop(-5)
cleaned['MATH'].pop(-5)
cleaned['CSE'] = uniques_per_dept['CSE'][-30:]
for i in range(9):
    cleaned['CSE'].pop(-1)
cleaned['CSE'].pop(-2)
cleaned['CSE'].pop(-2)
cleaned['CSE'].pop(-2)
cleaned['CSE'].pop(-3)
cleaned['CSE'].pop(-4)
cleaned['CSE'].pop(-4)
cleaned['CSE'].pop(-5)
cleaned['COGS'] = uniques_per_dept['COGS'][-20:]
cleaned['COGS'].pop(-3)
cleaned['COGS'].pop(-3)
cleaned['COGS'].pop(-4)
cleaned['COGS'].pop(-5)
cleaned['COGS'].pop(-6)
cleaned['COGS'].pop(-10)
cleaned['COGS'].pop(-10)
cleaned['COGS'].pop(-10)
cleaned['COGS'].pop(-10)

#pie plots generated here
for dept in depts:
    toplot = cleaned[dept][-10:]
    toplot = list(zip(*toplot))
    fig = plt.Figure(
        data = [plt.Pie(values = toplot[1],labels = toplot[0],textinfo='label+value')],
        layout_title_text = "Top 10 Keywords in " + dept + " Department"
    )
    fig.show()