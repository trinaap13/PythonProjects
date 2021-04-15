import sys, random

print("Welcome to The Name Picker!\n")
print("A new name fit for royalty:\n\n")

first = ('Baby Oil', 'Bad News', 'Lil Debil', 'Worms',
         'Figgs', 'Cornbread', 'Crabmeat', 'Slaps',
         'Jimbo', 'Buttocks')
last = ('Williams', 'Jefferson', 'Stevens', 'Turnipseed'
        'Woolysocks', 'Putney')

while True: # keep running till I tell you to stop
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter. Else press n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
