import random

friends_number = int(input("Enter the number of friends joining (including you):"))
if friends_number < 1:
    print("No one is joining for the party")
else:
    friends = dict()
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(friends_number):
        friends[input()] = 0

    total = float(input("Enter the total bill value:"))

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    chosen_one = None

    if input() == "Yes":
        chosen_one = random.choice(list(friends))
        print(f"{chosen_one} is the lucky one!")
        friends_number -= 1
    else:
        print("No one is going to be lucky")

    share = round(total / friends_number, 2)

    for name in friends.keys():
        friends[name] = share

    if chosen_one:
        friends[chosen_one] = 0

    print(friends)
