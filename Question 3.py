import sqlite3
con = sqlite3.connect('database.sqlite')
cur = con.cursor()

print("Name of HomeTeam,Number of home goals,Number of away goals")
print(con.execute("Select HomeTeam,FTHG,FTAG from Matches where Season = '2010' and HomeTeam = 'Aachen' ORDER BY FTHG DESC").fetchall())

print("Total number of home games each team won during the 2016 season.")
print(con.execute("Select HomeTeam,COUNT(FTR) from Matches where FTR = 'H' and Season = '2016' GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC").fetchall())

print("First ten rows from the Unique_Teams table")
print(con.execute("Select * from Unique_Teams LIMIT 10").fetchall())

print("Match ID and Unique Team_ID with the corresponding Team Name.")
print("By using WHERE statemens")
print(con.execute("Select Teams_in_Matches.Match_id,Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName from Teams_in_Matches,Unique_Teams where Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID ").fetchall())

print("By using JOIN statement")
print(con.execute("Select Teams_in_Matches.Match_id,Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName from Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID ").fetchall())

print("Query that joins together the Unique_Teams data table and the Teams table")
print(con.execute("Select * from Unique_Teams JOIN Teams LIMIT 10").fetchall())

print("Query that shows the Unique_Team_ID and TeamName from Unique_Teams and AvgAgeHome, Season and ForeignPlayersHome from Teams, return the first five rows")
print(con.execute("Select Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome from Unique_Teams JOIN Teams ON Unique_Teams.TeamName = Teams.TeamName LIMIT 5").fetchall())

print("Query that shows the highest MatchID for each team that ends in a “y” or a “r” Display the Unique_Team_ID Teams_in_Matches and the TeamName from Unique_Teams")
print(con.execute("Select MAX(Match_id),Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName from Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID where TeamName LIKE '%y' OR TeamName LIKE '%r' GROUP BY Teams_in_Matches.Unique_Team_ID, TeamName").fetchall())

con.close()
