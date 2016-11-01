# DataAnalysisWithPython

## Midterm:
The purpose of the midterm exam is to work with StackExchange API to extract the data from the website, save it, and analyze it.

In the Midterm.py file, the question and the required functions have been explained for each step. Here, I will give a big picture of how the analysis has been done.



First, we import required modules. Then we define the functions which are necessary to search and save the data.

## Functions:
- *time_epoch*: StackExchange uses time entries in epoch format. This function converets the date entry to epoch format. You can see an example of the output of this function.
- *search_save_question_tag*: This function search through questions in a specified time interval which contain some tags. It will check if there is anymore data on next pages. In that case, it will search through next page until there is no more data. Then the data will be saved in a json format. *time_epoch* is used inside this function.
- *read_data*: This function takes the path of the file, and reads it.
- *pretty_print* prints the data in a more readable form.


## Analysis 1:
### Steps:
   1. Get the questions with tag python and pandas. Inputs: tag='python;pandas', from_date='2016 01 01',to_date='2016 10 28'.
   2. Read the data using *read_data*.
   3. Parse the body for responses to collect a list of questions and user_id for the questions. To do so, we define two function: *get_question_list* and *get_user_id_list*.
   4. Use the user_id obtained to send a request again to get user profile. Obtain the badges count to determine weightage. Since we have a set of user IDs, we can use */users/{ids}* method to get the profiles. *search_save_user_profile* will take care of this. There are three types of badges: Gold, Silver, and Bronze. We assume the weight of 10, 5, and 2 for each badge, respectively. The output of this step will be a dictionary in which user IDs are keys and the weightage of each user is the value. Since we can get the profiles for at most 100 users, we divide the user IDs in batches with size 100. *user_id_batch_100* will do this. Then we use *id_question* and *top_questions* to find the questions which users with high weightage asked.
