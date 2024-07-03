# main script run when program is started
# launches GUI and either connects to or creates db file if none exists
# orchestrates scheduling logic
import os
from database import file, create_database, add_employee, get_employees, employeeActions, get_new_emp_from_user, how_many_employees, getChoice

def main():

    if (os.path.exists(file) and os.path.isfile(file)):
        print('database exists!')
    else:
        create_database()

    print('Welcome to the EZBreZE Scheduling App\n')
    choice = getChoice()
    if (choice == 'A'):
        employeeActions()

if __name__ == "__main__":
    main()