#Student Database Python Script
#Dominick Ferro

import time

time_format = '%Y-%m-%d %X'  # time configuration
time.strftime(time_format, time.gmtime(time.time()))


def showInfo():  # Student info database
    print("-" * 30)  # Show available functions
    print("University Student Management System")
    print("1. Add student information")
    print("2. Delete student information")
    print("3. Modify student information")
    print("4. Query student information")
    print("5. Save all student information")
    print("6. Show all student information")
    print("7. Exit the program")
    print('-' * 30)


# list that stores info of students defined
students = []

while True:
    # Show function list to user
    showInfo()
    # Ask user to select function
    # Show function selected by user
    key = int(input("Please select the function you want to access:"))

    # Complete the function according to function selected
    if key == 1:
        print("You have selected to add student information")
        name = input("Please enter the student's name:")
        newid = input("Please enter student ID (IDs can not be repeated):")
        age = input("Please enter the age of the student:")
        sex = input("Please enter the gender/sex of the student:")
        address = input("Please enter the student's address:")
        credit = 4

        # Check to see if student ID has been used before
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == newid:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            print("Repeated student ID input, failed to add!")
            break
        else:
            # Define dictionary to store single student info
            stuInfo = {}
            stuInfo['name'] = name
            stuInfo['id'] = newid
            stuInfo['age'] = age
            stuInfo['sex'] = sex
            stuInfo['address'] = address
            stuInfo['Grade Points'] = credit


            # Added Single student info to list
            students.append(stuInfo)
            print("Added successfully!")


    elif key == 2:
        print("You have selected to delete student function")
        delId = input("Please enter the student ID that you want deleted:")
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == delId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 0:
            print("This student ID does not exist, deletion failed!")
        else:
            del students[i]
            print("successfully deleted!")


    elif key == 3:
        print("You have selected to modify student information")
        alterId = input("Please type the student ID that you would like to modify:")
        # Is student ID available,if so modify the info
        i = 0
        leap = 0
        for temp in students:
            if temp['id'] == alterId:
                leap = 1
                break
            else:
                i = i + 1
        if leap == 1:
            while True:
                alterNum = int(input(" 1.Modify student ID\n 2.Edit name \n 3.Modify age \n 4.Modify gender \n 5.Modify address \n 6.Exit modification\n"))
                if alterNum == 1:
                    newId = input("Enter the changed student ID:")

                    # Verify student ID to make sure it is unique
                    i = 0
                    leap1 = 0
                    for temp1 in students:
                        if temp1['id'] == newId:
                            leap1 = 1
                            break
                        else:
                            i = i + 1
                    if leap1 == 1:
                        print("The input student ID cannot be repeated, the modification failed!")
                    else:
                        temp['id'] = newId
                        print("Student ID has been changed successfully")
                elif alterNum == 2:
                    newName = input("Enter the changed name:")
                    temp['name'] = newName
                    print("Name modified successfully")
                elif alterNum == 3:
                    newAge = input("Enter the changed age:")
                    temp['age'] = newAge
                    print("Age modified successfully")
                elif alterNum == 4:
                    newsex = input("Enter the changed gender:")
                    temp['sex'] = newsex
                    print("Gender modified successfully")
                elif alterNum == 5:
                    newadress = input("Enter the changed address:")
                    temp['adress'] = newadress
                    print("Address modified successfully")
                    break
                else:
                    print("Input errors found, please re-enter")
        else:
            print("Without the right student ID, modification failed!")
    elif key == 4:
        print("You have selected the function of querying student information")
        alterNum = int(input(
            "1. Query by student number\n 2. Query by grade point \n 3. Query by address \n 4. Exit modification\n"))
        if alterNum == 1:
            searchID = input("Please input the student ID of the student you would like to examine:")
            i = 0
            leap = 0
            for temp in students:
                if temp['id'] == searchID:
                    leap = 1
                    break
                else:
                    i = i + 1
            if leap == 0:
                print("Without the right student ID, the query failed!")
            else:
                print("Student found, the information is as follows:")
                print("student ID:%s\nName:%s\nage:%s\nGender:%s\nAddress:%s\nGrade points:%s\n" % (
                temp['id'], temp['name'], temp['age'], temp['sex'], temp['adress'], temp['Grade point']))
        elif alterNum == 2:
            newcredit = input("Please type in the grade point of the specific student you want to inspect:")
            i = 0
            leap = 0
            for temp in students:
                if temp['Grade Points'] == newcredit:
                    leap = 1
                    break
                else:
                    i = i + 1
            if leap == 0:
                print("Without this grade point, the query failed!")
            else:
                print("Discover student information based on grade points, the information is as follows:")
                print("student ID:%s\nName:%s\nage:%s\nGender:%s\nAddress:%s\nGrade points:%s\n" % (
                temp['id'], temp['name'], temp['age'], temp['sex'], temp['address'], temp['Grade point']))
        elif alterNum == 3:
            newadress = input("Please enter the address you would like to query:")
            i = 0
            leap = 0
            for temp in students:
                if temp['address'] == newadress:
                    leap = 1
                    break
                else:
                    i = i + 1
            if leap == 0:
                print("Without this address, the query failed!")
            else:
                print("Observe student information according to address, the information is as follows:")
                print("student ID:%s\nName:%s\nage:%s\nGender:%s\nAddress:%s\nGrade points:%s\n" % (
                temp['id'], temp['name'], temp['age'], temp['sex'], temp['address'], temp['Grade point']))
        elif alterNum == 4:
            break
        else:
            print("Input errors found, please re-enter")

    elif key == 5:  # Save info
        try:
            students_txt = open("a.txt", "a")  # Open type mode and clear file
        except Exception as e:
            students_txt = open("a.txt", "x")  # File not found, create file and open
        for temp in students:
            students_txt.write(str(temp) + "\n")  # Store line, add a new line
        students_txt.close()
    elif key == 6:

        #Output student info
        print('*' * 20)
        print("Next, go through all the student information...")
        print("*" * 20)
        print("first name".center(8), "student ID".center(10), "age".center(4), "gender".center(10),
              "address".center(10), "Grade point".center(10))
        i = 1
        for temp in students:
            print(i, temp.get("name").center(8), temp.get("id").center(10), temp.get("age").center(10),
                  temp.get("sex").center(10), temp.get("a\
dress").center(11), "{:^12.2f}".format(temp.get("Grade point")))
        i += 1

    elif key == 7:

        # Verify if you want exit the function
        quitconfirm = input("Are you sure that you want to quit (yes or no)??~~(>_<)~~??")
        if quitconfirm == 'yes':
            print("Welcome to use this program at the current time, thank you")
            break;
    else:
        print("There was a mistake, please try again")
input(time.strftime(time_format, time.gmtime(time.time())))


