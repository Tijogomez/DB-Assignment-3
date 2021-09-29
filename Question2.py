import sqlite3
con = sqlite3.connect('database.sqlite')
cur = con.cursor()

print("Number of rows in the Teams table")
print(con.execute("Select Count(*) from Teams").fetchall())

print("Unique values in the Season coloumn")
print(con.execute("Select DISTINCT Season from Teams").fetchall())

print("Largest Stadium Capacity")
print(con.execute("Select MAX(StadiumCapacity) from Teams ").fetchall())
print("Smallest Stadium Capacity")
print(con.execute("Select MIN(StadiumCapacity) from Teams").fetchall())

print("Sum of squad players in 2014")
print(con.execute("Select SUM(KaderHome) from Teams where Season ='2014' ").fetchall())

print("Average home goals scored by Man United")
print(con.execute("Select ROUND(AVG(FTHG), 2) FROM Matches where HomeTeam = 'Man United'").fetchall())

con.close()

