TICKET_PRICE = 10

tickets_remaining = 100

#Run this code continuously until we run out of tickets
while tickets_remaining >= 1:

    # Output how many tickets are remaining using the tickets_remaining variable

    print("There are {} tickets remaining".format(tickets_remaining))

    # Gather the users name and sign it to a new variable
    users_name = input("What is your name?  ")

    # Prompt the user by name and ask how many tickets would they like

    total_tickets = input("{} tickets are $10 how many would you like to by?  ".format(users_name))
    total_tickets = int(total_tickets)

    # Calculate the price(number of tickets multiplied by the price) and assign to a variable

    total_amount = TICKET_PRICE * total_tickets

    # Output the price on the screen
    print("Your total will be ${} ".format(total_amount) )

    #Prompt user if they want to proceed. Y/N?

    answer = input("Are you ready to purcahse those Y/N? " )

    #If they want to proceed
    if answer.lower() == "y":
        print("SOLD!!!! Thank you for the purcahse")
        #print out to the screen "SOLD!" to confirm purchease

    #and then reduce tickets remaining by tickets purcahse
        tickets_remaining -= total_tickets
        print(tickets_remaining)
    #Otherwise...
    else:
        #Thank them by name
        print("Tickets will sell out, {}".format(users_name))

#Notify user that the tickets are sold out
    print("See should have gotten some tickets sooner")
