
# coding: utf-8

# # Midterm Exam
# 
# First, we import required modules.
# Then we define the functions which are necessary to search and save the data.
# 
# ## Functions:
# - *time_epoch*: StackExchange uses time entries in epoch format. This function converets the date entry to epoch format. You can see an example of the output of this function.
# - *search_save_question_tag*: This function search through questions in a specified time interval which contain some tags. It will check if there is anymore data on next pages. In that case, it will search through next page until there is no more data. Then the data will be saved in a json format. *time_epoch* is used inside this function.
# - *read_data*: This function takes the path of the file, and reads it.
# - *pretty_print* prints the data in a more readable form.

# In[1]:

import requests
import json
import time
import operator
import matplotlib.pyplot as plt
get_ipython().magic(u'pylab inline')


# In[2]:

def time_epoch(date_time = '2016 01 01',pattern = '%Y %m %d'):
    t_ephoc = str(int(time.mktime(time.strptime(date_time, pattern))))
    return t_ephoc

time_epoch('2016 01 01')    


# In[3]:

def search_save_question_tag(tag, from_date, to_date):
    
    query = 'questions'
    key = 'Q8FdL9ZUYfXOw74bF8Q9Wg(('                           #This is the key which enables us to have a higher limit to search
    page = 1
    pattern = '%Y %m %d'
    formdate = time_epoch(from_date, pattern) 
    todate = time_epoch(to_date, pattern)
    
    # We need to make the correct url to send a request to StackExchange.
    
    url = 'https://api.stackexchange.com/2.2/'+query+'?key='+key+'&page='+str(page)+'&pagesize=100'+'&fromdate='+fromdate+     '&todate='+todate+'&order=desc&min='+'&sort=activity&tagged='+tag+'&site=stackoverflow'
    
    results = requests.get(url).json()
    new_results = results['items']
    
    #Here, we make sure we also get all the data in next pages.
    
    while results['has_more']==True:
        
        page+=1
        print page
        url = 'https://api.stackexchange.com/2.0/'+query+'?key='+key+'&page='+str(page)+'&pagesize=100'+'&fromdate='+fromdate+         '&todate='+todate+'&order=desc&min='+'&sort=activity&tagged='+tag+'&site=stackoverflow'
        results = requests.get(url).json()
        new_results += results['items']

    #At the end, we save the data in a json format to do analysis on later.
    
    path = query+tag
    with open(path+'.json', 'w') as file_out :
            json.dump(new_results, file_out,indent=2)
            


# In[4]:

def read_data(path):
    with open(path ,'r') as json_data:
        data = json.load(json_data)
        
    return data


# In[24]:

def pretty_print(jsondata) :
    print json.dumps(jsondata, indent=2)


# # Analysis 1:
# ## Steps:
#    1. Get the questions with tag python and pandas. Inputs: tag='python;pandas', from_date='2016 01 01',to_date='2016 10 28'.
#    2. Read the data using *read_data*.
#    3. Parse the body for responses to collect a list of questions and user_id for the questions. To do so, we define two function: *get_question_list* and *get_user_id_list*.
#    4. Use the user_id obtained to send a request again to get user profile. Obtain the badges count to determine weightage. Since we have a set of user IDs, we can use */users/{ids}* method to get the profiles. *search_save_user_profile* will take care of this. There are three types of badges: Gold, Silver, and Bronze. We assume the weight of 10, 5, and 2 for each badge, respectively. The output of this step will be a dictionary in which user IDs are keys and the weightage of each user is the value. Since we can get the profiles for at most 100 users, we divide the user IDs in batches with size 100. *user_id_batch_100* will do this. Then we use *id_question* and *top_questions* to find the questions which users with high weightage asked.

# In[5]:

tag = 'python;pandas'
from_date = '2016 01 01'
to_date = '2016 10 28'
search_save(query, tag, from_date, to_date)


# In[6]:

def get_question_list(data):
    
    question_list = []
    
    #In order to get the questions out of the data, we store the value of key 'title'.
    for i in range(len(data)):
        question_list.append(data[i]['title'])
        
    return question_list
    


# In[7]:

def get_user_id_list(data):
    
    user_id_list = []
    
    for i in range(len(data)):

        if 'user_id' in data[i]['owner']:
            user_id_list.append(data[i]['owner']['user_id'])
        else:
            continue

    #We return the user IDs information in both formats of set and list; set to have the unique IDs, 
    #and list, in case of finding the frequency of each user who asked questions with the specified tags.
    
    user_id_set = list(set(user_id_list))
    
    return user_id_list, user_id_set
        
    


# In[8]:

#Read the data.

data_question_tag = read_data('questionspython;pandas.json')


# In[25]:

# One example of how the data looks like.

pretty_print(data_question_tag[0])


# In[9]:

question_list = get_question_list(data_question_tag)
user_id_list, user_id_set = get_user_id_list(data_question_tag)

print 'Number of questions = '+ str(len(question_list))
print 'Number of user IDs = ' + str(len(user_id_set))


# In[10]:

#Now, we know that we have 5118 unique IDs, we put them in batches with size 100 and the remiander in another list.
#Then, we join values in each batch together with ; to send the correct format of request.

def user_id_batch_100(user_data_set):
    
    user_id_100 = []
    list1 = user_id_set[0:100]
    list2 = user_id_set[100:200]
    list3 = user_id_set[200:300]
    list4 = user_id_set[300:400]
    list5 = user_id_set[400:500]
    list6 = user_id_set[500:-1]
    
    
    list11 = []
    for i in range(len(list1)):
        list11.append(str(list1[i]))
        
        
    list22 = []
    for i in range(len(list2)):
        list22.append(str(list2[i]))
        
    list33 = []
    for i in range(len(list3)):
        list33.append(str(list3[i]))
    list44 = []
    for i in range(len(list4)):
        list44.append(str(list4[i]))
    list55 = []
    for i in range(len(list5)):
        list55.append(str(list5[i]))
        
        
    u_format1 = ";".join(list11)
    u_format2 = ";".join(list22)
    u_format3 = ";".join(list33)
    u_format4 = ";".join(list44)
    u_format5 = ";".join(list55)

    user_id_100.append(u_format1)
    user_id_100.append(u_format2)
    user_id_100.append(u_format2)
    user_id_100.append(u_format2)
    user_id_100.append(u_format2)
    return user_id_100

        
    return user_id_100
        


# In[11]:

user_batch = user_id_batch_100(user_id_set)


# In[12]:

def search_save_user_profile(user_id_list):
    
    query = 'users'
    
    new_results = []
    
    for i in range(len(user_id_list)):
    
        key = 'Q8FdL9ZUYfXOw74bF8Q9Wg(('
        page = 1

        url = 'https://api.stackexchange.com/2.2/'+query+'/'+user_id_list[i]+'?key='+key+'&page='+str(page)+'&pagesize=100'+        '&order=desc&sort=reputation&site=stackoverflow'
        results = requests.get(url).json()
        new_results += results['items']


        while results['has_more']==True:

            page+=1
            print page
            url = 'https://api.stackexchange.com/2.2/'+query+'/'+user_id_list[i]+'?key='+key+'&page='+str(page)+            '&pagesize=100'+'&order=desc&sort=reputation&site=stackoverflow'
            results = requests.get(url).json()
            new_results += results['items']

    path = query+'Badge_count'
    with open(path+'.json', 'w') as file_out :
            json.dump(new_results, file_out,indent=2)

  


# In[13]:

#Find and store the data.

search_save_user_profile(user_batch)


# In[14]:

#Read the data.

data_user_badge_count = read_data('usersBadge_count.json')


# In[26]:

# One example of how the data looks like.

pretty_print(data_user_badge_count[0])


# In[15]:

#Define the weight of each badge.

weightage = {'gold': 10, 'silver':5, 'bronze':2}


# In[16]:

def id_weightage(data, weightage):
    
    ids_weightage = {}
    
    for i in range(len(data)):
        ids_weightage[data[i]['user_id']] = data[i]['badge_counts']['gold']*weightage['gold']        +data[i]['badge_counts']['silver']*weightage['silver']+data[i]['badge_counts']['bronze']*weightage['bronze']
    
    #Sort the dictionary based on the reputation of each user.
    
    ids_weightage = sorted(ids_weightage.items(), key=operator.itemgetter(1), reverse=True)
    
    return ids_weightage


# In[17]:

user_id_weightage = id_weightage(data_user_badge_count, weightage)


# In[27]:

#This is how the result looks like.

user_id_weightage


# In[28]:

def id_question(data):
    
    id_q = {}
    
    for i in range(len(data)):
        
        if 'user_id' in data[i]['owner']:
            id_q.setdefault(data[i]['owner']['user_id'],[])
            id_q[data[i]['owner']['user_id']].append(data[i]['title'])
        else:
            continue
    
    return id_q


# In[29]:

user_id_question = id_question(data_question_tag)


# In[32]:

def top_questions(id_weightage, id_question):
    
    #Since the id_weightage sorted based on the weightage, the first 5 entries of each question gives the most weighted users.
    
    for c in range(5):
        print 'User '+str(id_weightage[c][0])+ ' with weightage = '+str(id_weightage[c][1])+ ' >>> Question:\n '
        print id_question[id_weightage[c][0]]
        print '\n'


# In[33]:

top_5_questions = top_questions(user_id_weightage,user_id_question)


# # Analysis 2:
# 
# ## Steps:
#    1. For each of the User ID that you have collected, ping the API to get all the tags that user has identified with. Here, we use */user/{ids}/tags* method to get the data. Then we save it. *get_id_tags* function is defined to serve this purpose. *id_tag* gives a dictionary in which the user IDs are keys and tags for each user are values.
#    2. Creat a file for each topic, containing user_id, user_name and link to their profile sorted by reputation. *get_user_profile* gives a dictionary which contains the user_name, link, and reputation of each user ID. *topic_user* is also defined to show the users who used each tag sorted by their reputation.
#    3. For a given topic (say python), what are the top users who have reputation in that topic. *top_users_tag* prints out the first or the first two top users who are reputated in a specified topic.

# In[20]:

def get_id_tags(user_id_list):
    
    query = 'users'
    
    new_results = []
    
    for i in range(len(user_id_list)):
    
        key = 'Q8FdL9ZUYfXOw74bF8Q9Wg(('
        page = 1

        url = 'https://api.stackexchange.com/2.2/'+query+'/'+user_id_list[i]+'/tags'+'/?key='+key+'&page='+str(page)+'&pagesize=100'+         '&order=desc&sort=popular&site=stackoverflow'
        

        results = requests.get(url).json()
        new_results += results['items']


        while results['has_more']==True:

            page+=1
            print page
            url = 'https://api.stackexchange.com/2.2/'+query+'/'+user_id_list[i]+'/tags'+'/?key='+key+'&page='+str(page)+'&pagesize=100'+             '&order=desc&sort=popular&site=stackoverflow'
            results = requests.get(url).json()
            new_results += results['items']

    path = query+'tags'
    with open(path+'.json', 'w') as file_out :
            json.dump(new_results, file_out,indent=2)

  
    


# In[47]:

#Find and store the data.

get_id_tags(user_batch)


# In[34]:

#Read the data.

data_user_tag = read_data('userstags.json')


# In[54]:

def id_tag(data):
    
    ids_tags = {}
    
    for i in range(len(data)):
        ids_tags.setdefault(data[i]['user_id'],set())
        ids_tags[data[i]['user_id']].add(data[i]['name'])
        
    return ids_tags


# In[55]:

ids_tags = id_tag(data_user_tag)


# In[57]:

#For example, the tags associated with user_id : 53468 look like this:

ids_tags[53468]


# In[50]:

def get_user_profile(data):
    user_pro = {}
    for i in range(len(data)):
        user_pro.setdefault(data[i]['user_id'],{})
        user_pro[data[i]['user_id']] = {'reputation': data[i]['reputation'],'user_name':data[i]['display_name'],'link':data[i]['link']}
        
    return user_pro


# In[51]:

# We use *data_user_badge_count* that we stored in Analysis 1.

user_profiles = get_user_profile(data_user_badge_count)


# In[58]:

#For example, the profile associated with user_id : 53468 looks like this:

user_profiles[53468]


# In[59]:

def topic_user(data,user_profiles):

    topic_ids = {}
    
    for i in range(len(data)):

        topic_ids.setdefault(data[i]['name'],{})
        topic_ids[data[i]['name']][data[i]['user_id']] = user_profiles[data[i]['user_id']]
        
    #Sort the values in the dictionary based on the reputatio of each user.
    
    for i in topic_ids:
        
        sorted_val = sorted(topic_ids[i].items(), key = lambda x: x[1]['reputation'], reverse=True)
        topic_ids[i]=(sorted_val)
        
    return topic_ids


# In[64]:

topics_users = topic_user(data_user_tag,user_profiles)


# In[67]:

#This how  the results look like for topic : python

topics_users['python']


# In[68]:

def top_users_tag(topic, topic_user):
    num_users = len(topic_user[topic])
    if num_users == 1:
        print topic_user[topic][0]
    else:
        print topic_user[topic][0]
        print topic_user[topic][1]


# In[69]:

#First two top users on topic python

top_users_reput_tag = top_users_tag('python', topics_users)


# # Analysis 3:
# ## Steps:
#    1. For each of the badge type, find how many users (based on the data you have collected) have badge. To find the number of badges for each user, we can use the result of Analysis 1. In dictionary *user_id_weightage* the users whose values are zero, have no badges. *users_with_no_badge* finds that number.
#    2. We want to see what badges are popular among the users. *popular badge* counts the number of each type of badges.

# In[175]:

def users_with_no_badge(user_id_weightage):
    
    user_w = dict(user_id_weightage)
    c = 0
    
    for i in user_w:
        if user_w[i]==0:
            c+=1
        else:
            continue
            
    print str(c)+' users out of '+ str(len(user_w))+ ' have no badge'
    return c


# In[176]:

users_no_badge = users_with_no_badge(user_id_weightage)


# In[181]:

def popular_badge(data):
    
    num_badge = {'gold':0, 'silver':0, 'bronze':0}
    
    for i in range(len(data)):
        
        num_badge['gold'] += data[i]['badge_counts']['gold']
        num_badge['silver'] += data[i]['badge_counts']['silver']
        num_badge['bronze'] += data[i]['badge_counts']['bronze']
    
    return num_badge


# In[182]:

popular_badges = popular_badge(data_user_badge_count)


# In[184]:

popular_badges

#We can see 'bronze' is the most popular badge among all badges.


# # Analysis 4:
# ## Steps:
# 1. For each of the question that is asked, find out the tags attached to it. *search_save_question* uses */questions* method to find this data. *all_tags* gives the tags associated with each question in a dictionary format.
# 2. Find how many numbers of answers have been given for each question. For each tag, calculate the number of questions asked and how many times it has been answered. *number_of_answers* gives a dictionary of the questions and the number of answers given to that question. *tag_number_of_questions* and *tag_number_of_answers* will find that for each tag how many questions have been asked, and how many answers given to them, respectively.

# In[67]:

def search_save_question(from_date, to_date):
    
    query = 'questions'
    key = 'Q8FdL9ZUYfXOw74bF8Q9Wg(('                           #This is the key which enables us to have a higher limit to search
    page = 1
    pattern = '%Y %m %d'
    formdate = time_epoch(from_date, pattern) 
    todate = time_epoch(to_date, pattern)
    
    # We need to make the correct url to send a request to StackExchange.
    
    url = 'https://api.stackexchange.com/2.2/'+query+'?key='+key+'&page='+str(page)+'&pagesize=100'+'&fromdate='+fromdate+     '&todate='+todate+'&order=desc&min='+'&sort=activity&site=stackoverflow'
    
    results = requests.get(url).json()
    new_results = results['items']
    
    #Here, we make sure we also get all the data in next pages.
    
    while results['has_more']==True:
        
        page+=1
        print page
        url = 'https://api.stackexchange.com/2.0/'+query+'?key='+key+'&page='+str(page)+'&pagesize=100'+'&fromdate='+fromdate+         '&todate='+todate+'&order=desc&min='+'&sort=activity&site=stackoverflow'
        results = requests.get(url).json()
        new_results += results['items']

    #At the end, we save the data in a json format to do analysis on later.
    
    path = query
    with open(path+'.json', 'w') as file_out :
            json.dump(new_results, file_out,indent=2)
            


# In[70]:

#Read the data.

data_question_tag = read_data('questionspython;pandas.json')


# In[71]:

def all_tags(data):
    
    all_tags = set()
    
    for i in range(len(data)):
        
        for j in data[i]['tags']:
            all_tags.add(j)
    
    return all_tags


# In[72]:

all_tags_questions = all_tags(data_question_tag)


# In[73]:

all_tags_questions


# In[74]:

def number_of_answers(data):
    
    num_answers = {}
    
    for i in range(len(data)):
        num_answers[data[i]['title']]=data[i]['answer_count']
        
    return num_answers


# In[75]:

num_of_answers = number_of_answers(data_question_tag)


# In[78]:

num_of_answers


# In[79]:

def tag_number_of_questions(data):
    
    tag_n_q = {}
    
    for i in range(len(data)):
        for j in data[i]['tags']:
            tag_n_q.setdefault(j,0)
            tag_n_q[j]+=1
            
    return tag_n_q
            


# In[80]:

tag_num_of_questions = tag_number_of_questions(data_question_tag)


# In[82]:

tag_num_of_questions['python']


# In[83]:

def tag_number_of_answers(data):
    
    tag_n_a = {}
    
    for i in range(len(data)):
        for j in data[i]['tags']:
            tag_n_a.setdefault(j,0)
            tag_n_a[j]+=data[i]['answer_count']
            
    return tag_n_a


# In[84]:

tag_num_of_answers = tag_number_of_answers(data_question_tag)


# In[86]:

tag_num_of_answers['python']


# # Analysis 5:
# ## Steps:
# 1. Find out the user whose questions have been downvoted the most.

# In[87]:

def id_downvoted(data):
    id_down = {}
    for i in range(len(data)):
        if 'user_id' in data[i]['owner']: 
            id_down.setdefault(data[i]['owner']['user_id'],0)
            id_down[data[i]['owner']['user_id']]+=data[i]['score']
            
    sorted_down = sorted(id_down.items(), key=operator.itemgetter(1))
        
    return sorted_down


# In[88]:

id_down_voted = id_downvoted(data_question_tag)


# In[89]:

#User with ID 6612697 has got the most downvotes.

id_down_voted


# In[ ]:



