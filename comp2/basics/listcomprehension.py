list_of_names = ["Bing", "Bang", "Boom"]
[bop for bop in list_of_names]
#returns ["B", "B", "B"]
    #each element becomes bop, and the value of each bop at 0 is returned into a list

my_list = []
[x for x in my_list]
#makes a copy of the list

list_of_ints = [0, 1, 2]
[str(num) for num in list_of_ints]
#makes new list with numbers as strings

one_to_ten = [x for x in range(1,11)]
#creates list of ints from 1 - 10
fractions = [1/n for n in range(100)]

list_of_nums = [2, 3, 4, 5, 6]
first_digits = [str(x) for x in list_of_nums]

list_of_name = ["Berry", "Benson", "Alice", "Jesse", "Ben"]
new_l = [x for x in list_of_name if x[0] == "B"]