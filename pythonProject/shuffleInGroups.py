import random

start_roll = int(input("Enter the start roll: "))
end_roll = int(input("Enter the end roll: "))
rolls = list(range(start_roll, end_roll+1))
group_size = int(input("Enter numbers of member in a group: "))


dec= input("Is there anyone absent? (y/n): ").lower()

if dec == 'y':
    while True:
        ab_roll = int(input("Enter absent roll (press 0 to quit): "))
        if ab_roll == 0:
            break
        elif ab_roll in rolls:
            rolls.remove(ab_roll)
        else:
            print("Roll not found in the list.")

i = 1

while len(rolls) > 0:
    group = []
    for _ in range(min(group_size, len(rolls))):
        rand = random.randint(0,  len(rolls)-1)
        group.append(rolls.pop(rand))

    print(f"Group-{i}: {group}")
    i += 1