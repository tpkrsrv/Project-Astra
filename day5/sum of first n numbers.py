n = 10  # Let's find the sum of numbers from 1 to 10
total_sum = 0  # Our bucket

for i in range(1, n + 1):
    total_sum = total_sum + i  # Add the current number to our bucket

print(f"The sum of the first {n} numbers is: {total_sum}")

