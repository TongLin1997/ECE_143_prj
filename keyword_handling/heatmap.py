#heatmap
import plotly.graph_objects as go
import numpy as np

"""
script to generate the heatmap we had in the presentation.
the big_dict sub-dictionaries were generated using the query function with the associated keywords.
"""

big_dict = {}
big_dict['Machine Learning'] =  {'ECE': ['ECE 175A'], 'MATH': ['MATH 181D'], 'CSE': ['CSE 151A', 'CSE 158', 'CSE 184', 'CSE 152B'], 'COGS': ['COGS 118A', 'COGS 185', 'COGS 118B', 'COGS 108', 'COGS 188', 'COGS 9']}
big_dict['System'] = {'ECE': ['ECE 111', 'ECE 181', 'ECE 161A', 'ECE 153', 'ECE 100', 'ECE 148', 'ECE 183', 'ECE 17', 'ECE 123', 'ECE 16', 'ECE 158B', 'ECE 163', 'ECE 194', 'ECE 5', 'ECE 171A', 'ECE 125B', 'ECE 45', 'ECE 101', 'ECE 145', 'ECE 154A', 'ECE 172A', 'ECE 166', 'ECE 121B', 'ECE 121A', 'ECE 165', 'ECE 157B', 'ECE 161B', 'ECE 158A', 'ECE 157A', 'ECE 128C', 'ECE 171B'], 'MATH': ['MATH 130', 'MATH 15A', 'MATH 31AH', 'MATH 187A', 'MATH 187B', 'MATH 104A', 'MATH 179', 'MATH 170A', 'MATH 20D', 'MATH 146', 'MATH 112A'], 'CSE': ['CSE 169', 'CSE 152B', 'CSE 140', 'CSE 132A', 'CSE 127', 'CSE 140L', 'CSE 124', 'CSE 30', 'CSE 150A', 'CSE 112', 'CSE 132B', 'CSE 184', 'CSE 113', 'CSE 176E', 'CSE 141', 'CSE 141L', 'CSE 167', 'CSE 21', 'CSE 125', 'CSE 158', 'CSE 20', 'CSE 120'], 'COGS': ['COGS 17', 'COGS 20', 'COGS 155', 'COGS 151', 'COGS 101B', 'COGS 121', 'COGS 100', 'COGS 123', 'COGS 124', 'COGS 107B', 'COGS 107A']}
big_dict['Probability'] =  {'ECE': ['ECE 109', 'ECE 153', 'ECE 155'], 'MATH': ['MATH 180A', 'MATH 181F', 'MATH 186', 'MATH 189', 'MATH 183', 'MATH 112A', 'MATH 11'], 'CSE': ['CSE 156', 'CSE 103', 'CSE 21'], 'COGS': ['COGS 14B']}
big_dict['Software Engineering'] = {'ECE': ['ECE 17', 'ECE 140A', 'ECE 140B', 'ECE 121A', 'ECE 30'], 'MATH': ['MATH 179'], 'CSE': ['CSE 118', 'CSE 112', 'CSE 110', 'CSE 113'], 'COGS': []}
big_dict['Web Design'] =  {'ECE': [], 'MATH': [], 'CSE': ['CSE 134B', 'CSE 136'], 'COGS': ['COGS 187B', 'COGS 8', 'COGS 187A', 'COGS 3']}
big_dict['Algebra'] =  {'ECE': ['ECE 25'], 'MATH': ['MATH 170A', 'MATH 103A', 'MATH 102', 'MATH 100C', 'MATH 100A', 'MATH 31AH', 'MATH 103B', 'MATH 18', 'MATH 100B', 'MATH 106'], 'CSE': ['CSE 5A', 'CSE 169', 'CSE 11'], 'COGS': []}
big_dict['Computer Vision'] = {'ECE': ['ECE 148'], 'MATH': [], 'CSE': ['CSE 152A', 'CSE 152', 'CSE 166', 'CSE 152B'], 'COGS': []}
big_dict['Brain'] =  {'ECE': [], 'MATH': [], 'CSE': [], 'COGS': ['COGS 175', 'COGS 174', 'COGS 177', 'COGS 179', 'COGS 107C', 'COGS 180', 'COGS 163', 'COGS 155', 'COGS 172', 'COGS 154', 'COGS 176', 'COGS 107A', 'COGS 170', 'COGS 189', 'COGS 157']}
big_dict['Digital Circuits'] =  {'ECE': ['ECE 111', 'ECE 108', 'ECE 165', 'ECE 25'], 'MATH': [], 'CSE': [], 'COGS': []}


for subj in big_dict.keys():
    for key in big_dict[subj].keys():
        big_dict[subj][key] = len(big_dict[subj][key])

x = list(big_dict.keys())
z = [list(big_dict[keys].items()) for keys in big_dict.keys()]
for i in range(len(z)):
    z[i] = [el[1] for el in z[i]]
    z[i] = [el/sum(z[i]) for el in z[i]]
z = np.asarray(z)
z = np.transpose(z)
fig = go.Figure(data=go.Heatmap(
                   z=z,
                   x=x,
                   y=['ECE','MATH','CSE','COGS'],
                   hoverongaps = False,
                   colorscale='blues'),
                   layout_title_text = "Percent Representation of Subjects per Department"
                   )

fig.show()