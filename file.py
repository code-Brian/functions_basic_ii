# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countDown(5) should return [5,4,3,2,1,0]

def countDown(number):
    countList = []
    for x in range(number, 0, -1):
        countList.append(x)
    return countList

count = countDown(5)
print(count)

# Print and Return - Receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2. 

def print_and_return(list):
    print(list[0])
    return(list[1])

printReturn = print_and_return([5,10])
print(printReturn)

# First Plus Length - Accepts a list and returns the sum of the first value in list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6. (first value: 1 plus length:5)

def first_plus_length(list):
    first = list[0]
    length = len(list)

    return first + length

print(first_plus_length([1,2,3,5,6,7,8,9,10,11,12,13]))
