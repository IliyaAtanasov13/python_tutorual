def tax_in_us(state, gross_income):
    """
    Calculate the net income after federal and state tax
    :param state: Gross income
    :param gross_income: State name
    :return: Net income
    """
    state_tax = {'Florida': 0.05, 'Maine': 0.035, 'Alaska': 0.07}
    if state in state_tax:
        net_income = gross_income - (gross_income * 0.1) - (gross_income * state_tax[state])
        print(f'Your income after all taxes is: {net_income}')
        return net_income
    else:
        print('State is not in the list.')
        return None


tax_in_us('Florida', 10000)


car = {'make': 'bmw', 'model': '2 series', 'year': 2014}


def exception_handling():
    try:
        print(car['color'])
    except:
        print('Key value is not in dictionary')
    else:
        print('Key is found')
    finally:
        print('Exception handling method was run.')


exception_handling()