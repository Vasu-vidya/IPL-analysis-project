import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import missingno as msno
import numpy as np

# Loading the data

data = pd.read_csv("file:///C:/Users/Vasu%20Prasad/Downloads/archive(1)/Dataset/2023/batting_summary_2023.csv")
data

data.drop("Unnamed: 0",axis = 1,inplace = True) #Droping the unwanted column

data.head()

data.describe()

data.info()

data.dtypes

data.isnull().sum().reset_index().rename(columns = {0:"count"}) #cheaking the null values

msno.matrix(data) # Displaying the null values

# Locatins of the null values
data[data["Batsman Names"].isna() | data["Out/Not Out"].isna()| data["Balls Played"].isna()| data["Runs Scored"].isna() | data["Fours"].isna() | data["Sixes"].isna() | data["Strike Rate"].isna() ]

# Updating the null values

data.at[17,"Out/Not Out"]

data.at[17,"Out/Not Out"] = "b Chakaravarthy"

data.at[33,"Runs Scored"]

data.at[33,"Runs Scored"] = 73

data.at[68,"Balls Played"]

data.at[68,"Balls Played"] = 10

data.at[82,"Batsman Names"]

data.at[82,"Batsman Names"] = "Conway"

data.at[102,"Batsman Names"]

data.at[102,"Batsman Names"] = "Sarfaraz Khan"

data.at[169,"Batsman Names"]

data.at[169,"Batsman Names"] = "Samsom(c & WK)"

data.at[215,"Out/Not Out"]

data.at[215,"Out/Not Out"] = "not out"

data.at[263,"Batsman Names"]

data.at[263,"Batsman Names"] = "Padikkal"

data.at[335,"Batsman Names"]

data.at[335,"Batsman Names"] = "N Jagadeesan"

data.at[319,"Sixes"]

data.at[319,"Sixes"] = 2

data.at[350,"Sixes"]

data.at[350,"Sixes"] = 1

data.at[367,"Runs Scored"]

data.at[367,"Runs Scored"] = 3

data.at[403,"Strike Rate"] 

data.at[403,"Strike Rate"] = 125.53

data.at[440,"Runs Scored"]

data.at[440,"Runs Scored"] = 34

data.at[472,"Sixes"]

data.at[472,"Sixes"] = 1

data.at[488,"Runs Scored"]

data.at[488,"Runs Scored"] = 0

data.at[523,"Batsman Names"]

data.at[523,"Batsman Names"] = "Warner(c)"

data.at[542,"Strike Rate"]

data.at[542,"Strike Rate"] = 57.14

data.at[576,"Runs Scored"]

data.at[576,"Runs Scored"] = 12

data.at[639,"Balls Played"]

data.at[639,"Balls Played"] = 19

data.at[676,"Fours"]

data.at[676,"Fours"] = 0

data.at[693,"Fours"]

data.at[693,"Fours"] = 1

data.at[765,"Out/Not Out"]

data.at[765,"Out/Not Out"] = "c Axar b Mitchell Marsh"

data.at[781,"Sixes"]

data.at[781,"Sixes"] = 0

data.at[831,"Fours"]

data.at[831,"Fours"] = 1

data.at[863,"Sixes"]

data.at[863,"Sixes"] = 1

data.at[944,"Balls Played"] 

data.at[944,"Balls Played"] = 3

data.at[978,"Strike Rate"]

data.at[978,"Strike Rate"] = 148.39

data.at[1003,"Fours"]

data.at[1003,"Fours"] = 0

data.at[1020,"Balls Played"]

data.at[1020,"Balls Played"] = 9

data.at[1066,"Runs Scored"]

data.at[1066,"Runs Scored"] = 11

data.at[1082,"Strike Rate"]

data.at[1082,"Strike Rate"] = 137.5

data.isnull().sum().reset_index().rename(columns = {0:"count"})

msno.matrix(data) 

data[data["Batsman Names"].isna()] #null values

# Droping the null values
data.dropna(inplace = True)
data

data.reset_index(drop = True,inplace = True)

data

# Cheaking for data types
data.dtypes

data["Balls Played"] = data["Balls Played"].astype(int)
data["Runs Scored"] = data["Runs Scored"].astype(int)
data["Fours"] = data["Fours"].astype(int)
data["Sixes"] = data["Sixes"].astype(int)

data.dtypes

new_data = data.copy()

team_playes = data[["Team Playing","Batsman Names"]]
team_playes.groupby(by = ["Team Playing","Batsman Names"]).count()

pd.set_option('display.max.rows',248 )

# Replacing the names of the playes
#Chennai Super Kings Innings
new_data.replace('Conway','Devon Conway',inplace = True)
new_data.replace('Dhoni (c & wk)','MS Dhoni (c & wk)',inplace = True)
new_data.replace('Moeen','Moeen Ali',inplace = True)
new_data.replace('Rayudu','Ambati Rayudu',inplace = True)



# Delhi Capitals Innings
new_data.replace('Axar','Axar Patel',inplace = True)
new_data.replace('Warner (c)','David Warner (c)',inplace = True)
new_data.replace('Warner(c)','David Warner (c)',inplace = True)
new_data.replace('Sarfaraz Khan','Sarfaraz Khan (wk)',inplace = True)
new_data.replace('Nortje','Anrich Nortje',inplace = True)
new_data.replace('Rossouw','Rilee Rossouw',inplace = True)
new_data.replace('Salt (wk)','Philip Salt (wk)',inplace = True)

# Gujarat Titans Innings
new_data.replace('Miller','David Miller',inplace = True)
new_data.replace('W Saha (wk)','Wriddhiman Saha (wk)',inplace = True)
new_data.replace('Shami','Mohammed Shami',inplace = True)
new_data.replace('Shanaka','Dasun Shanaka',inplace = True)

# Kolkata Knight Riders Innings
new_data.replace('Russell','Andre Russell',inplace = True)
new_data.replace('Chakaravarthy','Varun Chakaravarthy',inplace = True)
new_data.replace('Wiese','David Wiese',inplace = True)
new_data.replace('Gurbaz (wk)','Rahmanullah Gurbaz (wk)',inplace = True)
new_data.replace('Mandeep','Mandeep Singh',inplace = True)
new_data.replace('N Jagadeesan','N Jagadeesan (wk)',inplace = True)
new_data.replace('Narine','Sunil Narine',inplace = True)
new_data.replace('Thakur','Shardul Thakur',inplace = True)
new_data.replace('Umesh','Umesh Yadav',inplace = True)

# Lucknow Super Giants Innings
new_data.replace('Krunal Pandya','Krunal Pandya (c)',inplace = True)
new_data.replace('Nicholas Pooran','Nicholas Pooran (wk)',inplace = True)
new_data.replace('Pooran','Nicholas Pooran (wk)',inplace = True)
new_data.replace('Pooran (wk)','Nicholas Pooran (wk)',inplace = True)
new_data.replace('de Kock (wk)','Quinton de Kock (wk)',inplace = True)
new_data.replace('Rahul (c)','KL Rahul (c)',inplace = True)
new_data.replace('Stoinis','Marcus Stoinis',inplace = True)
new_data.replace('K Gowtham','Krishnappa Gowtham',inplace = True)
new_data.replace('K Mayers','Kyle Mayers',inplace = True)
new_data.replace('K Mayers','Kyle Mayers',inplace = True)

# Mumbai Indians Innings
new_data.replace('Green','Cameron Green',inplace = True)
new_data.replace('Chawla','Piyush Chawla',inplace = True)
new_data.replace('Rohit (c)','Rohit Sharma (c)',inplace = True)
new_data.replace('Rohit Sharma','Rohit Sharma (c)',inplace = True)
new_data.replace('Suryakumar Yadav (c)','Suryakumar Yadav',inplace = True)

# Punjab Kings Innings
new_data.replace('Harpreet Singh','Harpreet Singh Bhatia',inplace = True)
new_data.replace('Livingstone','Liam Livingstone',inplace = True)
new_data.replace('Prabhsimran','Prabhsimran Singh',inplace = True)
new_data.replace('Sam Curran (c)','Sam Curran',inplace = True)
new_data.replace('Dhawan (c)','Shikhar Dhawan (c)',inplace = True)
new_data.replace('Raza','Sikandar Raza',inplace = True)

# Rajasthan Royals Innings
new_data.replace('Holder','Jason Holder',inplace = True)
new_data.replace('Padikkal','Devdutt Padikkal',inplace = True)
new_data.replace('Ashwin','Ravichandran Ashwin',inplace = True)
new_data.replace('Samsom(c & WK)','Sanju Samson (c & wk)',inplace = True)
new_data.replace('Samson (c & wk)','Sanju Samson (c & wk)',inplace = True)
new_data.replace('Hetmyer','Shimron Hetmyer',inplace = True)
new_data.replace('Boult','Trent Boult',inplace = True)
new_data.replace('Zampa','Adam Zampa',inplace = True)

# Royal Challengers Bangalore Innings
new_data.replace('Anuj Rawat','Anuj Rawat (wk)',inplace = True)
new_data.replace('Karthik','Dinesh Karthik (wk)',inplace = True)
new_data.replace('Karthik (wk)','Dinesh Karthik (wk)',inplace = True)
new_data.replace('Kohli','Virat Kohli',inplace = True)
new_data.replace('Kohli (c)','Virat Kohli',inplace = True)
new_data.replace('Lomror','Mahipal Lomror',inplace = True)
new_data.replace('M Bracewell','Michael Bracewell',inplace = True)
new_data.replace('Prabhudessai','Suyash Prabhudessai',inplace = True)
new_data.replace('du Plessis','Faf du Plessis (c)',inplace = True)
new_data.replace('du Plessis','Faf du Plessis (c)',inplace = True)
new_data.replace('Willey','David Willey',inplace = True)
new_data.replace('Maxwell','Glenn Maxwell',inplace = True)
new_data.replace('Maxwell','Glenn Maxwell',inplace = True)


# Sunrisers Hyderabad Innings
new_data.replace('Bhuvneshwar Kumar (c)','Bhuvneshwar Kumar',inplace = True)
new_data.replace('Bhuvneshwar','Bhuvneshwar Kumar',inplace = True)
new_data.replace('Glenn Phillips','Glenn Phillips (wk)',inplace = True)
new_data.replace('Anmolpreet Singh (wk)','Anmolpreet Singh',inplace = True)
new_data.replace('Klaasen (wk)','Heinrich Klaasen',inplace = True)
new_data.replace('Markram (c)','Aiden Markram (c)',inplace = True)
new_data.replace('Tripathi','Rahul Tripathi',inplace = True)

new_data

new_team_players = new_data[["Team Playing","Batsman Names"]]
new_team_players.groupby(by = ["Team Playing","Batsman Names"]).count()

pd.set_option('display.max.rows',248 )

# Top Fours

Top_Fours = new_data[["Batsman Names","Fours"]]
Top_Fours

Top_Fours_Byplayers = Top_Fours.groupby("Batsman Names").sum()
Top_Fours_Byplayers

Fours = Top_Fours_Byplayers.sort_values("Fours",ascending = False).reset_index().head(10)
Fours

# Top Six

Top_six = new_data[["Batsman Names","Sixes"]]
six = Top_six.groupby("Batsman Names").sum().reset_index()

six

Top_sixes = six.sort_values("Sixes",ascending = False).head(10).reset_index()
Top_sixes

# Total Teams

new_data[["Team Playing"]].groupby(by =["Team Playing"] ).count().reset_index()

# Highest Team Scores

Highest_Team_Scores = new_data[["Team Playing","Total Runs"]].groupby(by = ["Team Playing"]).max().sort_values(by = ["Total Runs"],ascending = False).reset_index()
Highest_Team_Scores

# Runs_Scored_ByPlayers

Runs_Scored = new_data[["Batsman Names","Runs Scored"]].groupby(by = ["Batsman Names"]).sum().sort_values("Runs Scored",ascending = False).reset_index().head(10)
Runs_Scored







# Graphical representation

plt.figure(figsize = (6,4))
sns.set_style("darkgrid")
ax=sns.barplot(x =Fours['Batsman Names'],y = Fours['Fours'],palette ="rocket",errorbar=('ci', False))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.title("Top Four Hits By Players")
plt.show()


plt.figure(figsize = (6,4))
sns.barplot(x = Top_sixes["Sixes"],y = Top_sixes["Batsman Names"],palette = "mako",errorbar=('ci', False))
plt.title("Top Six By Players")
plt.show()

plt.figure(figsize = (6,4))
sns.set_style("darkgrid")
#sns.set(rc={'axes.facecolor':'lightblue', 'figure.facecolor':'lightgreen'})
sns.scatterplot(x = Highest_Team_Scores['Total Runs'],y=Highest_Team_Scores['Team Playing'],marker = "*",s = 200)
plt.title("Teams With High SCore")
plt.show()

ab=sns.lineplot(x = Runs_Scored['Runs Scored'],y = Runs_Scored["Batsman Names"],marker = "*")
plt.title("Top Score by Players")
plt.show()

# Bowling Data

B_data=pd.read_csv("file:///C:/Users/Vasu%20Prasad/Downloads/archive(1)/Dataset/2023/bowling_summary_2023.csv")

B_data.head()

B_data.describe()

B_data.isnull().sum().reset_index().rename(columns = {0:"count"})

B_data[B_data["Bowler Name"].isna() | B_data["Overs"].isna() | B_data["Maidens"].isna() | B_data["Runs"].isna() | B_data["Wickets"].isna() | B_data["Wides"].isna()]

msno.matrix(B_data)

pd.set_option('display.max.rows',761)

B_data.at[301,"Bowler Name"]

B_data.at[301,"Bowler Name"] = "Akash Singh"

B_data.at[467,"Bowler Name"]

B_data.at[467,"Bowler Name"] = "Green"

B_data.at[542,"Bowler Name"]

B_data.at[542,"Bowler Name"] = "Vaibhav Arora"

B_data.at[581,"Bowler Name"]

B_data.at[581,"Bowler Name"] = "Shami"

B_data.at[631,"Bowler Name"]

B_data.at[631,"Bowler Name"] = "Behrendorff"

B_data.at[61,"Overs"]

B_data.at[61,"Overs"] = 2

B_data.at[288,"Overs"]

B_data.at[288,"Overs"] = 4

B_data.at[530,"Overs"]

B_data.at[530,"Overs"] = 4

B_data.at[417,"Maidens"]

B_data.at[417,"Maidens"] = 0

B_data.at[689,"Maidens"]

B_data.at[689,"Maidens"] = 0

B_data.at[379,"Runs"] 

B_data.at[379,"Runs"] = 25

B_data.at[727,"Wickets"] 

B_data.at[727,"Wickets"] = 0

B_data.at[183,"Wides"] 

B_data.at[183,"Wides"] = 0

B_data.at[750,"Wides"] 

B_data.at[750,"Wides"] = 0

B_data

B_data.isnull().sum().reset_index().rename(columns = {0:"count"})

msno.matrix(B_data)

B_data.dtypes

B_data[["Overs"]] = B_data[["Overs"]].astype(int) 
B_data[["Maidens"]] = B_data[["Maidens"]].astype(int) 
B_data[["Economies"]] = B_data[["Economies"]].astype(int) 
B_data[["Wides"]] = B_data[["Wides"]].astype(int) 
B_data[["Runs"]] = B_data[["Runs"]].astype(int) 
B_data[["Wickets"]] = B_data[["Wickets"]].astype(int) 

B_data.dtypes

B_data.shape

B_data.drop("Unnamed: 0",axis = 1,inplace = True)

B_data

B_data.columns

Team_Bowlers = B_data[["Team Bowling","Bowler Name"]]
Team_Bowlers.groupby(by = ["Team Bowling","Bowler Name"]).count() 

#updating the team players names
B_data["Bowler Name"].replace({'D Chahar':'Deepak Chahar','Moeen':'Moeen Ali',
                               'M Theekshana':'Maheesh Theekshana',
                               'RS Hangargekar':'Rajvardhan Hangargekar',
                               'Santner':'Mitchell Santner',
                               'Axar':'Axar Patel',
                               'Ishant':'Ishant Sharma',
                               'Nortje':'Anrich Nortje',
                               'Rashid Khan':'Rashid Khan (c)',
                               'Shami':'Mohammed Shami',
                               'Russell':'Andre Russell',
                               'Narine':'Sunil Narine',
                               'Southee':'Tim Southee',
                               'Umesh':'Umesh Yadav',
                               'Chakaravarthy':'Varun Chakaravarthy',
                               'Thakur':'Shardul Thakur',
                               'Krunal Pandya':'Krunal Pandya (c)',
                               'K Mayers':'Kyle Mayers',
                               'Green':'Cameron Green',
                               'Chawla':'Piyush Chawla',
                               'Livingstone':'Liam Livingstone',
                               'Sam Curran':'Sam Curran (c)',
                               'Raza':'Sikandar Raza',
                               'Rabada':'Kagiso Rabada',
                               'Holder':'Jason Holder',
                               'Jason Holder':'Ravichandran Ashwin',
                               'Zampa':'Adam Zampa',
                               'Chahal':'Yuzvendra Chahal',
                               'Boult':'Trent Boult',
                               'Maxwell':'Glenn Maxwell',
                               'Siraj':'Mohammed Siraj',
                               'Parnell':'Wayne Parnell',
                               'Willey':'David Willey',
                               'W Hasaranga':'Wanindu Hasaranga',
                               'Bhuvneshwar':'Bhuvneshwar Kumar',
                               'Markram (c)':'Aiden Markram (c)',
                               'Bhuvneshwar (c)':'Bhuvneshwar Kumar',
                               'Markande':'Mayank Markande'
                               },inplace=True)

New_Team_Bowlers = B_data[["Team Bowling","Bowler Name"]]
New_Team_Bowlers.groupby(by = ["Team Bowling","Bowler Name"]).count() 


# Top Wickets

# Top Wickets
W_data = B_data[["Bowler Name","Wickets"]].groupby(by = ["Bowler Name"]).sum().reset_index()
W_data

Top_Wickets = W_data.sort_values("Wickets",ascending = False)
Top_Wickets

# Top Over

# Top Over
Over  = B_data[["Bowler Name","Overs"]].groupby(by =["Bowler Name"]).sum().reset_index()
Over

Overs_1 = Over.sort_values("Overs",ascending = False)
Overs_1

# Wides

Wides = B_data[["Bowler Name","Wides"]].groupby(by = ["Bowler Name"]).sum().reset_index()
Wides

Most_Wides = Wides.sort_values("Wides",ascending = False).head(10)
Most_Wides

# graphical representation

#Top Wickets
#x = Top_Wickets['Bowler Name']
#y = Top_Wickets['Wickets']
plt.figure(figsize = (25,17))
ax = sns.barplot(x = Top_Wickets['Bowler Name'],y = Top_Wickets['Wickets'],data = Top_Wickets,palette = "magma")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.title("Top Wickets")
plt.show()

#Top Over
#x = Overs_1['Overs']
#y = Overs_1['Bowler Name']

plt.figure(figsize = (17,23))
sns.barplot(x = Overs_1['Overs'],y = Overs_1['Bowler Name'],data = Overs_1,palette = "viridis",errorbar=('ci', False))
plt.title("Top Overs")
plt.show()

#Most_wides
#x = Most_Wides['Bowler Name']
#y = Most_Wides['Wides']
plt.figure(figsize = (10,8))

ay = sns.stripplot(x = Most_Wides['Bowler Name'],y = Most_Wides['Wides'],data = Most_Wides,marker = "*",s = 20)
ay.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.title("Most_wides")
plt.show()





