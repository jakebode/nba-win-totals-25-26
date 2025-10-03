# tools package for displaying data in various formats

from IPython.display import display, HTML
import pandas as pd

# display generation module for showing DataFrames in Jupyter Notebooks
def show_df(df: pd.DataFrame):
    display(HTML(df.to_html(notebook=True).replace("<table", "<table style='display:block; overflow-x:auto; white-space:nowrap;'")))

# edits years to expanded date for consistency ('1999-00' --> '1999-2000')
def edit_year_format(year):
    edited_year = year[:4]
    if int(edited_year) <= 1998:
        edited_year += '-' + '19' + year[-2:]
    else:
        edited_year += '-' + '20' + year[-2:]
    return edited_year