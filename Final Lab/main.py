from security import askUsername
from modules import Modules as md
import os

# System security
askUsername() # Username: ComputerScience  Password: PSU88@

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
        os.system('cls')
        module_number = int(input("Main Menu:\n(1) Add Student\n(2) Search Student\n(3) Update Course\n(4) Filter by Course\n(5) Count Students\n(6) View Record\n(7) Quit\nEnter module number: "))
        print("\n")

        modules[module_number](students_records) # Will call the chosen module
        
        continue_program = input("\nWould you like to continue? (enter any key\s to Continue || enter q to Quit) -").strip().lower()
        if continue_program == "q":
            print("\nThank you for using me!")
            quit()

        print("\n")
        module_selector()

module_selector()