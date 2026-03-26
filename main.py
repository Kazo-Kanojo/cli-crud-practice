# A simple CRUD demonstrating the FIFO (First-In, First-Out) concept.

def add_to_queue(queue):
    """Adds one or more customers to the queue."""
    while True:
        try:
            num_names = int(input("How many names do you want to add: "))
            if num_names > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(num_names):
        name = input(f"Enter the name for customer #{i + 1}: ")
        queue.append(name)
    print(f"{num_names} customer(s) added to the queue successfully.")

def list_queue(queue):
    """Lists all the customers currently in the queue."""
    if not queue:
        print("The queue is empty.")
    else:
        print("\nCurrent Queue:")
        for i in range(len(queue)):
            print(f"  {i}º: {queue[i]}")
        print()


def serve_customers(queue):
    """Serves all customers in the queue in FIFO order."""
    if not queue:
        print("The queue is empty. No one to serve.")
    else:
        print("\nServing all customers...")
        while queue:
            customer = queue.pop(0)
            print(f"\nCustomer '{customer}' has been served.")
        print("All customers have been served. The queue is now empty.")


def remove_from_queue(queue):
    """Removes a specific customer from the queue."""
    if not queue:
        print("The queue is empty. Cannot remove anyone.")
        return

    list_queue(queue)
    name_to_remove = input("Enter the name of the customer you want to remove: ")

    if name_to_remove in queue:
        queue.remove(name_to_remove)
        print(f"Customer '{name_to_remove}' was removed from the queue.")
    else:
        print(f"Customer '{name_to_remove}' was not found in the queue.")

def update_queue(queue):
    """Updates the queue based on user input."""
    if not queue:
        print("The queue is empty.")
        return
    list_queue(queue)
    name_to_update = input("Input the name of the customer you want to update: ")
    if name_to_update in queue:
        for i in range(len(queue)):
            if queue[i].lower() == name_to_update.lower():
                new_name = input("Enter the new name: ")
                queue[i] = new_name
                print(f"Customer '{name_to_update}' has been updated to '{new_name}'.")
                break
    else:
        print(f"Customer '{name_to_update}' was not found in the queue.")


def main():
    """Main function to run the queue management system."""
    queue = []
    print("Initializing the system...")
    print("Welcome! What would you like to do?")

    while True:
        print("\n--- Menu ---")
        print("1 - Add customer(s) to the queue")
        print("2 - Remove a customer from the queue")
        print("3 - Serve all customers in the queue")
        print("4 - View all customers in the queue")
        print("5 - Update a costumer")
        print("6 - Exit the system")

        try:
            reply = int(input("Enter the number for your choice: "))
            match reply:
                case 1:
                    add_to_queue(queue)
                case 2:
                    remove_from_queue(queue)
                case 3:
                    serve_customers(queue)
                case 4:
                    list_queue(queue)
                case 5:
                    update_queue(queue)
                case 6:
                    print("Exiting the system...")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
