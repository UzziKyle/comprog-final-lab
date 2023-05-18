from security import askUsername
from modules import Modules as md

# System security
askUsername()

# Main program
students_records = []
modules = {
    1 : md.add_student,
    2 : md.search_student,
    3 : md.update_course,
    4 : md.filter_students_by_course,
    5 : md.count_students,
    6 : md.view_record,
}

def module_selector():
    while True:
        module_number = int(input("Main Menu:\n(1) Add Student\n(2) Search Student\n(3) Update Course\n(4) Filter by Course\n(5) Count Students\n(6) View Record\nEnter module number: "))
        print("\n")

        modules[module_number](students_records) # Will call the chosen module
        
        continue_program = input("\nWould you like to continue? (enter any key\s to Continue || enter q to Quit) -").strip().lower()
        if continue_program == "q":
            print("\nThank you for using me!")
            quit()

        print("\n")
        module_selector()

module_selector()