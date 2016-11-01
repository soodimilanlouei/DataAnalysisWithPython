# DataAnalysisWithPython

## Midterm:
The purpose of the midterm exam is to work with StackExchange API to extract the data from the website, save it, and analyze it.

In the Midterm.py file, the question and the required functions have been explained for each step. Here, I will give a big picture of how the analysis has been done.

# Midterm Exam

First, we import required modules.
Then we define the functions which are necessary to search and save the data.

## Functions:
- *time_epoch*: StackExchange uses time entries in epoch format. This function converets the date entry to epoch format. You can see an example of the output of this function.
- *search_save_question_tag*: This function search through questions in a specified time interval which contain some tags. It will check if there is anymore data on next pages. In that case, it will search through next page until there is no more data. Then the data will be saved in a json format. *time_epoch* is used inside this function.
- *read_data*: This function takes the path of the file, and reads it.
- *pretty_print* prints the data in a more readable form.
