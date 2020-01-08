#Question
# The series, 11 + 22 + 33 + … + 1010 = 10405071317. Find the last ten digits of the series, 11 + 22 + 33 + … + 10001000.

# Algorithm
# Initialize sum as 0
# Run the for loop from 1 to 1000
# sum = sum + n to the power n
# print the remainder of dividing sum by 10**10

end = 1000
mod = 10**10
sum = 0
for x in range(1, end+1):
    sum += x**x

#Print last ten digit of the series
print(sum % mod)

