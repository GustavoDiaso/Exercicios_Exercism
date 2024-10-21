def return_given_money(given_money):
    CHANGE_COINS = [100, 25, 10, 5, 1]
    change = []

    if given_money >= 1:

        while given_money != 0:
            for coin_type in CHANGE_COINS:
                while given_money - coin_type >= 0:
                    given_money = given_money - coin_type
                    change.append(coin_type)

        return change

    else:
        raise ValueError("can't make target with given coins")


print(return_given_money(20))
