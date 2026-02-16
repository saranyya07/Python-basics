name=input("enter student name: ")
marks=float(input("Enter student marks(out of 100): "))
if marks <0 or marks >100:
    print("Invalid input,enter marks between 1 and 100")
else:
    if marks>=90:
        grade="A+"
    elif marks>=75:
        grade="A"
    elif marks>=60:
        grade="B"
    elif marks>=50:
        grade="C"
    elif marks>=35:
        grade="D"
    else:
        grade="F"
    print("Student name: ",name)
    print("Student marks: ",marks)
    print("Grade: ",grade)
    
    if marks>=35:
        print("Result:PASS")
        if marks>=75:
            print("outstanding performance")
    else:
        print("FAIL")