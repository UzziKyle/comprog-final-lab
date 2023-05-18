import pandas as pd

class Modules():
    def __init__(self) -> None:
        pass

    def add_student(students_records = list) -> None:
        students_informations = ["Full Name", "Age", "Course", "Year Level"]
        new_student = {students_informations[key]: (input(f"Enter {students_informations[key]}: ").strip().upper()) for key in range(len(students_informations))}
        students_records.append(new_student)

    def search_student(students_records = list) -> None:
        searched_name = input("Search by name: ").strip().upper()
        print('\n')
        for student in students_records:
            if searched_name in student["Full Name"]:
                for info in student:
                    print("{}: {}".format(info, student[info]))
                print("\n")
                
    def update_course(students_records = list) -> None:
        searched_name = input("Enter student's full name: ").strip().upper()
        print('\n')
        for student in students_records:
            if student["Full Name"] == searched_name:
                for info in student:
                    if (info == "Full Name") or (info == "Course"):
                        print("{}: {}".format(info, student[info]))

        course_update = input("\nEnter student's new program: ").strip().upper()
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
        course_search = input("Search by course: ").strip().upper()
        print("\n")
        for student in students_records:
            if student["Course"] == course_search:
                for info in student:
                    print("{}: {}\n".format(info, student[info]))

    def count_students(students_records = list, count = 0) -> None:
        if len(students_records) - count != 0:
            count += 1
            Modules.count_students(students_records, count)

        else:
            print("There are currently {} students enrolled.".format(count))

    def view_record(students_records = list) -> None:
        print(pd.DataFrame(students_records))