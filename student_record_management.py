students=[]
while True:
    print("\n--- Student Record Management System---")
    print("1.Add Student")
    print("2.Display Students")
    print("3. Search Students")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sid = int(input("Enter Student ID: "))
        name=input("Enter Name: ")
        marks =float(input("Enter Marks: "))
        student = {
            "ID":sid,
            "Name":name,
            "Marks":marks
            }
        students.append(student)
        print("Student added successfully.")
    elif choice == 2:
        if len(students)==0:
            print("No student records found.")
        else:
            print("\nStudent Records: ")
            for s in students:
                print("ID:",s["ID"])
                print("Name:",s["Name"])
                print("Marks:",s["Marks"])
                
    elif choice ==3:
        sid=int(input("Enter Student ID to search: "))
        found=False
        for s in students:
            if s["ID"]==sid:
                print("Student Found!")
                print("ID",s["ID"])
                print("Name:",s["Name"])
                print("Marks: ",s["Marks"])
                found=True
                break
        if not found:
            print("Student not found.")
        elif choice==4:
            sid=int(input("Enter Student ID to update: "))
            found=False
            for s in students:
                if s["ID"]==sid:
                    s["Name"]=input("Enter New Name: ")
                    s["Marks"]=float(input("Enter New Marks: "))
                    print("Student record updated successfully!")
                    found=True
                    break
            if not found:
                print("Student not found.")
        elif choice==5:
            sid=int(input("Enter Student ID to delete: "))
            found =False
            for s in students:
                if s in students:
                    if s["ID"]==sid:
                        students.remove(s)
                        print("Student recors deleted successfully!")
                        found=True
                        break
                    if not found:
                        print("Student not found.")
        elif choice==6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
        
