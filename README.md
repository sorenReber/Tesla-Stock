# Overview

The data used in this analysis is the daily stock price for Tesla beginning 9/30/2019 and ending 4/11/2022. The dataset can be found [here on Kaggle.com](https://www.kaggle.com/datasets/jillanisofttech/tesla-stock-price)

I wanted to create a program to analyze the Tesla stock price. I wanted it to be able to run independent of other programs like a web browser. Because of this I stayed away from Pandas ability to export and display the dataframe in HTML. I created my own GUI using tkinter to display the data and to be able to answer some basic analysis.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

* Question 1: What was the highest closing stock price point and when did it occur?
    * $1229.91 November 4th, 2021
* Question 2: Based on the plot of the closing stock price, is there a general upward trend in the stock price?
    * Overall for the entire time period, yes. However, the plot does show that at the final five months of the data, there has been a slight downward trend after the maximum stock price is reached. The dataset ends with a spike in the stock price that leaves the downward trend uncertain, but still possible.

# Development Environment

* VS Code
* GitHub

* Python 3.9.7 64-bit
* Pandas
* Tkinter
* Matplotlib

# Useful Websites

* [10 Minutes to Pandas - Official Site](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [Getting Started Tutorials - Official Site](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
* [Tkinter Listbox Tutorial](https://www.pythontutorial.net/tkinter/tkinter-listbox/)
* [Exploratory Data Analysis - Kaggle](https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas/notebook)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Future add: The ability to show a second plot that will more easily allow for comparisons.
* Fix/Improve: There is a clunky part of the code where I had to convert strings of True and False to boolean type for the sorting purposes. This was because tkinter was giving me issues when trying to use booleans for the radio buttons. Using strings worked but I would like to be able to take out that conversion.
* Improve: I would like the column names to be above the displayed dataframe, that way when scrolling through the dataframe the column names are still visible. Getting them to line up would be the tricky part and so for now I left it as is.