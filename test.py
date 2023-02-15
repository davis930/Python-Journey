# function to print the ^3 of numbers in a list
def print_raised_to_the_third(numbers):
    for num in numbers:
        raised_to_the_third = num ** 3
        print(raised_to_the_third)

# loop to print the ^3 of numbers 1 through 5
for i in range(1, 6):
    print(i, "raised to the third is", i ** 3)

# loop to print the ^3 of even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i, "raised to the third  is", i ** 3)

# using the function to print the ^3 of a list of numbers
my_numbers = [3, 7, 9, 12, 16]
print("The ^3 of my numbers are:")
print_squares(my_numbers)
