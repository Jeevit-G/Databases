# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'cuz_music.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

# This is the SQL to connect to all the tables in the database
TABLES = (" cuz_music "
           "LEFT JOIN Gender ON cuz_music.gender_id = gender.gender_id "
           "LEFT JOIN Instrument ON cuz_music.instrument_id = instrument.instrument_id "
           "LEFT JOIN School on cuz_music.school_id = school.school_id "
           "LEFT JOIN Days on cuz_music.days_id = days.days_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  


menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Music Lessons database\n\n'
                    'Type the letter for the information you want:\n'
                    'A: All Music Lesson Data\n'
                    'B: Monday Lessons\n'
                    'C: Wednesday Lessons\n'
                    'D: Owed money\n'
                    'O: Other\n'
                    'Z: Exit\n\nType option here: ')

    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All Data')
    elif menu_choice == 'B':
        print_query('Monday Lessons')
    elif menu_choice == 'C':
        print_query('Wednesday Lessons')
    elif menu_choice == 'D':
        print_query('Parents who owe')
    elif menu_choice == 'O':
        name = input('Enter student name: ')
        print_parameter_query("name, last_name, instrument, gender, lesson_time", "name = ?",name)

  # Import the libraries to connect to the database and present the information in tables

    
