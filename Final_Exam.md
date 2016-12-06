# A Brief Analysis of English Premier League Data
![premier-league-thumb](https://cloud.githubusercontent.com/assets/12864506/20905340/60175a74-bb11-11e6-84f7-b0589ef0bf23.png)



## Content:
 * Introduction
 * Analysis 1 : The distribution of the scoring times
  * Problem statement
  * Result
 * Analysis 2 : Goal Scorers
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

Along with the scoring times, I want to see what is the distribution of the scoring the winning goal time. I define a winning goal as the last goal in a match which finishes with one goal difference. Thus, in matches with one goal difference, I compute the distribution of the last goal. 
Finally, to explore the scoring time distribution for each team, I define a function called `team_scoring_time_dist`. This function will show two distribution for games in which one team plays at home and as a guest.

## Results:

![probability distribution of scoring time](https://cloud.githubusercontent.com/assets/12864506/20907280/3ea7fc68-bb1b-11e6-9b78-d7fbf1844f63.png)

The plot above shows there is a very smooth increase in the chance of scoring when we get closer to the end of the match; however, there are to picks at the end of the first and second halfs. It's safe to say teams are scoring more goals at the end of each half, with a higher chance at the end of the second half. 
Let's look at the distribution of the winning goal time.

![probability distribution of winning goal time](https://cloud.githubusercontent.com/assets/12864506/20907417/14a456ae-bb1c-11e6-9a7d-44680adfc3d2.png)

Interestingly, the distribution of the winning goal time is very similar to the scoring time. It can be concluded that if a team scores at the end of each half, there is a good chance for that goal to be the winning card. Regardless of two picks in the distribution, the slope of the distribution is still smooth, but higher than the slope of the distribution of scoring time. I would say this is pretty intuitive, there is a smaller chance to keep the result one team got in the early stages of the match till the end.

To see the goal scoring time distribution for one team, I use the function `team_scoring_time_dist` for *Manchester United*.

![probability distribution of scoring time manchester united](https://cloud.githubusercontent.com/assets/12864506/20907887/f7a40ab0-bb1e-11e6-9ac3-300c1186d763.png)

As a rule of thumb among footballers, there is a higher chance of scoring when you play in your home venue. The plot above shows this obviously. However, the picks are occuring in the same times as before.

# Analysis 2 : Goal Scorers
## Problem statement:
I would like to see what players scored for their club from season 2003-04 to 2013-14. I extract the name of goal scorers for each match. Then, I make a dictioanry containing the teams, the goal scorers for each team, and the number of goals each player scored. The result of this analysis is stored in `data/teams_scorers.json`. I will show the top scorer of each club, also for each season.

## Result:
A scheme of `data/teams_scorers.json` in which the scorers of each team and the number of goal any of them scored are scored, is shown below:

              {'Crystal Palace': {'Johnson': 20, 
              'Routledge': 1,  
              'Zaha': 1, ... }, 
              
              'Blackpool': {'Campbell': 12, 
              'Taylor-Fletcher': 5, 
              'Adam': 11, ... }, ... }

Among all scorers for a club, the one with the highest number of goals is shown in the plot below. 

![the number of goals of top scorers](https://cloud.githubusercontent.com/assets/12864506/20908397/adc67b5e-bb22-11e6-816a-a5cc26a6f5f9.png)





