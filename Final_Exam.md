# A Brief Analysis of English Premier League Data
![premier-league-thumb](https://cloud.githubusercontent.com/assets/12864506/20905340/60175a74-bb11-11e6-84f7-b0589ef0bf23.png)



## Content:

 * Introduction
 
 * Analysis 1 : Champions' performance
  * Performance definition
  * Result
  
 * Analysis 2 : Individual performance
  * Results and outputs
  
 * Analysis 3 : Goal Scorers
  * Problem statement
  * Result
  
 * Analysis 4 : The distribution of the scoring times
  * Problem statement
  * Result
  
 * Analysis 5 : Geographical relation
  * Probelm statement
  * Results
  
 * Cross-checking with an API



## Introduction
**************************************************************************************************************************************
I worked on a dataset containing all matches played in the EPL starting from season 2001 to season 2012. You can find this dataset in folder `data/2002-2012-EPL.csv` For each match, the home/away team, home/away score, home/away scorers, and the time of scoring have been stored in the dataset. Below, you can see a scheme from the raw dataset. In the column `Home Scorers` and `Away Scorers`, `g` is used to indicate a goal, also `og` and `pen` are used to indicate own goal and penalty.


Season | Date | Home Team | Home Score | Home Scorers | Away Team | Away Score | Away Scorers | Venue
----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- 
2001-02 | 6/11/02 | Blackburn Rovers|3|Andy Cole,53,g;Damien Duff,66,g;Andy Cole,81,g|Fulham|0|NaN|Ewood Park
2001-02 | 6/11/02 | Leicester City|2|Paul Dickov,60,g;Matthew Piper,71,g|Tottenham Hotspur|1|Teddy Sheringham,54,g|Filbert Street

I also used another dataset containing the geographical information of each team's venue to explore any possible relation between the hometown of a team and its stance.
**************************************************************************************************************************************


## Analysis 1 : Champions' performance
### Performance definition
I would like to start with exploring the performance of champions in each season. Considering that any win, draw, or loss provides three, one, and zero points for a team, one can find the points each team collected in each season using this raw dataset. The team with the highest points wins the cup, and if there is a tie, the team with a better goal difference will be announced as the winner. Next, I would check which champion has had a better perfomance in terms of the number of wins or the points collected. 
### Result
`data/seasons_champions.csv` shows the champion of each season, the number of wins, losses, and draws and the points they collected. 

Season | Champion | W | D | L | Pt 
----- | ----- | ----- | ----- | ----- | ----- 
 2001-2002 | Arsenal | 26 | 9 | 3 | 87
 2002-2003 | Manchester United | 25 | 8 | 5 | 83
 2003-2004 | Arsenal | 26 | 12 | 0 | 90
 2004-2005 | Chelsea | 29 | 8 | 1 | 95
 2005-2006 | Chelsea | 29 | 4 | 5 | 91
 2006-2007 | Manchester United | 28 | 5 | 5 | 89
 2007-2008 | Manchester United | 27 | 6 | 5 | 87
 2008-2009 | Manchester United | 28 | 6 | 4 | 90
 2009-2010 | Chelsea | 27 | 5 | 6 | 86
 2010-2011 | Manchester United | 26 | 9 | 3 | 87
 2011-2012 | Manchester City | 26 | 9 | 3 | 87
 2012-2013 | Manchester United | 26 | 9 | 3 | 87

The plot below shows the performance of each champion. As you can see, the champion of season 2003-04 (Arsenal) ended the season with no loss, which is an outstanding performance (W:26, D:12, L:0) even among all European leagues. However, the champion of season 2004-05 (Chelsea) got the highest point among other champions between 2001 to 2012 with 95 points out of 114 possible points.

![the number of wins draws and losses of each champion](https://cloud.githubusercontent.com/assets/12864506/21076110/45b3f7bc-bef1-11e6-96a6-9fe9dd3d2b94.png)

![points collected by each champion](https://cloud.githubusercontent.com/assets/12864506/20942569/dd445124-bbc9-11e6-88b6-768fff9e5770.png)

**************************************************************************************************************************************

## Analysis 2 : Individual performance
### Problem statement
I looked into the individual performance of each team by defining a function called `get_team_stat`. This function takes the name of one team, and generates tables and graphs showing the performance of the team between seasons 2001 to 2012. For instance, below you can see how *Manchester United* perfomed thorugh this timeline.

season| 	ranking	| points	| W | D | L | average number of goals per game
----- | ----- | ----- | ----- | ----- | ----- | ----- 
2001-2002	| 3	| 77	| 24 | 5 | 9 | 2.28947
2002-2003	| 1	| 83	| 25 | 8 | 5 | 1.94737
2003-2004	| 3	| 75 |	23 | 6 | 9 | 1.68421
2004-2005	| 3	| 77	| 22 | 11 | 5 | 1.52632
2005-2006	| 2	| 83	| 25 | 8 | 5 | 1.89474
2006-2007	| 1	| 89	| 28 | 5 | 5 | 2.18421
2007-2008 |	1	| 87	| 27 | 6 | 5 | 2.10526
2008-2009 |	1	| 90	| 28 | 6 | 4 | 1.78947
2009-2010	| 2	| 85	| 27 | 4 | 7 | 2.26316
2010-2011 |	1 |	80	| 23 | 11 | 4 | 2.05263
2011-2012	| 2	| 89	| 28 | 5 | 5 | 2.34211
2012-2013 |	1	| 89	| 28 | 5 | 5 | 2.26316

![average number of goals-game in each season - manchester united](https://cloud.githubusercontent.com/assets/12864506/21076164/63cb05aa-bef2-11e6-9a69-bfa086cfcc7a.png)

![ranking in each season - manchester united](https://cloud.githubusercontent.com/assets/12864506/21076163/63c9e116-bef2-11e6-9ddc-7742ba4ee965.png)


**************************************************************************************************************************************

## Analysis 3 : Goal Scorers
### Problem statement
I would like to see what players scored for their club from season 2001 to 2012. I extract the name of goal scorers for each match. Then, I make a dictioanry containing the teams, the goal scorers for each team, and the number of goals each player scored. The result of this analysis is stored in `data/teams_scorers.json`. I will show the top scorer of each club, also for each season.

### Result
A scheme of `data/teams_scorers.json` in which the scorers of each team and the number of goal any of them scored are scored, is shown below:

              {'Crystal Palace': {'Johnson': 20, 
              'Routledge': 1,  
              'Zaha': 1, ... }, 
              
              'Blackpool': {'Campbell': 12, 
              'Taylor-Fletcher': 5, 
              'Adam': 11, ... }, ... }

Among all scorers for a club, the one with the highest number of goals is shown in the plot below. 

![the number of goals of top scorers](https://cloud.githubusercontent.com/assets/12864506/21076206/caee6eec-bef3-11e6-95fe-f03542857eea.png)

**************************************************************************************************************************************


## Analysis 4 : The distribution of the scoring times
### Problem statement
For the beginning, I want to see what is the distribution of the scoring times. To do so, I split the columns `Home Scorer` and `Away Scorers`, generating a list for each match containing the minue of each goal scored. I exclude the own goals, since they cannot reflect the pattern of the scoring. So, any goal which has the `og` tag is removed from the analysis. I store these list in a dataframe which looks like below. The dataframe is stored in `data/matches_goal_min`.

Home Team | Home Score | Home Score Min | Away Team | Away Score | Away Score Min
----- | ----- | ----- | ----- | ----- | ----- 
 Blackburn Rovers|3|[53, 66, 81]|Fulham|0|[]
 Leicester City|2|[60, 71]|Tottenham Hotspur|1|[54]

To explore the scoring time distribution for each team, I define a function called `team_scoring_time_dist`. This function will show two distribution for games in which one team plays at home and as a guest.
Along with the scoring times, I want to see what is the distribution of the scoring the winning goal time. I define a winning goal as the last goal in a match which finishes with one goal difference. Thus, in matches with one goal difference, I compute the distribution of the last goal timing. 


## Results

![probability distribution of scoring time](https://cloud.githubusercontent.com/assets/12864506/21076246/adb35aa8-bef4-11e6-9c48-d146663865e3.png)

The plot above shows there is a very smooth increase in the chance of scoring when we get closer to the end of the match; however, there are to picks at the end of the first and second halfs. It's safe to say teams are scoring more goals at the end of each half, with a higher chance at the end of the second half. 
The plot below shows the same plot as above separately for `home team` and `away team`. As a rule of thumb among footballers, there is a higher chance of scoring when you play in your home venue.  However, the picks are occuring in the same times as before.

![probability distribution of goal timing home-away](https://cloud.githubusercontent.com/assets/12864506/21076266/3788e568-bef5-11e6-9849-0df4ba4a8124.png)


I use function `team_scoring_time_dist` to show the individual distribution for any team. For instance, below you can see the scoring time distribution for *Manchester United*, when they are palying at home and away. Confirming the claim that I mentioned before as higher chance to score when a team is playing at home, the plot below shows even at the individual level, this pattern stays put. However, *Manchester United* deviates from the mean field when it comes to the chance of scoring at the end of each half. While, considering all teams together, the probability of scoring at the end of second half is significantly higher than the the probability of scoring at the end of first half, *Manchester United* seems to have an equal chance in both times.

![probability distribution of scoring time home - away](https://cloud.githubusercontent.com/assets/12864506/21076314/25fc2070-bef6-11e6-871c-30e3e5417379.png)


Let's look at the distribution of the winning goal time.

![probability distribution of winning goal time](https://cloud.githubusercontent.com/assets/12864506/21076301/d0ba7b98-bef5-11e6-9552-6e6fdc19299a.png)

Interestingly, the distribution of the winning goal time is very similar to the scoring time. It can be concluded that if a team scores at the end of each half, there is a good chance for that goal to be the winning card. Regardless of two picks in the distribution, the slope of the distribution is still smooth, but higher than the slope of the distribution of scoring time. I would say this is pretty intuitive, since there is a smaller chance to keep the result one team got in the early stages of the match till the end. 

However, the question is whether this pattern changes when one team plays at home comparing with playing away. The plot below says not really. The way I interpret this is when a team plays at home, it has a higher chance of scoring - winning the game -; however, when is difference of scores is larger than one, the remaning goals does not change the final result. On the other hand, when an away team scores one goal more than the home team, then away team trys to keep the result as it is, rather than risking too much to score more. Because they already won three points, and the home team may score any time. To conclude, in terms of scoring winning goal time, teams behave similarly when they play at home or away.

![probability distribution of winning goal time home-away](https://cloud.githubusercontent.com/assets/12864506/21076308/09361b08-bef6-11e6-88d7-0a8303935302.png)


**************************************************************************************************************************************
## Analysis 5 : Geographical relation

<img width="636" alt="maps-uk-map-english-cities-and-towns-map" src="https://cloud.githubusercontent.com/assets/12864506/21080295/7aeb0bb8-bf79-11e6-8bd1-226fef241928.png">

### Probelm statement
Using the `Basemap` module, I would like to see how major football clubs (teams who played in the Premier League) are spreaded across the country and whether geography plays a role in teams' performance. Performance can be evaluated as the average ranking, the average number if wins/losses/draws, the number of away wins, and the average number of goals in each match.

### Results

The plot below shows the location of all teams who have played in the Premier league. Most of the teams are located in London, North West England, and where West Midlands and East Midlands meet.
![geo-spread](https://cloud.githubusercontent.com/assets/12864506/21080312/d0107808-bf79-11e6-8a6a-a5b52eabff03.png)
Checking the average ranking of teams, you can see teams in Manchester, London, and Liverpool are usually outperforming. The size of each green point is a logarithmic scale of the average ranking.
![avg_rank_geo](https://cloud.githubusercontent.com/assets/12864506/21080334/3a2c31e6-bf7a-11e6-9c23-897c5f1fdbdb.png)
**************************************************************************************************************************************

## Cross-checking with an API

In the table of Analysis 1 (shown below), at first my putput showed that *Manchester United* has won the league which is not true. So I realized I just checked the points of each team to determine the champion. However, if there is a tie between two teams in terms of collected points, the team with better goal difference will have the higher rank. So I re-run my code, considering the goal difference as well.

Season | Champion | W | D | L | Pt 
----- | ----- | ----- | ----- | ----- | ----- 
 2001-2002 | Arsenal | 26 | 9 | 3 | 87
 2002-2003 | Manchester United | 25 | 8 | 5 | 83
 2003-2004 | Arsenal | 26 | 12 | 0 | 90
 2004-2005 | Chelsea | 29 | 8 | 1 | 95
 2005-2006 | Chelsea | 29 | 4 | 5 | 91
 2006-2007 | Manchester United | 28 | 5 | 5 | 89
 2007-2008 | Manchester United | 27 | 6 | 5 | 87
 2008-2009 | Manchester United | 28 | 6 | 4 | 90
 2009-2010 | Chelsea | 27 | 5 | 6 | 86
 2010-2011 | Manchester United | 26 | 9 | 3 | 87
 2011-2012 | Manchester City | 26 | 9 | 3 | 87
 2012-2013 | Manchester United | 26 | 9 | 3 | 87
 
To make sure my other results are correct, instead of checking it online, I used an REST API (called football-data) to validate my results. I checked the table ranking, points collected, and number of wins/draws/losses. Fortunately, my results are matching. This API gives a very messi output, and cleaning the result take so much time, so I did not store the output in a proper format. For example one of the issues with the output of this API is they call teams differently! For instance, they call *Leicester City*, *Foxes* which is their nickname. In another example, instead of *Tottenham Hotspur*, they call them *Spurs*.
 below, you can see a sample of my code:
 
 
     connection = httplib.HTTPConnection('api.football-data.org')
     headers = { 'X-Auth-Token': 'f7836f842fe14d9487b41d091782ffe2', 'X-Response-Control': 'minified' }
     connection.request('GET', '/v1/competitions/398/leagueTable/?season/2015',None, headers )
     response = json.loads(connection.getresponse().read().decode())
     print (response)
   
     {'standing': 
     [{'playedGames': 38, 'rank': 1, 'teamId': 338, 'points': 81, 'goals': 68, 'team': 'Foxes', 'crestURI':       'http://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png', 'goalDifference': 32, 'goalsAgainst': 36}, 
     {'playedGames': 38, 'rank': 2, 'teamId': 57, 'points': 71, 'goals': 65, 'team': 'Arsenal', 'crestURI': 'http://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg', 'goalDifference': 29, 'goalsAgainst': 36}, 
     {'playedGames': 38, 'rank': 3, 'teamId': 73, 'points': 70, 'goals': 69, 'team': 'Spurs', 'crestURI': 'http://upload.wikimedia.org/wikipedia/de/b/b4/Tottenham_Hotspur.svg', 'goalDifference': 34, 'goalsAgainst': 35}, 
     .... }
