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

# Values greater than second - accepts a list and creates a new list containing only the values from the original list
# that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements,
# have the function return False
    # Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
    # Example: values_greater_than_second([3]) should return False

# define function which uses list as param
def values_greater_than_second(list):
    # create a new list which will contain our return values
    greater_than_second = []
    greater_total = 0
    # create a variable to store the second value of the arg list which gets passed in
    x = list[1]
    # iterate through the incoming list and check each value
    for i in range(len(list)):
        # check the length of incoming list to make sure it's greater than 2
        if len(list) < 2:
            # if list length is 2 or less, return False
            return False
        # check each index of the list to see if it's greater than the 2nd value of the list
        elif list[i] > list[1]:
            # if value is greater, add it to a new list
            greater_than_second.append(list[i])
            # iterate on count of how many values are greater than 2nd index
            greater_total += 1
        # if value is less, ignore that value
        else: 
            continue
    # print the total values greater than 2nd index
    print(f"The amount of indexes greater than 2nd index is: {greater_total}")
    # return the new list of values greater than 2nd index
    return greater_than_second

print(values_greater_than_second([5,2,3,2,1,4]))

# This Length, That Value - accepts two ints as params: size and value
# the function should create and return a list whose length is equal to the given size, and whose values are all the given value.
    # Example: length_and_value(4,7) should return [7,7,7,7]
    # Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# define a function which takes the params size and value
def length_and_value(size,value):
    # create a variable to store our list
    value_list = []
    # create a for loop which is inclusive range from the size param/arg
    for i in range(size + 1):
        # add the value to our values list
        value_list.append(value)
    #return the values list at the end of function
    return value_list

print(length_and_value(6,2))