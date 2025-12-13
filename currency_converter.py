"""Currency converter (from US dollars to Turkish lira)"""
try:
    US_dollar_currency = 42.58
    amount_US_dollar = float(input('Please enter the amount of US dollar you have: '))
    amount_Turkish_lira = amount_US_dollar * US_dollar_currency
    if amount_US_dollar < 0:
        print('Please enter a valid amount!')
    else:
        print(f'You have {amount_Turkish_lira} Turkish liras.')

except ValueError:
    print('Please enter a number, not a text!')
