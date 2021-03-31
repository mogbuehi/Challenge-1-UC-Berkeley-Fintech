# Part 1: Automate Calculations
# ******************************************************************************************
# Print section title with extra line for legibility
print ('')
print('Part 1 : Automate Calculations')                                        
print('')
# Create variables for amount, sum, and 
# the average of the loans and print descriptive statement
loan_costs = [500, 600, 200, 1000, 450] 
amt_loans = len(loan_costs)         
sum_loans = sum(loan_costs)
avg_loans = sum_loans/amt_loans

print (f'The total amount of loans is {amt_loans}.')
print (f'The sum of all loans is ${sum_loans}.')
print (f'The average loan price is ${round(avg_loans)}.')

# Deliniate end of section
print ('*'*80)


# Part 2: Analyze Loan Data
# ******************************************************************************************
# Print section title with extra line for legibility
print('')
print('Part 2 : Analyze Loan Data')    
print ('')                                         

# Dictionary object of loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use `.get()` method (as opposed to key indexing) to store 
# the following in variables: future value and remaining months
# and print a descriptive statement with those variables.

future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')
print(f'The future value of the loan is ${future_value}.')
print(f'The remaining months on the loan are {remaining_months}.')

# Store 0.2 in `discount_rate` variable.
# Calculate present value of loan and save to variable called `present_value`. 
discount_rate = 0.20
present_value = future_value / (1 + discount_rate/12) ** remaining_months

# Write if-else script that prints 'Loan is at least-break even and is a fair price.' 
# if present value greater than or equal to future value, 
# else print ('Loan is too expensive and not worth present value calculated')
if present_value >= loan.get('loan_price'):
    print('Loan is at least break-even and is a fair price.')
else:
    print('Loan is too expensive and not worth the present value calculated.')

print('*'*80)


# Part 3: Perform financial calculations using functions
# ******************************************************************************************
print('')
print('Part 3: Perform finanacial calculations using functions')                                        
print('')


# Dict object for new_loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Present value evaluator function that takes future value, remaining months, 
# and annual discount rate as parameters and returns calculation of present value stored in variable.
def present_value_evaluator (future_value, remaining_months, annual_discount_rate):
    present_value = future_value / ( 1 + annual_discount_rate/12 ) ** remaining_months
    return present_value

# Calling function with arguments derived from `new_loan` dict object, and using 0.2 as discount rate.
present_value_evaluator (new_loan.get('loan_price'), new_loan.get('remaining_months'), 0.2)
print(f"The present value of the loan is: ${round(present_value, 2)}")

# Deliniate end of section
print ('*'*80)


# Part 4: Conditionally filter list of loans
# ******************************************************************************************
print('')
print('Part 4: Conditionally filter list of loans') 
print('')
# Loan data expressed as a list of dictionaries
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Use for loop to find loans with price lower than 500. 
# Initiate an empty list.
inexpensive_loans = []
# For loop to find loan price with .get() method
# Within for loop use if statement to append `inexpensive_loans` list with loan dict that 
# has `loan_price` > 500. Print resulting list outside of loop.
for loan in loans:
    loan_price = loan.get('loan_price')
    if loan_price < 500:
        inexpensive_loans.append(loan)

print('The list of inexpensive loans : ', inexpensive_loans)

# Deliniate end of section
print ('*'*80)

# Part 5: Save the results
# ******************************************************************************************
print('')
print('Part 5: Save the results') 
print('')

#Importing entire `csv` libary. Importing `Path()` function from `pathlib` library
import csv      
from pathlib import Path            

# Data table header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the path of the file. In other words create the filename that the data will be saved to
output_path = Path("inexpensive_loans.csv")

# Use `with`-`open()`-`as` pattern to save file as a '.csv' file. Use for loop and .writerows() 
# method to transfer dictionaries saved in `inexpensive_loans` list into rows in a csv file.
with open (output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

# Print messsage that states that file has been written to `output_path` directory.
print (f'Results are saved as {output_path} and is located in same folder as this python file.')