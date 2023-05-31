from security import run_security
from modules import Modules as md
from time import sleep as sp
from os import system as sys

# Main program
students_records = [
    {
        "Full Name" : "UZZIEL KYLE R. YNCIONG",
        "Age" : "20",
        "Course" : "BSCS",
        "Year Level" : "1",
    },
]
modules = {
    1 : md.add_student,
    2 : md.search_student,
    3 : md.update_course,
    4 : md.filter_students_by_course,
    5 : md.count_students,
    6 : md.view_record,
    7 : exit,
}

def module_selector():
    while True:
        try:
            sys('cls')
            module_number = int(input("STUDENT DIRECTORY\n\nMain Menu:\n(1) Add Student\n(2) Search Student\n(3) Update Course\n(4) Filter by Course\n(5) Count Students\n(6) View Record\n(7) Quit\n\nEnter module number: "))
            print("\n")

        except ValueError:
            print("Invalid Input", end="\r")
            sp(0.5)

        except KeyError:
            print("Invalid Input", end="\r")
            sp(0.5)

        else:
            modules[module_number](students_records) # Will call the chosen module
        
            while True:
                try:
                    continue_program = input("\nEnter 'c' to Continue|| enter 'q' to Quit - ").strip().lower()
                
                    if continue_program not in "qc":
                        raise ValueError("Invalid Input")
                    
                except ValueError:
                    print("Invalid Input", end="\r")
                    sp(0.5)
                    sys('cls')

                except KeyError:
                    print("Invalid Input", end="\r")
                    sp(0.5)
                    sys('cls')

                else:
                    if continue_program == "q":
                        print("\nThank you for using me!")
                        quit()

                    print("\n")
                    module_selector()

# System security
run_security() # Username: ComputerScience  Password: PSU88@

# Main
module_selector()
