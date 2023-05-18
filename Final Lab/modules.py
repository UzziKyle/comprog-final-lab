import pandas as pd

class Modules():
    def __init__(self) -> None:
        pass

    def add_student(students_records = list) -> None:
        students_informations = ["Full Name", "Age", "Course", "Year Level"]
        new_student = {students_informations[key]: (input(f"Enter {students_informations[key]}: ").strip().upper()) for key in range(len(students_informations))}
        students_records.append(new_student)

    def search_student(students_records = list) -> None:
        name_search = input("Enter the name of the student: ").strip().upper()
        print('\n')
        for student in students_records:
            if student["Full Name"] == name_search:
                for info in student:
                    print("{}: {}".format(info, student[info]))
                
    def update_course(students_records = list) -> None:
        name_search = input("Search by full name: ").strip().upper()
        print('\n')
        for student in students_records:
            if student["Full Name"] == name_search:
                for info in student:
                    if (info == "Full Name") or (info == "Course"):
                        print("{}: {}".format(info, student[info]))

        course_update = input("\nEnter student's new program: ").strip().upper()
        for student in students_records:
            if student["Full Name"] == name_search:
                for info in student:
                    if info == "Course":
                        student[info] = course_update

        for student in students_records:
            if student["Full Name"] == name_search:
                for info in student:
                    print("{}: {}".format(info, student[info]))

    def filter_students_by_course(students_records) -> None:
        course_search = input("Search by course: ").strip().upper()
        print("\n")
        for student in students_records:
            if student["Course"] == course_search:
                for info in student:
                    print("{}: {}".format(info, student[info]))
                print("\n")

    def count_students(students_records = list, count = 0) -> None:
        if len(students_records) - count != 0:
            count += 1
            Modules.count_students(students_records, count)

        else:
            print("There are currently {} students enrolled.".format(count))

    def view_record(students_records = list) -> None:
        print(pd.DataFrame(students_records))