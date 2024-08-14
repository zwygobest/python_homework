def go_to_lobby(gold_coins: int) -> None:
    """ The start of the adventure """
    print_gold_amount(gold_coins)
    print("You are in the lobby of the dungeon. What do you do?")
    print("1. Examine the lobby.")
    print("2. Go to the throne hall.")
    print("3. Leave.")
    option = int(input())
    if option == 1:
        examine_lobby(gold_coins)
    elif option == 2:
        go_to_throne_hall(gold_coins)
    else:
        leave(gold_coins)


def examine_lobby(gold_coins: int) -> None:
    """ The user examines the lobby """
    print_gold_amount(gold_coins)
    rob_amount = 10
    print("A band of goblins rob " + str(rob_amount) + " gold from you.")
    go_to_lobby(gold_coins - rob_amount)


def leave(gold_coins: int) -> None:
    """ The end of the adventure
        unless the user owes money
     """
    if gold_coins < 0:
        go_to_kitchen(gold_coins)
    else:
        print_gold_amount(gold_coins)
        print("You leave the dungeon.")


def go_to_throne_hall(gold_coins: int) -> None:
    """ The middle of the adventure """
    print_gold_amount(gold_coins)
    print("You are in the throne hall. What do you do?")
    print("1. Examine the throne hall.")
    print("2. Go back to the lobby.")
    option = int(input())
    if option == 1:
        examine_throne_hall(gold_coins)
    else:
        go_to_lobby(gold_coins)


def examine_throne_hall(gold_coins: int) -> None:
    """ The user examines the throne hall """
    print_gold_amount(gold_coins)
    rob_amount = 40
    print("You disturb the dungeon keeper who makes you pay " + str(rob_amount) + " gold.")
    go_to_throne_hall(gold_coins - rob_amount)


def print_gold_amount(gold_coins: int) -> None:
    """ Prints to the user their current amount of gold """
    print("You have " + str(gold_coins) + " gold.")


def go_to_kitchen(gold_coins: int) -> None:
    """ The user can wash dishes for few golds or leave """
    if gold_coins > 0:
        go_to_lobby(gold_coins)
    print_gold_amount(gold_coins)
    wash_dishes_amount = 1
    leave_early_amount = 10
    print("You are in the kitchen. What do you do?")
    print("0. Go back to the lobby.")
    print("Or enter ammount of gold to earn by washing dishes.")
    option = int(input())

    if option == 0:
        go_to_lobby(gold_coins - leave_early_amount)
    else:
        go_to_kitchen(gold_coins + wash_dishes_amount)


go_to_lobby(50)