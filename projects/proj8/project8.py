name = ""
hours = 0
gpa = 0
mhours = 0
mgpa = 0
credit_hour = []
grades = []
mcredir_hour = []
mgrades = []

gpa_val = {"A+": 4.0, "A": 4.0, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

while True: #asks for name until valid one is inputted
    first = input("Enter first name: ")
    
    last = input("Enter last name: ")
    first.lower() #setting both values to lower case so file can be located
    last.lower()
    fullName = (f"{first}_{last}.txt")
    print(fullName)
    try:
        with open(fullName) as fileWorks:
            break #when a file is found the loop breaks
    except IOError:
        print("Student name not found") #error message displays when invalid student name is put in and starts loop over
    with open(fullName) as fileInfo:
        print("File found")
        checkMajor = input("Enter major: ")
        count = 1
        for line in fileInfo:
            if count == 1: #first line of file contains name
                name = line
            if count == 2: #second line contains major
                major = line.rstrip()
            if count > 2:
                line = line.strip("\n").split(",") #puts grade and credit hour into different dictionary
                if line[0] == checkMajor:
                    mgrades.append(line[4])
                    mcredir_hour.append(line[3])
                grades.append(line[4])
                credit_hour.append(line[3])
            count+= 1
        for hours in credit_hour: #changes credit hours from string to a float
            currentHours = hours
            currentHours = float(currentHours)
            hours += currentHours
        count2 = 0
        for mhours in mcredir_hour:
            currentMHour = mhours
            currentMHour = float(currentMHour)
            mhours += currentMHour
        for grade in grades: #changes letter grades to gpa value and adds to gpa 
            if grade != "T" and grade != "P":
                newGrade = 0
                newGrade = gpa_val[grade]
                gpa += newGrade
                count2 += 1
        gpa = gpa/count2
        count3 = 0
        for mgrade in mgrades: #changes inputted letter grades to numbers
            if mgrade != "T" and mgrade != "P":
                majorGrade = 0
                majorGrade = gpa_val[mgrade]
                mgpa += majorGrade
                count3 += 1
        mgpa = mgpa/count3
        if checkMajor == major: #double checks to see if the inputted major is valid
            print(f'Name: {name}', end="")
            print(f"Major: {major}\n", end="")
            print(f"University credit hours: {hours}\n", end="")
            print(f"GPA: {gpa:.2f}")
            print(f"Credit hours in major: {mhours}")
            print(f"GPA in major: {mgpa:.2f}")
        else:
            print("Major does not match")