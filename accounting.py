def did_customer_pay_correct_amount(num_of_melons, amount_paid):
    """
    Determines if customer paid the amount of money actually owed to ubermelon
    :param num_of_melons: int
    :param amount_paid: float
    :return: boolean
    """
    expected_cost = determine_payment_amount(num_of_melons)
    if expected_cost != amount_paid:
        return False
    else:
        return True


def determine_payment_amount(num_of_melons):
    """
    Determines how much the payment should be for the amount of melons purchased
    :param num_of_melons: int
    :return: float
    """
    melon_cost = 1.0
    return melon_cost * num_of_melons


def print_incorrect_customer_payment(name, expected_payment, actual_payment):
    """
    Prints the payment information of customers who did not pay the correct amount
    :param name: string
    :param expected_payment: float
    :param actual_payment: float
    :return: None
    """
    print(name, "paid {:.2f}, expected {:.2f}".format(actual_payment, expected_payment))


def read_customer_file(filename):
    """
    Opens a customer log file and reports any incorrect payment information
    :param filename: string
    :return: None
    """
    file = open(filename)
    for line in file:
        line = line.rstrip()
        words = line.split("|")

        name = words[1]
        melons_purchased = int(words[2])
        amount_paid = float(words[3])

        if not did_customer_pay_correct_amount(melons_purchased, amount_paid):
            print_incorrect_customer_payment(name, determine_payment_amount(melons_purchased), amount_paid)
    file.close()


read_customer_file("customer-orders.txt")

