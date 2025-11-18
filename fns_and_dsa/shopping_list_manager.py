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
            item_to_add = input("Enter the item to add: ").strip() # Add a single item

            if item_to_add:
                shopping_list.append(item_to_add)

                print(f"'{item_to_add}' added to the list.") # Print confirmation message
            else:
                print("Item name cannot be empty.")

        elif choice == '2':

            if not shopping_list:
                print("The shopping list is empty.") # Remove a single item
                continue

            item_to_remove = input("Enter the item to remove: ").strip()

            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                # Print removal confirmation
                print(f"'{item_to_remove}' removed from the list.")
            else:
                # Print 'not found' message as required
                print(f"'{item_to_remove}' not found in the list.")

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