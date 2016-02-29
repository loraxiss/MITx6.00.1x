def remaining_balance(balance, payment, annual_int):
    '''
    balance is the amount remaining on the loan
    payment is the reduction on the balance
    annual_int is the annual interest being charged
    
    This function will return the remaining loan balance not rounded
    '''
    reduced_balance = balance - payment
    interest = reduced_balance * (annual_int/12)
    return(reduced_balance + interest)

total_paid = 0

for month in range(1, 13):
    payment = balance * monthlyPaymentRate
    balance = remaining_balance(balance, payment, annualInterestRate)
    total_paid += payment
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(payment, 2))) 
    print('Remaining balance: ' + str(round(balance, 2)))

print('Total paid: ' + str(round(total_paid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))

