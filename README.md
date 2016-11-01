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

A snapshot of the results: 
- data collected for the questions and tags:

		{

		  "is_answered": true, 

		  "tags": [
			 "python", 
			 "pandas", 
			 "numpy"
		  ], 

		  "bounty_closes_date": 1478287199, 

		  "title": "daily data, resample every 3 days, calculate over trailing 5 days efficiently", 

		  "last_activity_date": 1477688683, 

		  "answer_count": 2, 

		  "creation_date": 1477272066, 

		  "score": 3,

		  "link": "http://stackoverflow.com/questions/40209520/daily-data-resample-every-3-days-calculate-over-trailing-5-days-efficiently",

		  "bounty_amount": 500,

		  "owner": {
			 "user_id": 2336654, 
			 "profile_image": "https://i.stack.imgur.com/cZOEs.jpg?s=128&g=1", 
			 "user_type": "registered", 
			 "reputation": 29968, 
			 "link": "http://stackoverflow.com/users/2336654/pirsquared", 
			 "accept_rate": 96, 
			 "display_name": "piRSquared"
		  }, 

		  "view_count": 67,

		  "last_edit_date": 1477686080, 

		  "question_id": 40209520
		}


- question_list: ['How can I replicate excel COUNTIFS in python/pandas?',.....]
- user_id_set: [5906433, 5552408, 3760132,.... ]

- - data collected for user IDs and badge counts:

		{
		  "is_employee": false, 
		  "last_access_date": 1476725496, 
		  "user_id": 237696, 
		  "account_id": 85196, 
		  "badge_counts": {
		    "bronze": 71, 
		    "silver": 38, 
		    "gold": 4
		  }, 
		  "last_modified_date": 1477424115, 
		  "profile_image": "https://i.stack.imgur.com/cUqoH.jpg?s=128&g=1", 
		  "user_type": "registered", 
		  "reputation_change_day": 0, 
		  "creation_date": 1261583297, 
		  "reputation_change_quarter": 89, 
		  "reputation_change_year": 901, 
		  "reputation": 7849, 
		  "link": "http://stackoverflow.com/users/237696/mr-sk", 
		  "location": "Bandar Seri Begawan, Brunei", 
		  "accept_rate": 80, 
		  "display_name": "mr-sk", 
		  "reputation_change_month": 89, 
		  "website_url": "http://www.nycdayz.com", 
		  "reputation_change_week": 0
		}
   
## Analysis 2:

### Steps:
   1. For each of the User ID that you have collected, ping the API to get all the tags that user has identified with. Here, we use */user/{ids}/tags* method to get the data. Then we save it. *get_id_tags* function is defined to serve this purpose. *id_tag* gives a dictionary in which the user IDs are keys and tags for each user are values.
   2. Creat a file for each topic, containing user_id, user_name and link to their profile sorted by reputation. *get_user_profile* gives a dictionary which contains the user_name, link, and reputation of each user ID. *topic_user* is also defined to show the users who used each tag sorted by their reputation.
   3. For a given topic (say python), what are the top users who have reputation in that topic. *top_users_tag* prints out the first or the first two top users who are reputated in a specified topic.
   
## Analysis 3:
### Steps:
   1. For each of the badge type, find how many users (based on the data you have collected) have badge. To find the number of badges for each user, we can use the result of Analysis 1. In dictionary *user_id_weightage* the users whose values are zero, have no badges. *users_with_no_badge* finds that number.
   2. We want to see what badges are popular among the users. *popular badge* counts the number of each type of badges.   

# Analysis 4:
## Steps:
   1. For each of the question that is asked, find out the tags attached to it. *search_save_question* uses */questions* method to find this data. *all_tags* gives the tags associated with each question in a dictionary format.
   2. Find how many numbers of answers have been given for each question. For each tag, calculate the number of questions asked and how many times it has been answered. *number_of_answers* gives a dictionary of the questions and the number of answers given to that question. *tag_number_of_questions* and *tag_number_of_answers* will find that for each tag how many questions have been asked, and how many answers given to them, respectively.
   
## Analysis 5:
### Steps:
1. Find out the user whose questions have been downvoted the most.
