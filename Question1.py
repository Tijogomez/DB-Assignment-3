import sqlite3
con = sqlite3.connect('database.sqlite')
cur = con.cursor()

print("Names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals")
print(con.execute("Select HomeTeam,AwayTeam from Matches where Season ='2015' and FTHG ='5'").fetchall())

print("Details of the matches where Arsenal is the Home Team and  Full Time Result is Away Win")
print(con.execute("Select * from Matches where HomeTeam = 'Arsenal' and FTR = 'A'").fetchall())

print("Matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals > 2")
print(con.execute("Select HomeTeam,AwayTeam,FTR from Matches where Season BETWEEN 2012 AND 2015 and AwayTeam = 'Bayern Munich' and FTHG > 2 ").fetchall())

print("Matches where the Home Team name begins with A and Away Team name begins with M")
print(con.execute("Select HomeTeam,AwayTeam,FTR from Matches where HomeTeam LIKE 'A%' and AwayTeam LIKE 'M%'").fetchall())

con.close()
