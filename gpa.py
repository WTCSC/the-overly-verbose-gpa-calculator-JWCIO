print ("Welcome to the GPA calculator!")
classnum = int(input("How many classes are you taking? "))
grades = []
if classnum <= 0:
    print("You must be taking at least one class!")
    exit()

def convert(grade):
    if grade >= 93:
        return 4.0
    elif grade >= 90:
        return 3.7
    elif grade >= 87:
        return 3.3
    elif grade >= 83:
        return 3.0
    elif grade >= 80:
        return 2.7
    elif grade >= 77:
        return 2.3
    elif grade >= 73:
        return 2.0
    elif grade >= 70:
        return 1.7
    elif grade >= 67:
        return 1.3
    elif grade >= 65:
        return 1.0
    else:
        return 0.0
    
for i in range(classnum):
    try:
        grade = float(input("What is your grade in class " + str(i+1) + "? "))
    
    except ValueError:
        print("Letters are too vague! Please enter a numerical grade.")
        grade = float(input("What is your grade in class " + str(i+1) + "? "))
    if float(grade) < 0 or float(grade) > 100:
        print("Invalid grade! Please enter a grade between 0 and 100.")
        grade = float(input("What is your grade in class " + str(i+1) + "? "))
  
    
    grades.append(float(convert(float(grade))))
    
gpa = sum(grades) / classnum
print("Your GPA is: " + str(gpa))



