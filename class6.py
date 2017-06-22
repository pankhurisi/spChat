from spy_details import spy

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends = []

print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
existing = raw_input(question)


def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if current_status_message:
        print 'Your updated status message is: %s' % (current_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input("Age?")
    new_friend['age'] = int(new_friend['age'])

    new_friend['rating'] = raw_input("Spy rating?")
    new_friend['rating'] = float(new_friend['rating'])

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend['name'],
                                                             friend['age'],
                                                             friend['rating'])
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def start_chat(spy):
    current_status_message = None

    spy['name'] = spy['salutation'] + " " + spy['name']

    if spy['age'] > 12 and spy['age'] < 50:

        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(
            spy['rating']) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n " \
                           "3. Select a Friend \n 4. Send a secret message \n 5. Read a secret message \n " \
                           "6. Read Chats from a user \n 7. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                # Set status
                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    index = select_friend()
                    print index
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing == "Y":
    start_chat(spy)
else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

        spy['age'] = raw_input("What is your age?")
        spy['age'] = int(spy['age'])

        spy['rating'] = raw_input("What is your spy rating?")
        spy['rating'] = float(spy['rating'])

        spy['is_online'] = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'