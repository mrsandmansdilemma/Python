def display_menu(): # The main function that displays menu and handles selection.
    print("""
==========================================
 WELCOME, WHAT WOULD YOU LIKE TO DO TODAY?
==========================================
1- Display employees list
2- Assign weekly tasks 
3- Generate meeting report 
4- Display meeting report
5- Review meeting report
6- Display task summary 
0- EXIT
******************************************
""")
def ask_menu_selection(): #Menu selection function. 
    try:
        selection = int(input("Please select an option (0-6): "))
        if selection == 0:
            exit
        elif 1 <= selection and 6 >= selection:
            return selection
        else:
            print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 0 AND 6.") 
    except ValueError: # Error handling for non-integers
        print("INVALID CHOICE. PLEASE ENTER A NUMBER.")

def select_department(): # The second menu function where the user decides the department.
    print("""
==========================================
 WHAT DEPARTMENT WOULD YOU LIKE TO SELECT?
==========================================
1- Software Development
2- Artificial Intelligence
3- Research and Development
4- Quality Assurance
5- IT Operations
6- Human Resources
******************************************
""")
    try:
        department = int(input("Enter the number of your chosen department: ")) #department input 
        if department < 1 or department > 6:
            print("Invalid department number. Please enter a valid department number.")
            select_department() # Recursion for error handling. 
        else:
            return department
    except ValueError: # Error handling for non-integers.
        print("Invalid value input. Please enter a valid department number of your choice.")
        select_department()

def get_department_name(department): # This function retrieves the name of the department.
    if department == 1: 
        return "Software Development"
    elif department == 2:
        return "Artificial Intelligence"
    elif department == 3:
        return "Research and Development"
    elif department == 4:
        return "Quality Assurance"
    elif department == 5:
        return "IT Operations"
    elif department == 6:
        return "Human Resources"
def get_employee_title(id): # Helper function for meeting report generation. 
    with open("employees.txt") as file:
        for line in file: # Reading through the employees list via for loop. 
            if line.rstrip() == id:
                file.readline() # Passing insignificant lines.
                file.readline() # Passing insignificant lines.
                title = file.readline().rstrip() 
                return title # Returns employee titles. 
def get_employee_name(id): # Helper function for meeting report generation (Among other things).
    with open("employees.txt") as file: 
        for line in file: # Reading through the employees list via for loop. 
            if line.rstrip() == id: 
                name = file.readline().rstrip()
                surname = file.readline().rstrip()
                return (name + " " + surname) # Returns employee titles.
def generate_meeting_report(department):
    task_file = f"tasks_{department}.txt"             # Predefining task file for the relevant department. 
    review_file = f"review_{department}.txt"          # Predefining review file for the relevant department. 
    report_file = f"meeting_report_{department}.txt"  # Predefining meeting report file for the relevant department. 
    if not is_file_created(task_file): # Ends function call if task file is absent. 
        print("No defined tasks yet.")
        return
    if is_file_created(review_file): # The cases in which a review already exists.
        meeting_note = ""
        meeting_date = ""

        with open(review_file, 'r') as file:
            for line in file:
                if line == "Pending Approval\n" or line == "Approved\n": # Ends function call if status is pending approval or approved. 
                    print("This meeting report is already in progress.")
                    return
                elif line == "Rejected\n": # Asks for confirmation to overwrite. 
                    while True:
                        selection = input("WARNING! CONTINUING WILL OVERWRITE EXISTING REPORT DATA. Would you like to continue? [y/n]: ")
                        if selection == "y": break
                        elif selection == "n": return
                        else:
                            print("Please enter either 'y' or 'n'.")
                            continue
        with open(review_file, 'r') as read_file: # Looks up the existing review file for meeting date and notes.
            for i in range(4):
                read_file.readline()
            meeting_date = read_file.readline().rstrip()
            meeeting_note = read_file.readline().rstrip()

        with open(review_file, 'w') as file: # Creates/Rewrites the default review file.
            file.write("Pending Approval\n")
            file.write("-\n")
            file.write("-\n")
            file.write("-\n")
            file.write(meeting_date+"\n")
            file.write(meeeting_note+"\n")
        
        with open(report_file, 'w') as rep_file: # Writes the readable report file. 
            rep_file.write(f"Department: {get_department_name(department)}\n")
            rep_file.write(f"Meeting Date: {meeting_date}\n")
            rep_file.write(f"Meeting Note: {meeting_note}\n")
            rep_file.write("Status: Pending Approval\n")
            with open(task_file, 'r') as tasks: # Looks up task file for task information. 
                counter = 0
                employee_count = 0
                time_count = 0
                for line in tasks:
                    counter +=1
                    if counter % 4 == 1:
                        employee_count += 1
                        id = line.rstrip()
                        rep_file.write(f"Employee ID: {id}\n")
                        rep_file.write(f"Employee Name: {get_employee_name(id)}\n")
                        rep_file.write(f"Employee Title: {get_employee_title(id)}\n")
                    if counter % 4 == 2: rep_file.write(f"Task: {line.rstrip()}\n")
                    if counter % 4 == 3:
                        rep_file.write(f"Estimated Time: {line.rstrip()}\n")
                        time_count += int(line.rstrip())
                rep_file.write(f"Number of Employees: {employee_count}\n")
                rep_file.write(f"Total Estimated Time: {time_count} hrs\n")
                rep_file.write(f"Average Time: {(time_count / employee_count):.2f} hrs\n")
                rep_file.write("Reviewer ID: -\n")
                rep_file.write(f"Reviewer Name: -\n")
                rep_file.write(f"Reviewer Comment: -\n")

    else: # The case without a pre-existing meeting report.  
        while True:
            meeting_date = input("Please enter your meeting date: ") # Asks for input regarding the meeting date. While loop used for error handling. 
            if meeting_date == "":
                print("Please enter your meeting date.")
                continue
            else: break
        while True:
            meeting_note = input("Please enter your meeting note: ") # Asks for input regarding meeting notes. While loop used for error handling. 
            if meeting_note == "":
                print("Please enter your meeting note.")
                continue
            else: break
        with open(review_file, 'w') as file: # Creates the default review file. 
            file.write("Pending Approval\n")
            file.write("-\n")
            file.write("-\n")
            file.write("-\n")
            file.write(meeting_date+"\n")
            file.write(meeting_note+"\n")
        with open(report_file, 'w') as rep_file: # Creates meeting report. 
            rep_file.write(f"Department: {get_department_name(department)}\n")
            rep_file.write(f"Meeting Date: {meeting_date}\n")
            rep_file.write(f"Meeting Note: {meeting_note}\n")
            rep_file.write("Status: Pending Approval\n")
            with open(task_file, 'r') as tasks: # Open and look up task file for tasks information. Writes available information into meeting report. 
                counter = 0
                employee_count = 0
                time_count = 0
                for line in tasks:
                    counter +=1
                    if counter % 4 == 1:
                        employee_count += 1
                        id = line.rstrip()
                        rep_file.write(f"Employee ID: {id}\n")
                        rep_file.write(f"Employee Name: {get_employee_name(id)}\n")
                        rep_file.write(f"Employee Title: {get_employee_title(id)}\n")
                    if counter % 4 == 2: rep_file.write(f"Task: {line.rstrip()}\n")
                    if counter % 4 == 3:
                        rep_file.write(f"Estimated Time: {line.rstrip()}\n")
                        time_count += int(line.rstrip())
                rep_file.write(f"Number of Employees: {employee_count}\n")
                rep_file.write(f"Total Estimated Time: {time_count} hrs\n")
                rep_file.write(f"Average Time: {(time_count / employee_count):.2f} hrs\n")
                rep_file.write("Reviewer ID: -\n")
                rep_file.write(f"Reviewer Name: -\n")
                rep_file.write(f"Reviewer Comment: -\n")
              
def display_meeting_report(department): # Displays the meeting report for the selected department.
    filename = f"meeting_report_{department}.txt" # Constructs the target report filename using the department number.
    try: 
        with open(filename, 'r') as file: # Opens the report file in read mode.
            report_content = file.read() # Reads the entire content of the file.
            print(f"Meeting Report for {get_department_name(department)}:\n")
            print(report_content) # Prints the full content of the meeting report.
    except FileNotFoundError: 
        print(f"No meeting report found for {get_department_name(department)}.") # Informs the user that no report was found.
        display_menu() # Displays the main menu again.

def authenticate_manager(manager_id, password, department): # Authenticates the manager based on their ID, password, and department.
    try:
        manager_id = int(manager_id) # Converts user input ID to integer; jumps to except if non-numeric
    except ValueError:
        print("Invalid credentials. Please try again.")
        return False

    password_valid = False # Initializes a flag to track password validity.
    with open('manager_passwords.txt', 'r') as file: # Opens the manager passwords file in read mode.
        emp_id = file.readline() 
        while emp_id != "": # Loops until the end of the file.
            emp_id = int(emp_id.rstrip()) # Cleans and converts the ID to int inside the loop.
            manager_pass = file.readline().rstrip() # Reads and strips the password.
            file.readline() # Skip the empty line.
            
            if emp_id == manager_id and password == manager_pass: # Checks credentials inside the loop for every manager.
                password_valid = True # Sets the flag to True if the credentials match.
                break 
                
            emp_id = file.readline() # Reads the next manager ID to advance the loop.

    if not password_valid:
        print("Invalid credentials. Please try again.")
        return False

    # 2. Check if this ID is actually the Manager of the selected department in employees.txt
    target_department = get_department_name(department)
    with open('employees.txt', 'r') as emp_file:
        file_emp_id = emp_file.readline()
        while file_emp_id != "":
            file_emp_id = int(file_emp_id.rstrip())
            emp_name = emp_file.readline().rstrip()
            emp_surname = emp_file.readline().rstrip()
            emp_role = emp_file.readline().rstrip()
            emp_dept = emp_file.readline().rstrip()
            emp_rank = emp_file.readline().rstrip()
            emp_file.readline() # Skip the empty line (remove if employees.txt has no empty lines)

            if file_emp_id == manager_id and emp_rank == "Manager" and emp_dept == target_department:
                return True

            file_emp_id = emp_file.readline()

    print("Invalid credentials. Please try again.")
    return False
    
def review_meeting_report(department): # Handles login attempts, decision input, and report updates
    report_filename = f"meeting_report_{department}.txt" 
    review_filename = f"review_{department}.txt" 

    # 1. Require an existing report before asking for credentials and check its status
    try: # Checks if review_N.txt and meeting_report_N.txt exist
        with open(report_filename, "r") as rep_check: # Ensures report file exists
            pass
        with open(review_filename, "r") as rev_file: # Reads persistent metadata from review_N.txt
            current_status = rev_file.readline().strip() # Line 1: Status
            rev_id = rev_file.readline().strip() # Line 2: Reviewer ID
            rev_name = rev_file.readline().strip() # Line 3: Reviewer full name
            rev_comment = rev_file.readline().strip() # Line 4: Review comment
            meeting_date = rev_file.readline().strip() # Line 5: Meeting date (must be preserved)
            meeting_note = rev_file.readline().strip() # Line 6: Meeting note (must be preserved)
    except FileNotFoundError: # Handles missing report condition
        print(f"No meeting report exists for {get_department_name(department)}.") # Informs user
        return

    # Only reports with status Pending Approval can be reviewed
    if current_status != "Pending Approval": # Checks if already Approved or Rejected
        print(f"This report has already been reviewed. Current status: {current_status}") # Displays current status
        return 

    # 2. Allow at most three login attempts
    attempts = 0 # Tracks failed attempts
    authenticated = False # Flag for successful login
    valid_manager_id = "" # Stores authenticated manager ID

    while attempts < 3: # Maximum 3 attempts allowed
        manager_id = input("Enter Manager ID: ").strip() # Prompts for manager ID
        password = input("Enter Password: ").strip() # Prompts for password

        if authenticate_manager(manager_id, password, department): # Validates credentials and department
            authenticated = True # Marks authentication successful
            valid_manager_id = manager_id # Stores valid manager ID
            break # Exits login loop
        else: # Handles failed authentication
            attempts += 1 # Increments failure counter
            print("Invalid manager ID or password, or unauthorized department.") # Exact error message required by PDF

    if not authenticated: # Checks if all 3 attempts failed
        print("Maximum login attempts reached. Returning to main menu.") # Informs user
        return # Returns to main menu

    # 3. Display the report and offer Approve, Reject, and Cancel
    display_meeting_report(department) # Displays current report

    while True: # Loops until valid decision is entered
        decision = input("Enter your decision (Approve / Reject / Cancel): ").strip() # Prompts decision
        if decision == "Approve" or decision == "approve": # Checks Approve
            decision = "Approve" # Standardizes value
            break # Exits loop
        elif decision == "Reject" or decision == "reject": # Checks Reject
            decision = "Reject" # Standardizes value
            break # Exits loop
        elif decision == "Cancel" or decision == "cancel": # Checks Cancel
            decision = "Cancel" # Standardizes value
            break # Exits loop
        else: # Rejects invalid choice
            print("Invalid choice. Please enter Approve, Reject, or Cancel.") # Prompts again

    if decision == "Cancel": # Preserves current decision and returns
        print("Review cancelled. Current status preserved.") # Informs user
        return # Returns to main menu

    # 4. Collect comment (optional for Approve, required for Reject)
    if decision == "Approve": # Approval comment is optional
        comment = input("Enter approval comment (optional, press Enter to skip): ").strip() # Prompts comment
        if comment == "": # Stores a hyphen if blank
            comment = "-"
        new_status = "Approved" # Sets new status
    else: # Rejection comment is required and must not be empty
        while True: # Keeps asking until a nonempty rejection comment is entered
            comment = input("Enter rejection comment (required): ").strip() # Prompts required comment
            if comment != "": # Validates non-empty comment
                break # Exits loop
            print("Rejection comment cannot be empty. Please enter a comment.") # Rejects blank input
        new_status = "Rejected" # Sets new status

    # 5. Retrieve manager's full name from employees.txt
    manager_full_name = "" # Stores manager's full name
    with open("employees.txt", "r") as emp_file: # Opens employees file
        emp_id = emp_file.readline() # Reads Employee ID
        while emp_id != "": # Loops until end of file
            emp_id = emp_id.strip() # Strips whitespace
            emp_name = emp_file.readline().strip() # Reads Name
            emp_surname = emp_file.readline().strip() # Reads Surname
            emp_title = emp_file.readline().strip() # Reads Title
            emp_dept = emp_file.readline().strip() # Reads Department
            emp_role = emp_file.readline().strip() # Reads Role
            emp_file.readline() # Skips empty line

            if emp_id == str(valid_manager_id): # Matches manager ID
                manager_full_name = f"{emp_name} {emp_surname}" # Builds full name
                break # Exits loop

            emp_id = emp_file.readline() # Reads next Employee ID

    # 6. Save updated decision in review_N.txt (preserving meeting date and note)
    with open(review_filename, "w") as rev_file: # Overwrites review_N.txt with 6 exact lines
        rev_file.write(f"{new_status}\n") # Line 1: Status
        rev_file.write(f"{valid_manager_id}\n") # Line 2: Reviewer ID
        rev_file.write(f"{manager_full_name}\n") # Line 3: Reviewer full name
        rev_file.write(f"{comment}\n") # Line 4: Review comment
        rev_file.write(f"{meeting_date}\n") # Line 5: Preserved meeting date
        rev_file.write(f"{meeting_note}\n") # Line 6: Preserved meeting note

    # 7. Rebuild meeting_report_N.txt with the new decision
    temp_filename = f"temp_report_{department}.txt" # Temporary file to hold updated lines

    with open(report_filename, "r") as rep_file, open(temp_filename, "w") as temp_file:
        line = rep_file.readline() # Reads first line
        while line != "": # Loops until end of file
            if line.strip() == "Status: Pending Approval":
                temp_file.write(f"Status: {new_status}\n") # Writes updated status
            elif line.strip() == "Reviewer ID: -":
                temp_file.write(f"Reviewer ID: {valid_manager_id}\n") # Writes reviewer ID
            elif line.strip() == "Reviewer Name: -":
                temp_file.write(f"Reviewer Name: {manager_full_name}\n") # Writes reviewer name
            elif line.strip() == "Review Comment: -":
                temp_file.write(f"Review Comment: {comment}\n") # Writes review comment
            else:
                temp_file.write(line) # Copies original line directly
            line = rep_file.readline() # Reads next line

    # Copy updated content back into meeting_report_N.txt
    with open(temp_filename, "r") as temp_file, open(report_filename, "w") as rep_file:
        line = temp_file.readline()
        while line != "":
            rep_file.write(line)
            line = temp_file.readline()
def is_file_created(file): # Helper function for general usage. Checks if a file is created. 
    try:
        with open(file, 'r') as checkfile:
            return True # Returns true if file can be opened without issues. 
    except FileNotFoundError:
        return False # Returns false if the read function raises a FileNotFoundError. 
def assign_weekly_tasks(department): # Assigns weekly tasks to the entirety of a department's employees.
    task_file = f"tasks_{department}.txt" # Preassigns task file per department's code. 
    rev_file = f"review_{department}.txt" # Preassigns review file per department's code. 
    if is_file_created(task_file): # Checks if there already is a task file and then whether the relevant meeting report has been rejected. 
        with open(rev_file, 'r') as review_file:
            status = review_file.readline().rstrip() # Extracts status from review file. 
            while True:
                if status == "Rejected": # Asks for confirmation regarding overwrite if the relevant meeting report has been rejected. 
                    selection = input("WARNING! CONTINUING THIS OPERATION WILL OVERWRITE EXISTING TASK DATA. Would you like to continue? [y/n]: ")
                    if selection == "y":
                        with open(task_file, 'w') as file:
                            file.write("")
                            break
                    elif selection == "n": return
                    else:
                        print("Please enter either 'y' or 'n'.")
                        continue
                else: return


    department_name = get_department_name(department) # Assigns string variable as the relevant department's name. 
    with open('employees.txt', 'r') as emp_file: # Looks up employees to assign tasks to. 
        for i in range(50):
            id = emp_file.readline().rstrip()
            emp_name = emp_file.readline().rstrip()
            emp_surname = emp_file.readline().rstrip()
            emp_role = emp_file.readline().rstrip()
            emp_dept = emp_file.readline().rstrip()
            emp_file.readline()
            emp_file.readline()
            if emp_dept == department_name: # Assigns tasks to only employees of the relevant department. 
                print(f"""
Assign task for 
ID: {id}
Name: {emp_name} {emp_surname}
Role: {emp_role}                                         
""")
                with open(task_file, 'a+') as file: # Open text file for task input. 
                    while True:
                        task_desc = input("Please describe the task you'd like to assign: ")
                        if task_desc == "": # Looks for and rejects empty task descriptions. 
                            print("Please provide a description of the task.")
                            continue
                        try:
                            estimated_time = int(input("Please enter the estimated time for this task (1-40): "))  # Asks user for estimated time. 
                            if estimated_time > 40 or estimated_time < 1: # Rejects invalid inputs. 
                                print("Please provide a valid estimated time for this task.")
                                continue
                            else:
                                file.write(f"{id}\n") # Inputs employee ID in task file.
                                file.write(task_desc + "\n")  # Inputs task description in task file. 
                                file.write(f"{estimated_time}\n") # Inputs estimated time in task file.
                                file.write("\n") # Blank line separator 
                                break
                        except ValueError: # Rejects invalid inputs. 
                            print("Please provide a valid estimated time for this task.")
                            continue
def display_task_summary(department): # Displays task summary.
    task_file = f"tasks_{department}.txt" # Preassigns task file for relevant department. 
    counter = 0 # Total lines counter
    employee_count = 0 # Employee counter
    tasks_count = 0 # Task counter 
    total_hours = 0 # Total hours counter
    if is_file_created(task_file): # Reads task file only if it has been created, otherwise displays default blank task file info. 
        with open(task_file, 'r') as file:
            for line in file:
                counter += 1
                if counter % 4 == 1:
                    employee_count += 1
                elif counter % 4 == 2:
                    tasks_count += 1
                elif counter % 4 == 3:
                    total_hours += int(line)
            average = total_hours / tasks_count
    else:
        employee_count = 0
        tasks_count = 0
        total_hours = 0
        average = "N/A"

    print(f"""
Number of employees: {employee_count}
Number of assigned tasks: {tasks_count}
Total estimated hours: {total_hours}
Average hours per assigned task: {average}
""")


def display_employees(department): # Display employees per department. 
    department_name = get_department_name(department) # Assigns the literal name of the department to department_name. 
    print(f"Employees in {department_name} Department:") 
    with open('employees.txt', 'r') as emp_file:
        for i in range(50): # Checks employee file per individual employee. 
            id = emp_file.readline().rstrip()
            emp_name = emp_file.readline().rstrip()
            emp_surname = emp_file.readline().rstrip()
            emp_role = emp_file.readline().rstrip()
            emp_dept = emp_file.readline().rstrip()
            emp_rank = emp_file.readline().rstrip()
            emp_file.readline()  # Skip the empty line
            if emp_dept == department_name: # Displays only employees of the relevant department. 
                print(f"""
Employee ID: {id}
Employee Name: {emp_name} {emp_surname}
Employee Role: {emp_role}
Employee Rank: {emp_rank}

""")

def main(): # main function 
    while True: # main loop 
        display_menu() 
        while True: # Ensures correct input on menu selection. 
            selection = ask_menu_selection()
            if selection == None:
                continue
            else: break
        if selection == 0:
            print("Exiting the program. Goodbye!")
            break
        elif selection == 1: ## Department display events should be here. 
            department = select_department()
            display_employees(department)
        elif selection == 2: ## Task system assignation events should be here.
            department = select_department()
            assign_weekly_tasks(department)
        elif selection == 3: ## Meeting report generation events should be here.
            department = select_department()
            generate_meeting_report(department)
        elif selection == 4: ## Meeting report display events should be here.
            department = select_department()
            display_meeting_report(department)
        elif selection == 5: ## Meeting report review events should be here.
            department = select_department()
            review_meeting_report(department)
        elif selection == 6: ## Task summary display events should be here.
            department = select_department()
            display_task_summary(department)
main()