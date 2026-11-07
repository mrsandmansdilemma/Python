def display_menu(): # The main function that displays menu and handles selection.
    print("""
==========================================
 WELCOME, WHAT WOULD YOU LIKE TO DO TODAY?
==========================================
1- Display department employees
2- Assign weekly tasks 
3- Generate meeting report 
4- Display meeting report
5- Review meeting report
6- Display task summary 
0- EXIT
******************************************
""")
def ask_menu_selection():
    try:
        selection = int(input("Please select an option (0-6): "))
        if selection == 0:
            exit
        elif 1 <= selection and 6 >= selection:
            return selection
        else:
            print("INVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 0 AND 6.") 
            ask_menu_selection()
    except ValueError:
        print("INVALID CHOICE. PLEASE ENTER A NUMBER.")
        ask_menu_selection()

def main():
    display_menu
    selection = ask_menu_selection
    if selection == 1: ## Department display events should be here. 
        pass
    elif selection == 2: ## Task system assignation events should be here.
        pass
    elif selection == 3: ## Meeting report generation events should be here.
        pass
    elif selection == 4: ## Meeting report display events should be here.
        pass
    elif selection == 5: ## Meeting report review events should be here.
        pass
    elif selection == 6: ## Task summary display events should be here.
        pass