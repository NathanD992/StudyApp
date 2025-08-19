import time
import sys
from datetime import datetime
from prettytable import PrettyTable

QUIZZES = {
    "english": [
        {"question": "What is the synonym of 'happy'?", "answer": "Joyful", "choices": ["Sad", "Angry", "Tired", "Joyful"]},
        {"question": "What is the antonym of 'cold'?", "answer": "Hot", "choices": ["Chilly", "Frozen", "Hot", "Green"]},
        {"question": "Fill in the blank: She ___ to the store yesterday.", "answer": "Went", "choices": ["Goed", "Went", "Was", "Walk"]},
        {"question": "What is the plural of 'child'?", "answer": "Children", "choices": ["Childs", "Chillies", "Children", "Childer"]},
        {"question": "Which word is a noun: quickly, apple, run?", "answer": "Apple", "choices": ["Quickly", "Apple", "Run"]}
    ],
    "chemistry": [
        {"question": "What is the chemical symbol for water?", "answer": "H2O", "choices": ["CO2", "O2", "H2O", "NaCl"]},
        {"question": "What is the atomic number of Carbon?", "answer": "6", "choices": ["12", "6", "8", "14"]},
        {"question": "Which acid is found in lemons?", "answer": "Citric", "choices": ["Sulfuric", "Citric", "Hydrochloric", "Acetic"]},
        {"question": "What is the pH of a neutral solution?", "answer": "7", "choices": ["1", "7", "14", "0"]},
        {"question": "Which element is a noble gas?", "answer": "Neon", "choices": ["Oxygen", "Neon", "Nitrogen", "Carbon"]}
    ],
    "maths": [
        {"question": "What is 7 + 5?", "answer": "12", "choices": ["10", "11", "12", "13"]},
        {"question": "What is the square root of 81?", "answer": "9", "choices": ["8", "9", "10", "7"]},
        {"question": "What is 15 divided by 3?", "answer": "5", "choices": ["3", "4", "5", "6"]},
        {"question": "What is the value of pi (to 2 decimal places)?", "answer": "3.14", "choices": ["3.13", "3.14", "3.15", "3.16"]},
        {"question": "What is 6 x 7?", "answer": "42", "choices": ["36", "42", "48", "40"]}
    ]
}

ITEMS = {
    "avatar_decorations": [
        {"name": "Cool Glasses", "cost": 20, "description": "A pair of stylish sunglasses for your avatar."},
        {"name": "Wizard Hat", "cost": 30, "description": "A magical hat to make your avatar look wise."},
        {"name": "Golden Crown", "cost": 50, "description": "A shiny crown for a royal look."},
        {"name": "Rainbow Scarf", "cost": 25, "description": "A colorful scarf to brighten up your avatar."},
        {"name": "Headphones", "cost": 15, "description": "Trendy headphones for a music lover vibe."}
    ],
    "power_ups": [
        {"name": "Repair Streak", "cost": 50, "description": "Repairs a lost streak if used within 7 days of loss."},
        {"name": "Streak Protection", "cost": 70, "description": "Keeps your streak active if lost."}
    ],
    "premium_sub": [
        {"name": "1 Week Premium", "cost": 300, "description": "Gives the user Premium for 1 week"},
        {"name": "1 Month Premium", "cost": 1100, "description": "Gives the user Premium for 1 month"},
        {"name": "1 Year Premium", "cost": 13000, "description": "Gives the user Premium for 1 year"},
    ],
}

ALLSCHEDULE = []

TODAYSCHEDULE = []

coins = 0
inventory = []
premium = False
crtime = datetime.now().strftime('%Y-%m-%d %H:%S')

def inventoryList():
    print("\n" + "="*30)
    print("        INVENTORY")
    print("="*30 + "\n")
    time.sleep(0.5)
    if not inventory:
        print("Your inventory is empty!\n")
    else:
        table = PrettyTable()
        table.field_names = ["Item #", "Name", "Description", "Cost"]
        for idx, item in enumerate(inventory, 1):
            item_details = next((i for i in ITEMS['avatar_decorations'] if i['name'] == item), None)
            if item_details:
                table.add_row([idx, item_details['name'], item_details['description'], item_details['cost']])
            else:
                table.add_row([idx, item, "", ""])
        print(table)
    time.sleep(1)
    print()

def ask_questions(questions):
    global coins
    score = 0
    coins_earned = 0
    for idx, q in enumerate(questions, 1):
        print("\n" + "="*40)
        print(f"Question {idx}: {q['question']}")
        print("="*40 + "\n")
        table = PrettyTable()
        table.field_names = ["Choice #", "Option"]
        for i, choice in enumerate(q["choices"], 1):
            table.add_row([i, choice])
        print(table)
        time.sleep(0.5)
        while True:
            ans = input("Enter the choice number: ").strip()
            if ans.isdigit() and 1 <= int(ans) <= len(q["choices"]):
                selected = q["choices"][int(ans)-1]
                if selected.lower() == q["answer"].lower():
                    print("✅ Correct!\n")
                    score += 1
                    coins_earned += 5
                else:
                    print(f"❌ Incorrect. The answer is '{q['answer']}'.\n")
                time.sleep(1)
                break
            else:
                print("Error, Invalid Choice! Please enter a valid number.\n")
    coins += coins_earned
    print("\n" + "="*40)
    print(f"Quiz finished!\nYour score: {score}/{len(questions)}\nCoins Earned: {coins_earned}\nTotal Coins: {coins}")
    print("="*40 + "\n")
    time.sleep(2)

def dev_menu():
    global coins
    inP = input("Enter Command: ")
    if 'coin' in inP:
        amount = int(input("How many coins: "))
        coins += amount

def shop_menu():
    global inventory
    global coins
    print("\n" + "="*30)
    print("           SHOP")
    print("="*30)
    choice = input("Select a market to visit: \n1. Avatar Decoration\n2. Power-Ups\n3. Add coins (development purposes)\n4. Open Inventory\nSelect an option: ").lower()
    if choice == "1" or "avatar" in choice:
        avatar_shop(ITEMS)
    elif choice == "2" or "power" in choice:
        powerup_shop(ITEMS)
    elif choice == '3' or 'add' in choice:
        addC = float(input('How many coins would you like to add? '))
        coins += addC
    elif choice == '4' or 'inve' in choice:
        inventoryList()

def powerup_shop(items):
    global inventory
    global coins
    print("\n" + "="*30)
    print("           POWER-UPS SHOP")
    print("="*30)
    time.sleep(0.5)
    table = PrettyTable()
    table.field_names = ["#","Name","Cost","Description"]
    for idx, i in enumerate(items['power_ups'],1):
        table.add_row([idx,i['name'],i["cost"],i["description"]])
    print(table)
    print(f'Your Coins: {coins}')
    choice = input("Enter the number or name of the time you'd like to buy, or enter 'return' to exit: ").lower()
    found = False
    if choice.isdigit():
        idx = int(choice)-1
        if 0 <= idx < len(items["power_ups"]):
            item = items["power_ups"][idx]
            if coins >= item["cost"]:
                coins -= item["cost"]
                print(f"You bought {item['name']}! Remaining coins: {coins}")
                inventory.append(item['name'])
            else:
                print("Not enough coins!")
                found = True
        if not found:
            print("Invalid item choice (number).")
    elif choice.isalpha():
        if 'return' in choice:
            print('Returning to main menu.')
        else:
            for item in items["power_ups"]:
                if choice in item["name"].lower():
                    if coins >= item["cost"]:
                        coins -= item["cost"]
                        print(f"You bought {item['name']} for {item['cost']} coins! Remaining coins: {coins}")
                        inventory.append(item['name'])
                    else:
                        print("Not enough coins!")
                        found = True
            if not found:
                print("Invalid item choice (name).")

def avatar_shop(items):
    global inventory
    global coins
    print("\n" + "="*30)
    print("           AVATAR DECORATIONS SHOP")
    print("="*30)
    time.sleep(0.5)
    table = PrettyTable()
    table.field_names = ["#", "Name", "Cost", "Description"]
    for idx, i in enumerate(items["avatar_decorations"], 1):
        table.add_row([idx, i['name'], i['cost'], i['description']])
    print(table)
    print(f"Your Coins: {coins}")
    choice = input("Enter the number or name of the time you'd like to buy, or enter 'return' to exit: ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(items["avatar_decorations"]):
            item = items["avatar_decorations"][idx]
            if coins >= item["cost"]:
                coins -= item["cost"]
                print(f"You bought {item['name']}! Remaining coins: {coins}")
                inventory.append(item['name'])
            else:
                print("Not enough coins!")
        else:
            print("Invalid item number.")
    elif choice.isalpha():
        if 'return' in choice.lower():
            print("Returning to main menu.")
        else:
            found = False
            for item in items["avatar_decorations"]:
                if choice.lower() in item["name"].lower():
                    if coins >= item["cost"]:
                        coins -= item["cost"]
                        print(f"You bought {item['name']} for {item['cost']} coins! Remaining coins: {coins}")
                        inventory.append(item['name'])
                        found = True
                        break
                    else:
                        print("Not enough coins!")
                        found = True
            if not found:
                print("Invalid item choice (name).")
    else:
        print("Invalid input.")
    time.sleep(1.5)


# while True:
#     sys.stdout.write('\r' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     sys.stdout.flush()
#     time.sleep(1)
    

def todays_plan():
    global TODAYSCHEDULE
    print('\n' + "="*40)
    print("Today's Plan")
    print("="*40 + '\n')
    time.sleep(0.5)
    if not TODAYSCHEDULE:
        print("Nothing on today.\n")
    else:
        print("Today's Plan:\n")
        table = PrettyTable()
        table.field_names = ['#','Title','Due Date','Days left']
        for idx, item in enumerate(TODAYSCHEDULE,1):
            try:
                due_date = datetime.strptime(item['due'], "%d-%m-%Y").date()
                now = datetime.now().date()
                duein = (due_date - now).days
                if duein > 0:
                    time_left = f'{duein} days left'
                elif duein == 0:
                    time_left = "Due today!"
                elif duein < 0:
                    time_left = f"Overdue by {-duein} days!"
            except Exception:
                time_left = 'Invalid date.'
            table.add_row([idx,item['title'],item['due'],time_left])
        print(table)
    print('\nWould you like to add/remove a task to your schedule? (y/n)')
    add = input("")
    print('\n')
    time.sleep(0.5)
    if 'y' in add:
        addorremove = input("Would you like to add or remove a task? (add/remove): ").strip().lower()
        print()
        time.sleep(0.5)
        if 're' in addorremove:
            if not TODAYSCHEDULE:
                print("Nothing to remove.\n")
            else:
                print("Current Tasks:\n")
                table = PrettyTable()
                table.field_names = ['#', 'Title', 'Due Date']
                for idx, item in enumerate(TODAYSCHEDULE, 1):
                    table.add_row([idx, item['title'], item['due']])
                print(table)
                print()
                while True:
                    try:
                        task_num = int(input("Enter the task number to remove: ")) - 1
                        if 0 <= task_num < len(TODAYSCHEDULE):
                            removed_task = TODAYSCHEDULE.pop(task_num)
                            print(f"Removed task: {removed_task['title']}\n")
                            time.sleep(0.5)
                            break
                        else:
                            print("Invalid task number. Please try again.\n")
                    except ValueError:
                        print("Please enter a valid number.\n")
        elif 'ad' in addorremove:
            title = input("Enter Task Name: ")
            print()
            while True:
                duedate = input("Enter due date (e.g 14-08-2025): ")
                try:
                    datetime.strptime(duedate, "%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid date format! Please enter in DD-MM-YYYY format.\n")
            TODAYSCHEDULE.append({"title": title,"due":duedate})
            print(f"Added {title} to your schedule, due on {duedate}\n")
            time.sleep(1)
        else:
            print("Invalid choice. Returning to main menu.\n")
            time.sleep(0.5)

def home_screen():
    global coins
    print('\n' + "="*40)
    print('Home')
    print("="*40 + '\n')
    time.sleep(1)
    choice = input("What would you like to view: \n1. Today's Plan\nEnter Choice: ").lower()
    print()
    time.sleep(0.5)
    if choice == '1' or 'today' in choice:
        todays_plan()
    

def main():
    global coins
    print("\n" + "="*40)
    print("         Welcome to StudyApp!")
    print("="*40 + "\n")
    time.sleep(1)
    while True:
        print("\n" + "="*40)
        print("1. Home\n2. Quizzes\n3. Shop\n4. Inventory\nType 'quit' to exit.")
        print("="*40 + "\n")
        goto = input("Which page would you like to visit? ").strip().lower()
        print()
        time.sleep(0.5)
        if goto == "2" or goto == "quizzes":
            quiz_menu()
        elif goto == "3" or goto == "shop":
            shop_menu()
        elif goto == "4" or goto == "inventory":
            inventoryList()
        elif goto == "1" or 'home' in goto:
            home_screen()
        elif goto == "quit":
            print("Goodbye!\n")
            time.sleep(1)
            break
        elif "dev" in goto:
            dev_menu()
        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)

def quiz_menu():
    print("\n" + "="*30)
    print("         SUBJECTS")
    print("="*30 + "\n")
    table = PrettyTable()
    table.field_names = ["Subject"]
    for subject in QUIZZES.keys():
        table.add_row([subject.capitalize()])
    print(table)
    print(f"Your Coins: {coins}\n")
    time.sleep(0.5)
    while True:
        choice = input("Type a subject or 'return' to exit: ").strip().lower()
        print()
        time.sleep(0.5)
        if choice == "return":
            print("Returning to main menu.\n")
            time.sleep(1)
            break
        elif choice in QUIZZES:
            ask_questions(QUIZZES[choice])
        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)

if __name__ == "__main__":
    try:
        from prettytable import PrettyTable
    except ImportError:
        print("Please install the 'prettytable' package to use this app: pip install prettytable")
    else:
        main()