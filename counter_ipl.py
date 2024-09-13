Nandit = []
Rishab = []

Nandit_Money = 0
Rishab_Money = 0

wallet1 = 0
wallet2 = 0
wallet3 = 0
wallet4 = 0
wallet5 = 0
wallet6 = 0

Teams = ["RCB", "CSK", "DC", "GT", "KKR", "LSG", "MI", "PK", "RR", "SRH"]

Stage = ["League Stage", "Semi-Finals", "Final"]

while True:
    element1 = input("Enter the team for Nandit : ")
    if element1 not in Teams:
        print("Invalid team name. Please enter a valid team name.")
        continue
    Nandit.append(element1)

    element2 = input("Enter the team for Rishab: ")
    if element2 not in Teams:
        print("Invalid team name. Please enter a valid team name.")
        continue
    Rishab.append(element2)

    print('\n')

    Winner = input("Who is the winner : ")

    print("Nandit's Team : ", element1)
    print("Rishab's Team : ", element2) 

    print('\n')

    stages = input("Enter the stage of the tournament :")

    if stages not in Stage:
        print("Invalid Stage. Please enter a valid stage.")
        continue

    if stages == "League Stage":
        if Winner == element1:
            Nandit_Money += 100
            print("Rishab Ows Nandit : ", Nandit_Money)
            wallet1 = Nandit_Money

        else:
            Rishab_Money += 100
            print("Nandit ows Rishab: ", Rishab_Money)
            wallet2 = Rishab_Money

    elif stages == "Semi-Finals":
        if Winner == element1:
            Nandit_Money += 500
            print("Rishab Ows Nandit : ", Nandit_Money)
            wallet3 = wallet1 + Nandit_Money

        else:
            Rishab_Money += 500
            print("Nandit ows Rishab: ", Rishab_Money)
            wallet4 = wallet2 + Rishab_Money 

    elif stages == "Final":
        if Winner == element1:
            Nandit_Money += 1000
            print("Rishab Ows Nandit : ", Nandit_Money)
            wallet5 = wallet3 + Nandit_Money

        else:
            Rishab_Money += 1000
            print("Nandit ows Rishab: ", Rishab_Money)
            wallet6 = wallet4 + Rishab_Money 

    print('\n')
    print("Current Status: ")
    print("Nandit's Money: ", Nandit_Money)
    print("Rishab's Money: ", Rishab_Money)
    print('\n')

    restart = input("Do you want to start a new iteration? (Y/N): ")
    if restart.lower() == 'n':
        break

