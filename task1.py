'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
x = float(input("Please enter your expected number> "))
y = float(input("Please enter your actual value> "))

f = (( y - x ) / x) * 100
f = round(f, 2)

print(f"The percentage difference is {f}%")