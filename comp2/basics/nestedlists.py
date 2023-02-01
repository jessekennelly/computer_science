people_and_colors = [["Aaliyah", "Blue"],
                     ["Brandon", "Green"],
                     ["Carmen", "Red"],
                     ["Diego", "Yellow"]]
students_and_grades = [["Aaliyah", [90, 80, 70]],
                       ["Brandon", [80, 70, 60]],
                       ["Carmen", [70, 60, 50]],
                       ["Diego", [60, 50, 40]]]
#print each student name along with average grade
for row in students_and_grades:
    name = row[0]
    grades = row[1]
    avg = sum(grades) / len(grades)
    print(f"{name}, {avg}")
    

employees_and_titles = [["Aaliyah", "Manager"],
                        ["Brandon", "Software Developer"],
                        ["Carmen", "Product Manager"],
                        ["Diego", "Technical Writer"]]
deck = [['Ace', 'Spades'], ['2', 'Spades'], ['3', 'Spades'],
        ['4', 'Spades'], ['5', 'Spades'], ['6', 'Spades'], ['7', 'Spades'],
        ['8', 'Spades'], ['9', 'Spades'], ['10', 'Spades'], ['Jack', 'Spades'],
        ['Queen', 'Spades'], ['King', 'Spades'], ['Ace', 'Hearts'], ['2', 
'Hearts'],
        ['3', 'Hearts'], ['4', 'Hearts'], ['5', 'Hearts'], ['6', 'Hearts'],
        ['7', 'Hearts'], ['8', 'Hearts'], ['9', 'Hearts'], ['10', 'Hearts'],
        ['Jack', 'Hearts'], ['Queen', 'Hearts'], ['King', 'Hearts'], ['Ace', 
'Diamonds'],
        ['2', 'Diamonds'], ['3', 'Diamonds'], ['4', 'Diamonds'], ['5', 'Diamonds'],
        ['6', 'Diamonds'], ['7', 'Diamonds'], ['8', 'Diamonds'], ['9', 'Diamonds'],
        ['10', 'Diamonds'], ['Jack', 'Diamonds'], ['Queen', 'Diamonds'], ['King', 
'Diamonds'],
        ['Ace', 'Clubs'], ['2', 'Clubs'], ['3', 'Clubs'], ['4', 'Clubs'], ['5', 
'Clubs'],
        ['6', 'Clubs'], ['7', 'Clubs'], ['8', 'Clubs'], ['9', 'Clubs'], ['10', 
'Clubs'],
        ['Jack', 'Clubs'], ['Queen', 'Clubs'], ['King', 'Clubs']]





exit()
# ^ break point

#nested_list[row][col]

#for row in my_list:

    #for col in row:

"""
currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()
"""

