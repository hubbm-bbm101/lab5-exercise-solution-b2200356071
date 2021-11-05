
N = int(input("Enter a number: "))

sum_of_odd_numbers = 0
average_of_even_numbers = 0

for i in range(1, N+1):
    if i % 2 == 0:
        average_of_even_numbers += i
    else:
        sum_of_odd_numbers += i

print("Sum of odd numbers is", sum_of_odd_numbers)
print("Average of even numbers is", average_of_even_numbers/N/2)