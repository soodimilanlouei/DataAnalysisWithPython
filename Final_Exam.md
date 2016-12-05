# A Brief Analysis of English Premier League 
![premier-league-thumb](https://cloud.githubusercontent.com/assets/12864506/20905340/60175a74-bb11-11e6-84f7-b0589ef0bf23.png)



## Content:
 * Introduction
 * Analysis 1 : The distribution of the scoring times
  * Problem statement
  * Result

## Introduction

I worked on a dataset containing all matches played in the EPL starting from season 2001 to season 2014. You can find this dataset in folder `data/2002-2013-EPL.csv` For each match, the home/away team, home/away score, home/away scorers, and the time of scoring have been stored in the dataset. Below, you can see a scheme from the raw dataset. In the column `Home Scorers` and `Away Scorers`, `g` is used to indicate a goal, also `og` and `pen` are used to indicate own goal and penalty.


Season | Date | Home Team | Home Score | Home Scorers | Away Team | Away Score | Away Scorers | Venue
----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- 
 2001-2002 | 6/11/2002 | Blackburn Rovers|3|Andy Cole,53,g;Damien Duff,66,g;Andy Cole,81,g|Fulham|0|NaN|Ewood Park
 2001-2002 | 6/11/2002 | Leicester City|2|Paul Dickov,60,g;Matthew Piper,71,g|Tottenham Hotspur|1|Teddy Sheringham,54,g|Filbert Street


## Analysis 1 : The distribution of the scoring times
### Problem statement:
For the beginning, I want to see what is the distribution of the scoring times. To do so, I split the columns `Home Scorer` and `Away Scorers`, generating a list for each match containing the minue of each goal scored. I exclude the own goals, since they cannot reflect the pattern of the scoring. So, any goal which has the `og` tag is removed from the analysis. I store these list in a dataframe which looks like below. The dataframe is stored in `data/matches_goal_min`.

Home Team | Home Score | Home Score Min | Away Team | Away Score | Away Score Min
----- | ----- | ----- | ----- | ----- | ----- 
 Blackburn Rovers|3|[53, 66, 81]|Fulham|0|[]
 Leicester City|2|[60, 71]|Tottenham Hotspur|1|[54]

Along with the scoring times, I want to see what is the distribution of the scoring the winning goal. I define a winning goal time as the minute of last goal in a match which finishes with one goal difference. Thus, in matches with one goal difference, I compute the distribution of the last goal. 
Finally, to explore the scoring time distribution for each team, I define a function called `team_scoring_time_dist`.

## Results:

![probability distribution of scoring time](https://cloud.githubusercontent.com/assets/12864506/20907280/3ea7fc68-bb1b-11e6-9b78-d7fbf1844f63.png)

The plot above shows there is a very smooth increase in the chance of scoring when we get closer to the end of the match; however, there are to picks at the end of the first and second halfs. It's safe to say teams are scoring more goals at the end of each half, with a higher chance at the end of the second half. 
Let's look at the distribution of the winning goal time.
