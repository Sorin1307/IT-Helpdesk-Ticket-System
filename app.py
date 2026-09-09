from datetime import datetime


tickets = []


def create_ticket():
    print("\n--- Create New Ticket ---")

    title = input("Problem title: ")
    description = input("Problem description: ")
    priority = input("Priority (Low/Medium/High): ")

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Open",
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tickets.append(ticket)
    print(f"\nTicket #{ticket['id']} created successfully!")


def view_tickets():
    print("\n--- All Support Tickets ---")

    if not tickets:
        print("No tickets have been created.")
        return

    for ticket in tickets:
        print(f"\nTicket ID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Created: {ticket['created_at']}")


def update_ticket():
    view_tickets()

    if not tickets:
        return

    try:
        ticket_id = int(input("\nEnter ticket ID: "))

        for ticket in tickets:
            if ticket["id"] == ticket_id:
                new_status = input(
                    "New status (Open/In Progress/Resolved): "
                )
                ticket["status"] = new_status
                print("Ticket status updated successfully!")
                return

        print("Ticket not found.")

    except ValueError:
        print("Please enter a valid ticket ID.")


def main():
    while True:
        print("\n===== IT HELPDESK TICKET SYSTEM =====")
        print("1. Create a ticket")
        print("2. View all tickets")
        print("3. Update ticket status")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            print("Thank you for using the IT Helpdesk System.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
