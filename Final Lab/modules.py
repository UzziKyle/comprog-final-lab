from time import sleep as sp
import pandas as pd
import os

class Modules():
    def __init__(self) -> None:
        pass

    def add_student(students_records = list) -> None:
        os.system('cls')
        students_informations = ["Full Name", "Age", "Course", "Year Level"]
        new_student = {students_informations[key]: (input(f"Enter {students_informations[key]}: ").strip().upper()) for key in range(len(students_informations))}
        students_records.append(new_student)

    def search_student(students_records = list) -> None:
        os.system('cls')
        searched_name = input("Search by name: ").strip().upper()
        search_list = [student for student in students_records if searched_name in student["Full Name"]]

        if search_list == None:
            os.system('cls')
            print("No name in record.")
        
        else:
            os.system('cls')
            print("List of students with the name \"{}\":".format(searched_name))

            num = 0
            for student in search_list:
                num += 1
                print("({}) {}".format(num, student["Full Name"]))

            selected_student = int(input("\nEnter student number: ")) - 1
            
            os.system('cls')
            for details in search_list[selected_student]:
                print("{}: {}".format(details, search_list[selected_student][details]))

            sp(1)
         
    def update_course(students_records = list) -> None:
        os.system('cls')
        searched_name = input("Enter student's full name: ").strip().upper()
        print('\n')
        for student in students_records:
            if student["Full Name"] == searched_name:
                for info in student:
                    if (info == "Full Name") or (info == "Course"):
                        print("{}: {}".format(info, student[info]))

        course_update = input("\nEnter student's new program: ").strip().upper()

        os.system('cls')
        for student in students_records:
            if student["Full Name"] == searched_name:
                for info in student:
                    if info == "Course":
                        student[info] = course_update

        for student in students_records:
            if student["Full Name"] == searched_name:
                for info in student:
                    print("{}: {}".format(info, student[info]))

    def filter_students_by_course(students_records) -> None:
        os.system('cls')
        course_search = input("Search by course: ").strip()

        os.system('cls')
        print("STUDENTS IN \"{}\"\n".format(course_search))
        for student in students_records:
            if student["Course"] == course_search.upper():
                for info in student:
                    print("{}: {}".format(info, student[info]))
                print("\n")

    def count_students(students_records = list, count = 0) -> None:
        os.system('cls')
        if len(students_records) - count != 0:
            count += 1
            Modules.count_students(students_records, count)

        else:
            print("There are currently {} students enrolled.".format(count))

    def view_record(students_records = list) -> None:
        os.system('cls')
        print(pd.DataFrame(students_records))