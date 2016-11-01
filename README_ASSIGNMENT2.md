There are two scripts for the assignment 2:
*Search&Save* and *Analysis*

# *Search&Save* 

Use this script to search through Twitter and save the data

First, import required libraries. Two main libraries that we use here are *requests* and *urllib2*.
We store the data in *json* format which makes the analysis easier.

Second, we define some functions. Below, we introduce the functions:
1. *pretty_print* is an auxiliary function which prints json files in an easily readable format.

2. *get_token* sends a request to recieve the access token code.

3. *acc_token* returns the access token in the correct format.

4. *search_save* takes some keyword arguments, also the access token, searches through the right url, and saves the search results in json format.

# *Analysis*

Use this script to analyze the data.

First, import required libraries.

Second, we define some functions for each analysis we aim to commit. Below, we introduce the functions:
-  *read_data* simply takes the keyword arguments, and reads the json files.  
- **Analysis 1**

    * *find_hashtags* finds all the hashtags which have come with the query, and puts them into a data frame.
    
    * *max_hashtag* returns the hashtag which occured more frequently.
    
    * *plot_hashtags* plots a histogram to show the frequency of each hashtags which came with the query.
    
- **Analysis 2**
    
    * *number_of_favs* returns the frequency distribution of the number of favorites tweets are getting.
    
    * *plot_favs* plots the frequency distribution of the number of favorites tweets are getting. 
    
-  **Analysis 3**

    *number_of_followers* finds the number of followers of people who tweets about the query.  
    
    
-  **Analysis 4**

    * *country_of_tweet* finds the country from people tweet about the query.
    * *plot_countries* plots a histogram to show the frequency of each countries from people tweeted about the query.  
    
- **Analysis 5**
    * *average_positive* returns the average number of favorites and retweets tweets with positive attitudes are getting about the query.



