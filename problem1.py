#!python3

# Canada Income Tax Calculator part I

'''
It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
Python to determine Federal and Provincial Income Tax.

The Canadian income tax system is a tiered system, which means you pay different percentages of
your income for different parts of your income.
You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
20.5% on amounts over 49020 that are less than 98040
26% on amounts over 98040 but less than 151978
29% on amounts over 151978 but less than 216511
33% on amounts over 216511

Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

Example:
Enter your income: 125000
Your federal income tax is: 24411.7

'''

income = float(input("Please enter your income> "))
if income <= 49020:
    tax = income * 0.15
if 49020 < income <= 98040:
    t = 49020 * 0.15
    a = ( income - 49020 ) * 0.205
    tax = a + t
if 98040 < income <= 151978:
    t = 49020 * 0.15
    a = ( 98040 - 49020 ) * 0.205
    b = ( income - 98040 ) * 0.26
    tax = a + b + t
if 151978 < income <= 216511:
    t = 49020 * 0.15
    a = ( 98040 - 49020 ) * 0.205
    b = ( 151978 - 98040 ) * 0.26
    c = ( income - 151978 ) * 0.29
    tax = a + b + t + c
if 216511 < income:
    t = 49020 * 0.15
    a = ( 98040 - 49020 ) * 0.205
    b = ( 151978 - 98040 ) * 0.26
    c = ( 216511 - 151978 ) * 0.29
    d = ( income - 216511 ) * 0.33
    tax = a + b + t + c + d

tax = round(tax, 2)
print(f"Your federal income tax is: ${tax}")