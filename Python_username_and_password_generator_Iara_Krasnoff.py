#Import Section

from datetime import date           #import this for Date
import getpass                      #import this for User
import random                       #used to create random elements for generating passwords.
import json                         #used to read and write employee data to/from a JSON-formatted file.


#Flower Box Section

###########################################################################
#
#   Name: Iara Krasnoff 
#   Date: 04/15/2024
#   This Python program reads employee data from an "employee_data.txt" file using JSON. 
#   Then, it gathers and confirms the end user's input for employee details. Afterwards, 
#   it generates usernames and passwords. It also stores employee data in a dictionary, 
#   writing the data back to the "employee_data.txt" file. Also, it is set to display the 
#   system username, current date, employee data in tuples, usernames, employee data
#   dictionary, and sorted usernames list.
#
###########################################################################

#Variables Section

# Prepare the variables to store user's input and stablish the flow of the program.
first_name = ""                         #Stores the user's input for the first name.
last_name = ""                          #Stores the user's input for the last name.
year_born = ""                          #Stores the user's input for the year of birth.

is_this_correct = ""                    #Stores the user's confirmation input.

# Prepares lists and a dictionary to store employee's data and usernames.
all_employee_data_in_tuples_list = []   #List to hold employee data tuples.

username_list = []                      #List to store generated usernames.

username_sorted_list = []               #List to store sorted usernames.

employee_data_dictionary = {}           #Dictionary to draw usernames to employee's data.

# Stablishes a list of accepted "Yes" responses for end user confirmation.
YES_LIST = ["Yes", "YES", "Y", "yes", "y"]

password_length = ""                    #Prepares a variable to store the desired password length.
employee_greeting_and_age_list = []     #Creates an empty list to store employee greetings and ages.
employee_greeting_age = ()              #Prepares an empty tuple to store an employee's greeting and age.
greet = ""                              #Prepares a variable to store an employee's greeting message.
age = 0                                 #Prepares a variable to store an employee's age.
use_special_characters = False          #Prepares a flag variable to indicate if special characters should be used in the password.

error_message = ""                      #Prepares error message variable.
file_name = "employee_data.txt"         #File name for data storage.


#Function Section

def build_username(first, last, year, dup):
    """ function to create username"""
    if(not dup):            #Generates an username as defalt, without duplicates, using the first letter of the first name, last name in lowercase, and the last two digits of the year.
        username = first[0].lower()+last.lower()+year[-2:]
    else:                   #Generates an username specifically for duplicates, using the entire first name in lowercase, the first letter of the last name in lowercase, and the last two digits of the year.
        username = first.lower()+last[0].lower()+year[-2:] 

    return username   

def build_password(password_length, use_special_characters, use_numbers):                               #Defines character sets for generating passwords.
        ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRsSsTtUuVvWwXxYyZz"
        SPECIAL_CHARACTERS = "!@#%^$*"
        NUMBERS = "1234567890"

        count = 0
        password = ""

        while count < password_length:                 #Generates the password character by character.
            randomNumber = random.randrange(0,52,1)
            pwChar = ALPHABET[randomNumber]
            password = password + pwChar
            pwChar = ""
            count = count +1

            if use_special_characters and count < password_length: #Adds special characters to the password if the flag is set.
                randomNumber = random.randrange(0,7,1)
                pwChar = SPECIAL_CHARACTERS[randomNumber]
                password = password + pwChar
                pwChar = ""
                count = count +1
                
    
            if use_numbers and count < password_length: #Adds numbers to the password if the flag is set.
                randomNumber = random.randrange(0,9,1)
                pwChar = NUMBERS[randomNumber]
                password = password + pwChar
                pwChar = ""
                count = count +1

        return password        

#Input Section

try:                #Tries to open and read a JSON-formatted file named "employee_data.txt"
    with open(file_name, "r", encoding="utf-8") as file:   #Reads each line from the file, converts single quotes to double quotes, and loads the JSON data into the employee_data_dictionary.
        for line in file:      
            temp_dict = str(line)
            temp_dict = temp_dict.strip()
            temp_dict = temp_dict.replace("\'", "\"")
            employee_data_dictionary = json.loads(temp_dict)
except FileNotFoundError:           #If the file does not exist, prints an error message.
    print(f"Sorry, the file {file_name} does not exist.")
else:                               #Closes the file if it was successfully read.
    file.close()

print("Enter the information below to create an username for the network.")
# The while loop is used to gather information for at least 2 employees.
while len(all_employee_data_in_tuples_list) < 2:

    # Prompts the end user to enter the employee's first name and validates its length (at least 2 digits).
    first_name = input("Enter an employee first name: ")
    while len(first_name) < 2:
        first_name = input("Enter an employee first name: ")

    # Prompts the end user to enter the employee's last name and validates its length (at least 2 digits).
    last_name = input("Enter an employee last name: ")
    while len(last_name) < 2:
        last_name = input("Enter an employee last name: ")

    # Prompts the end user to enter the employee's year of birth and validates its length (at least 4 digits).
    year_born = input("Enter an employee year of birth: ")
    while len(year_born) < 4:
        year_born = input("Enter an employee year of birth: ")

    while  True:
        print(error_message)
        password_length = input("Enter a number between 6 and 10 or 16 for the length of your password: ")
        try:                             #The while loop creates an infinite loop that will only break if the end user selects the numbers inside of the required range.
            password_length = int(password_length)
            if(6 <= password_length <=10 or password_length == 16): #Defines a password length's range.
                error_message = ""
                break
            else:                 #Prints an error message if the password length is not inside of the range.
                error_message = "Length on password is incorrect!"
                continue
        except:
            error_message = "Please enter a whole number between 6 and 10 or 16 for the length of your password: "
            continue

    special_character = input("Special Characters? Yes/No: ")
    if(special_character in YES_LIST):
        use_special_characters = True

    numbers = input("Use numbers? Yes/No: ")
    if(numbers in YES_LIST):                #The end user can select if he wants or not the use of numbers in their system's generated password.
        use_numbers = True                  
    else:                                   
        use_numbers = False

    # Shows back the information provided by the end user and asks them to confirm if it is correct.
    print("You entered " + first_name + " " + last_name + " " + year_born + " Password Length: " + str(password_length) + " Special Characters? " + str(use_special_characters) + " Numbers? " + str(use_numbers) + " Is this correct? ") 
    #Displays the end user choice for verification
    
    is_this_correct = input("Yes or No: ")  #Asks to end user to verify their choices

    #If the end user confirms the information, the program stores the data as a tuple and clears the variables.
    if(is_this_correct in YES_LIST):
        employee_data = (first_name, last_name, year_born, password_length, use_special_characters, use_numbers)
        all_employee_data_in_tuples_list.append(employee_data)
        first_name = ""
        last_name = ""
        year_born = ""      
        password_length = ""
        use_special_characters = False
        use_numbers = False
    else:
        #If the information provided is not confirmed by the end user, the program clears the variables and continues the loop.
        first_name = ""
        last_name = ""
        year_born = ""  
        password_length = ""
        use_special_characters = False
        use_numbers = False
        continue 
 

#Process Section

# Iterates through each employee's data to generate usernames while handling duplicates.
for employee in all_employee_data_in_tuples_list:

    # Extracts individual data factors from the employee's tuple.
    first_name = employee[0]               #Obtained first name from employee's tuple
    last_name = employee[1]                #Obtained last name from employee's tuple
    year_born = employee[2]                #Obtained year of birth from employee's tuple
    password_length = employee[3]          #Gets the desired password length from the employee data.
    use_special_characters = employee[4]   #Defines if special characters should be used in the password.
    use_numbers = employee [5]             #Defines is numbers should be included in the password.
    dups_found = False                     #Prepares a flag to track if duplicates in usernames are found.

    username = build_username(first_name,last_name,year_born,dups_found)

    #Checks if the generated username is already present in the username list.
    if username in username_list:
        dups_found = True
        username = build_username(first_name,last_name,year_born,dups_found)

    #Appends the new username to the username list.
    username_list.append(username)

    #my_employee = Employee(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]) #Creates an instance of the Employee class with employee data, generate a password, and collect employee information.
    password = build_password(password_length, use_special_characters, use_numbers)
    
    employee_record = [first_name, last_name, year_born, password]                                  #Creates a record for the employee including their name, year of birth, and generated password.

    # Stores the employee's data in the dictionary using the username as the key.
    employee_data_dictionary[username] = employee_record

    # Creates a sorted copy of the username list.
username_sorted_list = list(username_list)

username_sorted_list.sort()

try:                                         #Tries to open and write to a file named "employee_data.txt"
    with open(file_name, "w") as file:       #Writes the employee_data_dictionary as a string to the file.
        file.write(str(employee_data_dictionary))
except FileNotFoundError:                    #If the file does not exist, prints an error message.
    print(f"Sorry, the file{file_name} does not exist.")
else:
    file.close()                             #Closes the file if the write operation was successful.


#Output Section

print(getpass.getuser())                        #Prints the current user's system username for reference.
print(date.today())                             #Prints the current date to provide a timestamp for the output.
print()                                         #Space left blank for formatting purposes.
print("All employee data in tuples list:")      #Prints the message "All employee data in tuples list:"
print(all_employee_data_in_tuples_list)         #Displays the gathered employee's data in tuple format.
print("Username list:")                         #Prints the message "Username list:"
print(username_list)                            #Displays the generated list of usernames.
print("Employee data dictionary:")              #Prints the message "Employee data dictionary:"
print(employee_data_dictionary)                 #Displays the employee's data stored in the dictionary with usernames as keys.
print("Username sorted list:")                  #Prints the message "Username sorted list:"
print(username_sorted_list)                     #Displays the sorted list of usernames.