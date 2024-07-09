# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.


service_tickets = {
    1: {"customer_name": "Aria Gabriel", "issue_description": "I have an error code", "status": "open"},
    2: {"customer_name": "Brooke Bear", "issue_description": "My account is locked", "status": "closed"},
    3: {"customer_name": "Mom Gabriel", "issue_description": "I am not getting updates", "status": "open"}
}



def open_ticket():
    ticket_id = len(service_tickets) + 1
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    status = "open"
    service_tickets[ticket_id] = {"customer_name": customer_name, "issue_description": issue_description, "status": status}
    print(f"Ticket {ticket_id} opened for {customer_name}.")

def update_ticket():
    ticket_id = int(input("Enter ticket ID: "))
    if ticket_id in service_tickets:
        status = input("Enter new status (open/closed): ")
        service_tickets[ticket_id]["status"] = status
        print(f"Ticket {ticket_id} updated.")
    else:
        print("Ticket not found.")

def display_tickets():
    status = input("Enter status to filter by (open/closed/all): ")
    for ticket_id, ticket in service_tickets.items():
        if status == "all" or ticket["status"] == status:
            print(f"Ticket ID: {ticket_id}, Customer Name: {ticket['customer_name']}, Issue Description: {ticket['issue_description']}, Status: {ticket['status']}")

def main():
    while True:
        print("1. Open Ticket")
        print("2. Update Ticket")
        print("3. Display Tickets")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            open_ticket()
        elif choice == "2":
            update_ticket()
        elif choice == "3":
            display_tickets()
        elif choice == "4":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":

    main()

