# GDP by Nation by Soren Reber

import tkinter as tk
from webbrowser import get
from numpy import average
import pandas as pd
import matplotlib.pyplot as mpl
mpl.close('all')
def main():
    # Create a dataframe from the imported data
    df = pd.read_csv('TSLA.csv', index_col='Date', parse_dates=['Date'])
    column_names = ['Date', 'High', 'Low','Close','Volume', 'Adj Close']
    # Display all the rows
    pd.set_option('display.max_rows', 639)
    # Create a window to display the dataframe.
    root = tk.Tk()
    frm_main = tk.Frame(root)
    frm_main.master.title("Tesla Stock October 2019 to April 2022")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=0)
    populate_main_window(frm_main, df, column_names)
    
    root.mainloop()

def populate_main_window(frm_main, df, column_names):
    # Display the dataframe
    sort_value = tk.StringVar()
    sort_value.set('True')
    dataframe_viewer = tk.Text(frm_main, width=90)
    dataframe_viewer.insert(tk.END, str(df))
    dataframe_viewer.config(state=tk.DISABLED)
   

    # Add a Scroll bar
    data_scrollbar = tk.Scrollbar(frm_main, orient='vertical', command=dataframe_viewer.yview)
    dataframe_viewer['yscrollcommand'] = data_scrollbar.set

    # Result label for average button
    lbl_avg_result = tk.Label(frm_main, width=10)

    # Text Entry
    column_var = tk.StringVar(value=column_names)
    list_field = tk.Listbox(frm_main, listvariable=column_var, height=6, selectmode=tk.BROWSE)

    # Buttons
    btn_sort = tk.Button(frm_main, text='Sort')
    btn_plot = tk.Button(frm_main, text='Plot')
    btn_avg = tk.Button(frm_main, text='Average')

    # Radio Buttons
    ascend_true = tk.Radiobutton(frm_main, text= 'Ascending Order', value='True', variable=sort_value)
    ascend_false = tk.Radiobutton(frm_main, text= 'Descending Order', value='False', variable=sort_value)

    # Grid Placement
    dataframe_viewer.grid(row=0, columnspan=5, sticky='ew')
    data_scrollbar.grid(row=0, column=5, sticky='ns')
    list_field.grid(rowspan=2, column=0)
    btn_sort.grid(row=1, column=1)
    ascend_true.grid(row=1, column=2)
    ascend_false.grid(row=1, column=3)
    btn_avg.grid(row=2, column=1)
    lbl_avg_result.grid(row=2, column=2)
    btn_plot.grid(row=2, column=3)
    
    # List selection function
    def get_list_selection():
        get_list_selection = list_field.curselection()
        if get_list_selection == ():
            sort_by = column_names[0]
        else: 
            sort_by = column_names[get_list_selection[0]]
        return sort_by

    # Sort Button Command
    def sort_by():
        sort_by = get_list_selection()
        sorted_value = sort_value.get()
        # Switch value from string to Boolean. 
        # Further work could be devoted to making this work without this step.
        if sorted_value == 'True':
            sorted_value = True
        elif sorted_value == 'False':
            sorted_value = False
        # Sort the Dataframe and update the text field
        sorted_df = df.sort_values(by=sort_by, ascending=sorted_value)
        dataframe_viewer.config(state=tk.NORMAL)
        dataframe_viewer.replace('0.0', tk.END, str(sorted_df))
        dataframe_viewer.config(state=tk.DISABLED)
    
    # Average Command
    def column_avg():
        sort_by = get_list_selection()
        if sort_by == 'Date':
            average = 'N/A'
            lbl_avg_result.config(text=average)
        else:
            average = df[sort_by].mean()
            lbl_avg_result.config(text="{:.2f}".format(average))

    # Button Command configuration
    btn_sort.config(command=sort_by)
    btn_avg.config(command=column_avg)


if __name__== '__main__':
    main()