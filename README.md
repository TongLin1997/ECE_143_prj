# ECE 143 Project Goup 5: Class Search System Based on Keywords and CAPE Reviews 

## group members:

Group members:

|Name|Email|
|---|---|
|Mikhail Kardash|mkardash@ucsd.edu|
|Jiabei Han|XXXX@ucsd.edu|
|Linyan Zheng|l5zheng@ucsd.edu|
|Tong Lin|tol009@ucsd.edu|

## Presentation

You can view our presentation by click here https://github.com/TongLin1997/ECE_143_prj/blob/master/Presentation.pdf

## packages that need to be installed

```
numpy

re

nltk

graphviz

plotly

pandas

pickle
```

## File Structure

```
raw_data/
    COGS_CAPE.txt
    COGS_Description.txt
    CSE_CAPE.txt
    CSE_Description.txt
    ECE_CAPE.txt
    ECE_Description.txt
    MATH_CAPE.txt
    MATH_Description.txt 
    
src/
    GPA_best_course.py
    GPA_best_time.py
    GPA_by_department.py
    GPA_by_professor.py	
    TIME_by_professor.py
    class.py
    Department.py
    create_container_structures.py
    generate_pie_plots_per_dept.py
    heatmap.py
    query.py
    sort_tokens_by_department.py
    tokenizer.py
    department_tokenizers.pkl
    departments.pkl
    machine_learning_classes.pkl
    uniques_per_dept.pkl

Final_proj.html
Final_proj.ipynb
Presentation.pdf
README.md
```

## how to run

### option1 
```
1.install all packages mentioned above. NLTK requires an extra download. Either run nltk.download() or go to http://nltk.org/nltk_data/ and download the punkt tokenizer models.

2.download all eight files in "raw_data" folder  (COGS_CAPE.txt, COGS_Description.txt, CSE_CAPE.txt, CSE_Description.txt, ECE_CAPE.txt, ECE_Description.txt, MATH_CAPE.txt, MATH_Description.txt) Download 
uniques_per_dept.pkl from the "keyword_handling" folder.

3.download Final_proj.ipynb and put it on the same path as eight files

4.open Final_proj.ipynb in Jupter Notebook and run from the first cell.
```


### option2
```
#### Run order

Make sure to have the entire repository downloaded. This especially includes the "raw_data" folder.

Run files in the following order:

1) create_container_structures.py
2) sort_tokens_by_department.py
3) query.py
4) generate_pie_plots_per_dept.py
5) heatmap.py

Steps 1,2 are not necessary if the user chooses to use the provided .pkl files.

Step 3 is also not required for the visualizations.

#### Additional Notes

Department.py and tokenizer.py are data structures that are used to handle data from the "raw_data" folder

We have provided our generated .pkl files for your convenience.

In order to get the visualizations as we have them in the powerpoint, use our provided 'uniques_per_dept.pkl'
```




