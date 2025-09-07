enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

player_strength = 10 #Global scope
def drink_potion():
    potion_strength = 2 #Local space
    print(potion_strength)
    print(player_strength)
drink_potion()
print(player_strength)
#In function there is block space but in any other statement and loops it is not count as separate local scope.