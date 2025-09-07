enemies = "Skeleton"
def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")


def increase_enemies():
    enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies + 1
    enemies = increase_enemies()
