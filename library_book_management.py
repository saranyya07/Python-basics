books=[]
while True:
    print("\n---Library Book Management System---")
    print("!.Add Book")
    print("2.Display Books")
    print("3.Search Book")
    print("4.Issue Book")
    print("5.Return Book")
    print("6.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        book_id=input("Enter your choice: ")
        title=input("Enter Book Title: ")
        book={
            "ID":book_id,
            "Title":title,
            "Available":True
            
        }
        books.append(book)
        print("Book added successfully!")
    elif choice==2:
        if len(books)==0:
            print("No books available.")
        else:
            print("\nBook Records: ")
            for b in books:
                status="Available" if b["Available"] else "Not Available"
                print(b["ID"],"-",b["Title"],"-",status)
    elif choice ==3:
        book_id=input("Enter Book ID to seach: ")
        found = False
        for b in books:
            if b["ID"]==book_id:
                status="Available" if b["Available"] else "Not Available"
                print("Book Found!")
                print("ID:",b["ID"])
                print("Title:",b["Title"])
                print("Status:",status)
                found=True
                break
        if not found:
            print("Book not found.")
    elif choice==4:
        book_id=input("Enter Book ID to issue: ")
        found=False
        for b in books:
            if b["ID"]==book_id:
                if b["Available"]:
                    b["Available"]=False
                    print("Book issues successfully!")
                else:
                    print("Book is already issued.")
                found=True
                break
        if not found:
            print("Book not found.")
        elif choice==5:
            book_id=input("Enter Book ID to return: ")
            found=False
            for b in books:
                if b["ID"]==book_id:
                    if not b["Available"]:
                        b["Available"]=True
                        print("Book returned successfully!")
                    else:
                        print("Book was not issues.")
                    found=True
                    break
            if not found:
                print("Book not found.")
        elif choice==6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
