# this script 'shopping_list_manager.py' will accept items and store them ready for viewing by the user --> additional functions are the ability to remove/add multiple items at a time

def display_menu():
    """Prints the main menu options to the console."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # add item(s)
            item_to_add = input("Enter the item to add (use commas for multiple items): ").strip().lower()

            # support multiple entries to shopping list
            items = [i.strip() for i in item_to_add.split(",") if i.strip()]

            if items:
                for item in items:
                    if item in shopping_list:
                        print(f"{item} already exists in the list") # duplicate prevention added here
                    else:
                        shopping_list.append(item)
                        print(f"{item} added to the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            # remove item(s)
            if not shopping_list:
                print("The shopping list is already empty.")
                continue
            
            item_to_remove = input("Enter the items to remove (use commas for multiple items): ").strip().lower()
            
            # support multiple deletions in shopping list
            items = [i.strip() for i in item_to_remove.split(",") if i.strip()]

            removed = []
            not_found = []

            for item in items: # check if the item is in the list before attempting removal
                if item in shopping_list:
                    shopping_list.remove(item)
                    removed.append(item)
                else:
                    not_found.append(item)
            
            if removed:
                print(f"{', '.join(removed)} removed from the list.")
            if not_found:
                print(f"{', '.join(not_found)} not found in the list.")
                
        elif choice == '3':
            # view List
            if shopping_list:
                print("\nYour Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty!")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()