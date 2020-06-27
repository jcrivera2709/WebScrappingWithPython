names = ['Jose', 'Carlos', 'Rivera', 'Santiago']

# Both print the same thing but the list comprehension allows you to go from 4 lines of code to 1 line.
l = []
for people in names:
    l.append(people)
print(l)
print([people for people in names])

# Adding information to the already made list with list comprehension
anotherL = []
for people in names:
    anotherL.append(people + ' is part of my name.')
print(anotherL)
print([people + ' is part of my name.' for people in names])

# Small example with list comprehension and manipulation in the list comprehension
movies_and_ratings = {"Shrek": 3, "Dark Knight": 8, "Avatar": 10, "Star Wars": 10}
movieL = []
for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        movieL.append(movie)
print(movieL)
print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])
