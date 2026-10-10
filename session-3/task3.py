def book_movie_ticket(tickets):
    wallet_balance = 1000

    try:
        tickets = int(tickets)
        price_per_ticket = wallet_balance / tickets
        print("Price per ticket:", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero.")

    except ValueError:
        print("Error: Please enter a valid number.")


tickets = input("Enter number of tickets: ")
book_movie_ticket(tickets)