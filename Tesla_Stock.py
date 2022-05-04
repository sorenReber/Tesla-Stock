# GDP by Nation by Soren Reber

import tkinter as tk
import pandas as pd
import matplotlib.pyplot as mpl
mpl.close('all')
def main():
    # Create a dataframe from the imported data
    df = pd.read_csv('TSLA.csv', index_col='Date', parse_dates=['Date'])
    # Display all the rows
    pd.set_option('display.max_rows', 639)
    # Create a window to display the dataframe.
    root = tk.Tk()
    frm_main = tk.Frame(root)
    frm_main.master.title("Tesla Stock October 2019 to April 2022")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=0)
    populate_main_window(frm_main, df)
    
    root.mainloop()

def populate_main_window(frm_main, df):
    # Display the dataframe
    sort_value = tk.StringVar()
    sort_value.set('True')
    dataframe_viewer = tk.Text(frm_main, width=90)
    dataframe_viewer.insert(tk.END, str(df))
    dataframe_viewer.config(state=tk.DISABLED)
   

    # Add a Scroll bar
    scrollbar = tk.Scrollbar(frm_main, orient='vertical', command=dataframe_viewer.yview)
    
    dataframe_viewer['yscrollcommand'] = scrollbar.set

    # Text Entry
    entry_field = tk.Entry(frm_main, width=16)
    entry_field.insert(tk.END, 'Date')
    lbl_entry_field = tk.Label(frm_main, text="Sort by:")
    btn_sort = tk.Button(frm_main, text='Sort')

    # Radio Buttons
    ascend_true = tk.Radiobutton(frm_main, text= 'Ascending Order', value='True', variable=sort_value)
    ascend_false = tk.Radiobutton(frm_main, text= 'Descending Order', value='False', variable=sort_value)

    # Grid Placement
    dataframe_viewer.grid(row=0, column=1, sticky='ew')
    scrollbar.grid(row=0, column=2, sticky='ns')
    lbl_entry_field.grid(row=1, column=2)
    entry_field.grid(row=1, column=3)
    btn_sort.grid(row=1, column=4)
    ascend_true.grid(row=2, column=3)
    ascend_false.grid(row=2, column=4)

    # Sort Button Command
    def sort_by():
        sort_by = entry_field.get().capitalize()
        sorted_value = sort_value.get()
        # Switch value back to Boolean
        if sorted_value == 'True':
            sorted_value = True
        elif sorted_value == 'False':
            sorted_value = False
        # Sort the Dataframe and update the text field
        sorted_df = df.sort_values(by=sort_by, ascending=sorted_value)
        dataframe_viewer.config(state=tk.NORMAL)
        dataframe_viewer.replace('0.0', tk.END, str(sorted_df))
        dataframe_viewer.config(state=tk.DISABLED)
    
    # Button Command
    btn_sort.config(command=sort_by)
if __name__== '__main__':
    main()