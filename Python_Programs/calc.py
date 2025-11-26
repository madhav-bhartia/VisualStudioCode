import decimal

numbers = ['0.004603727530668907', '0.005028172327714191', 
           '0.004708151673666186', '0.004544157307882615', 
           '0.004855784731852961', '0.004738926288448479']

# Convert the list of strings to a list of Decimal objects
decimal_numbers = [decimal.Decimal(num) for num in numbers]

# Calculate the sum of the Decimal objects
total = sum(decimal_numbers)

# Calculate the average
average = total / len(decimal_numbers)

print(average)