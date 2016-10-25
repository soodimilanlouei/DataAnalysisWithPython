
# coding: utf-8

# # Use this script to search through Twitter and save the data
# 
# 
# 
# 
# 
# First, import required libraries. Two main libraries that we use here are *requests* and *urllib2*.
# We store the data in *json* format which makes the analysis easier.
# 
# Second, we define some functions. Below, we introduce the functions:
# 1. *pretty_print* is an auxiliary function which prints json files in an easily readable format.
# 
# 2. *get_token* sends a request to recieve the access token code.
# 
# 3. *acc_token* returns the access token in the correct format.
# 
# 4. *search_save* takes some keyword arguments, also the access token, searches through the right url, and saves the search results in json format.

# In[1]:

import requests
import urllib2
import json
import base64
import pandas
from collections import Counter
import matplotlib.pyplot as plt
get_ipython().magic(u'pylab inline')


# In[2]:

def pretty_print(jsondata) :
    print json.dumps(jsondata, indent=2)


# In[3]:

def get_token():
    consumer_key = "fQGKP2WVd3tuZtftBUVIBjDvg"
    consumer_secret = "6eahgFefwaH7VRD89pXaNhyU5vMsX5Lgywy5cDvJC7CP0bFCLe"
    b64 = base64.b64encode(consumer_key+":"+consumer_secret)
    headers = {'Authorization':' Basic '+b64 , 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    r = requests.post("https://api.twitter.com/oauth2/token", headers = headers , data = {'grant_type':'client_credentials'})
    return r.text


# In[4]:

def acc_token():
    my_account=get_token()
    json_acceptable_string = my_account.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    acc_token = ' Bearer '+str(d['access_token'])
    return acc_token


# In[186]:

def save_search(kargs,access_token,output=False):
    
    results = requests.get("https://api.twitter.com/1.1/search/tweets.json",headers = {'Authorization':access_token},params = kargs).json()

    collected_tweets = results["statuses"]
    collected_meta_data = results["search_metadata"]
    while True :
        try :
            next_results = collected_meta_data["next_results"]

            kwargs = urllib2.urlparse.parse_qs(next_results[1:])


            results =  requests.get("https://api.twitter.com/1.1/search/tweets.json",headers = {'Authorization':access_token},params = kwargs).json()

            collected_tweets += results["statuses"]
            collected_meta_data = results["search_metadata"]
        except :
            break

            
            
    while True:
        try:
            with open('./search/'+kargs['q'] + ".json", 'w') as file_out :
                json.dump(collected_tweets, file_out,indent=2)
            path = './search/'+kargs['q'] + ".json"
            break
        except IOError:
            with open('./search/'+kargs['q'][:4] + ".json", 'w') as file_out :
                json.dump(collected_tweets, file_out,indent=2)
            path = './search/'+kargs['q'][:4] + ".json"
            break
            
            
            
    with open(path, 'w') as file_out :
            json.dump(collected_tweets, file_out,indent=2)
    if output:
        return collected_tweets


# In[8]:

access_token = acc_token()


# Here, we want to search tweets about Manchester United and Manchester City! We want to make sure that we cover all hashtags, with lower letters and upper letters.

# In[46]:

key_words_list_U = ["#MUFC", "#mufc", "#Mufc"]
key_words_str_U = " OR ".join(key_words_list)
kargs_U = {'q':key_words_str,'lang':'en','count':100,'per_page':50}
save_search(kargs_U,access_token)


# In[42]:

key_words_list_C = ["#MCFC", "#mcfc", "#Mcfc"]
key_words_str_C = " OR ".join(key_words_list)
kargs_C = {'q':key_words_str,'lang':'en','count':100,'per_page':100}
save_search(kargs_C,access_token)


# In[ ]:




# In[ ]:




# In[ ]:




# In[187]:

key_words_list_U = ["MUFC :)", "mufc :)", "Mufc :)", "ManUtd :)"]
key_words_str_U = " OR ".join(key_words_list_U)
kargs_U = {'q':key_words_str_U,'count':100,'per_page':100}
save_search(kargs_U,access_token)


# In[188]:

key_words_list_C = ["MCFC :)", "mcfc :)", "Mcfc :)", "ManCity :)"]
key_words_str_C = " OR ".join(key_words_list_C)
kargs_C = {'q':key_words_str_C,'count':100,'per_page':100}
save_search(kargs_C,access_token)


# In[ ]:



