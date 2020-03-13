#Keyword Handling Scripts

##Run order

Make sure to have the entire repository downloaded. This especially includes the "raw_data" folder.

Run files in the following order:

1) create_container_structures.py
2) sort_tokens_by_department.py
3) query.py
4) generate_pie_plots_per_dept.py
5) heatmap.py

Steps 1,2 are not necessary if the user chooses to use the provided .pkl files.

Step 3 is also not required for the visualizations.

##Additional Notes

Department.py and tokenizer.py are data structures that are used to handle data from the "raw_data" folder

We have provided our generated .pkl files for your convenience.

In order to get the visualizations as we have them in the powerpoint, use our provided 'uniques_per_dept.pkl'