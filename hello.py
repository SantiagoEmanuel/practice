# Define a list of names.
names = ["Harry", "Ron", "Hermione", "Ginny"]

print(names)

names.append("Draco")

print(names)

# Create en empty set

s = set()

# Add elements to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)

print(s)

#Intento de algo.

# Number of the players
n = int(input("Players: "))

# List the players
playerlist = set()

# input for the names of players
for i in range(n):
    players = input(f"Name for player {i}: ")
    i +=1
    playerlist.add(players)

# print list
print("These are the players for now")
print(playerlist)

# This experiment went well.