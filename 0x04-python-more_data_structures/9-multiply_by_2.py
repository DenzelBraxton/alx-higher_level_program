def multiply_by_2(a_dictionary):
#create a variable to store new result
    multiple = {}
#run loop to iterate through key values
    for i in a_dictionary:
        multiple[i] = a_dictionary[i] * 2
        return multiple
