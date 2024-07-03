# module for database operations --> SQLite interaction
# creates database if none exists

import sqlite3
import os

project = os.getcwd()
file = f'{project}/data/employees.db'

# function to create database and table (runs only once)
def create_database():
    conn = sqlite3.connect(file) # create or connect to SQLite database
    c = conn.cursor()   # create a cursor object

    # creates table if none exists
    c.execute('''CREATE TABLE IF NOT EXISTS employees
              (id INTEGER PRIMARY KEY, name TEXT, availability TEXT)''')
    
    conn.commit() # commit the changes
    conn.close() # close the connection

# function to add new employee
def add_employee(name, availability):
    conn = sqlite3.connect(file)
    c = conn.cursor()

    # insert row of data
    c.execute("INSERT INTO employees (name, availability) VALUES (?, ?)", (name, availability))


    conn.commit()
    conn.close()

# function to retrieve all employees
def get_employees():
    conn = sqlite3.connect(file)
    c = conn.cursor()

    # select all employees
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()

    conn.close()
    return employees

def how_many_employees():
    return len(get_employees())

def get_new_emp_from_user():
    new_emp_name = input('enter employee name: ')
    new_emp_availability = input('enter availability: ')
    add_employee(new_emp_name, new_emp_availability)

def getChoice():

    choice = 'z'
    while (choice != 'A' and choice != 'B'):

        choice = input('''What would you like to do?\n
        A) Edit Employee List
        B) Create a schedule\n''').capitalize()
        if (choice == 'A' or choice == 'B'):
            return choice
        
def employeeActions():
    choice = 'A'
    while (choice != 'D'):
            employee_choice = input('''What would you like to do?\n
            A) Add Employee
            B) Edit Employee
            C) Delete Employee
            D) Go Back\n''').capitalize()
            if (employee_choice == 'A'):
                get_new_emp_from_user()
            elif (choice == 'D'):
                break;