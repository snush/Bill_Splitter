import random

friends = dict()
number_of_people = int(input("Enter the number of friends joining (including you):\n"))
if number_of_people > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for i in range(number_of_people)}
    bill = int(input("Enter the total bill value:\n"))
    feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if feature == "Yes":
        lucky_man = random.choice([name for name in friends.keys()])
        print(f"{lucky_man} is the lucky one!")
        split_value = round(bill / (number_of_people - 1), 2)
        friends = {name: split_value if name != lucky_man else 0 for name in friends.keys()}
    else:
        print("No one is going to be lucky")
        split_value = round(bill / number_of_people, 2)
        friends = {name: split_value for name in friends.keys()}
    print(friends)
else:
    print("No one is joining for the party")
