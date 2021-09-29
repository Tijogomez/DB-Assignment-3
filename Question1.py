import sqlite3
con = sqlite3.connect('database.sqlite')
cur = con.cursor()
print(con.execute("Select HomeTeam,AwayTeam from Matches where Season ='2015' and FTHG ='5'").fetchall())

print(con.execute("Select * from Matches where HomeTeam = 'Arsenal' and FTR = 'A'").fetchall())

print(con.execute("Select HomeTeam,AwayTeam,FTR from Matches where Season BETWEEN 2012 AND 2015 and AwayTeam = 'Bayern Munich' and FTHG > 2 ").fetchall())

print(con.execute("Select HomeTeam,AwayTeam,FTR from Matches where HomeTeam LIKE 'A%' and AwayTeam LIKE 'M%'").fetchall())
con.close()
