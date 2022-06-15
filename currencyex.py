def exchange_money(budget, exchange_rate):
    """Create function to estimate value after exchange

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate
    pass


def get_change(budget, exchanging_value):
    """Create function to calculate currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value
    pass


def get_value_of_bills(denomination, number_of_bills):
    """Create function to calculate value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return int(denomination * number_of_bills)
    pass


def get_number_of_bills(budget, denomination):
    """Create function to calculate number of bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget // denomination)
    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Create function to calculate value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    return ((budget / (exchange_rate + exchange_rate * spread/100)) // denomination) * denomination
    pass
    def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """Create function to calculate non-exchangeable value

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    return int((budget / (exchange_rate + exchange_rate * spread/100)) % denomination)
    pass
