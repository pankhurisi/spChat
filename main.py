from spy_details import spy, Spy, ChatMssg, friends
from steganography.steganography import Steganography
from termcolor import colored

# special strings
SPECIAL_MESSAGES = ['SOS','SAVE ME','HELP ME','WAR IS ON','DETECTED']

# older status messages
STATUS_MSSGS = ['Hard work pays off', 'MISSION IS ON', 'Never say never']

# print is a keyword
# print is a function
print colored('Hello !', 'red', 'on_grey')

# The other way to write the same code is
# print "Let's get started"
print colored('Let\'s get started', 'red', 'on_grey')

# continue with default user or define a new user
question = colored("Continue as " + spy.salutation + " " + spy.name, 'red', 'on_grey')

# upper() is used to convert values entered to upper case
existing = raw_input(question).upper()


# method for adding or choosing a status from old status
def add_spy_status():

    updated_status_mssge = None

    if spy.current_status_mssge != None:
        print colored('Your current status message is %s \n' % spy.current_status_mssge, 'red')
    else:
        print colored('You don\'t have any status message currently \n', 'red', 'on_grey')

    default = raw_input(colored("Do you want to select from the older status (Y/N)? ", 'red'))

    if default.upper() == "N":
        spy_new_status_message = raw_input(colored("what status message do you want to set?", 'red', 'on_grey'))

        if len(spy_new_status_message) > 0:
            if spy_new_status_message.decode('utf-8').isspace():
                updated_status_mssge = None
            else:
                STATUS_MSSGS.append(spy_new_status_message)
                updated_status_mssge = spy_new_status_message

    elif default.upper() == "Y":

        item_position = 1

        for message in STATUS_MSSGS:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        old_message_selection = int(raw_input(colored("\n Choose from the above messages ", 'red', 'on_grey')))

        if len(STATUS_MSSGS) >= old_message_selection:
            updated_status_mssge = STATUS_MSSGS[old_message_selection-1]
    else:
        print colored('The option you chose is not valid! Press either y or n.', 'red')

    if updated_status_mssge:
        print 'Your updated status message is: %s' % updated_status_mssge
    else:
        print colored('You did not update your status message', 'red')

    return updated_status_mssge


# method to print friends number
def total_spy_friend():
    if len(friends) != 0:
        item_number = 0
        print 'your friends are:'
        for friend in friends:
            print '%d. %s %s rating %d and age %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age, friend.rating)
            item_number = item_number + 1
    else:
        return
    return

# method to add a spy
def add_spy_friend():

    # Spy is a class
    new_spy_friend = Spy('', '', 0, 0.0)

    new_spy_friend.name = raw_input(colored("Please add your friend's name:", 'red'))
    new_spy_friend.salutation = raw_input(colored("Are they Mr. or Ms.?: ", 'red'))

    new_spy_friend.age = raw_input(colored("Age?", 'red'))
    new_spy_friend.age = int(new_spy_friend.age)

    new_spy_friend.rating = raw_input(colored("Spy rating?", 'red'))
    new_spy_friend.rating = float(new_spy_friend.rating)

    if len(new_spy_friend.name) > 0 and new_spy_friend.age > 12 and new_spy_friend.rating >= spy.rating:
        friends.append(new_spy_friend)
        print colored('Friend Added', 'red')
        total_spy_friend()
    else:
        print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided', 'red')

    return len(friends)


# method to remove a spy
def remove_spy_friend():

    friend_choice = select_friend()

    del friends[friend_choice]
    print "Remaining friends are:"
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age, friend.rating)
        item_number = item_number + 1

    return len(friends)


# method to select a spy
def select_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                     friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input(colored("Choose from your friends", 'red'))

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# method to send a message
def send_message():

    friend_choice = select_friend()

    original_image = raw_input(colored("What is the name of the image?", 'red'))

    output_path = "bond.jpg"

    text = raw_input(colored("What do you want to say? ", 'red'))

    try:
        Steganography.encode(original_image, output_path, text)
    except:
        print colored("Problem in encoding \n", 'red')
        return

    new_chat = ChatMssg(text,True)

    friends[friend_choice].chats.append(new_chat)

    print colored("Your secret message is safe now!", 'red', 'on_grey')


# method to read message
def read_message():

    sender = select_friend()

    output_path = raw_input(colored("Name of the file?", 'red'))

    try:
        secret_text = Steganography.decode(output_path)
    except:
        print ("not a valid message")
        return

    new_chat = ChatMssg(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "The secret message is : \n" + secret_text

    if secret_text.upper() in SPECIAL_MESSAGES:
        print "We are on our way to help you"

    if(len(secret_text.split(" "))) > 100:
        print "This spy" + friends[sender].name + "was talking too much,therefore will be deleted from the list "
        del friends[sender]


# method to read chat history
def read_chat_history():

    read_for = select_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"),'blue'),colored('Me:','red'),
                                   colored(chat.message,'grey'))
        else:
            print '[%s] %s said: %s' % (colored(chat.time.strftime("%d %B %Y"),'blue'),
                                        colored(friends[read_for].name,'red'),colored(chat.message,'grey'))


def start_chat(spy):

    # here the two strings are being joined together
    # then variable  is reassigned to spy_name after concatenation
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        # other way to write it
        # print "Authentication complete. Welcome " + spy['name']," age: ", (spy['age']), " and rating of: ",
        # str(spy['rating'])," Proud to have you on_board"
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " \
              + str(spy.rating) + " Proud to have you on_board"
        show_menu = True

        # while loop
        while show_menu:

            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. See friend \n 3. Add a friend \n " \
                           "4. remove a friend \n 5. Send a secret message \n 6. Read a secret message \n" \
                           " 7. Read Chats from a user \n 8. Close Application \n "

            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                # set status
                if menu_choice == 1:
                    spy.current_status_mssge = add_spy_status()
                elif menu_choice == 2:
                    total_spy_friend()
                elif menu_choice == 3:
                    number_of_friends = add_spy_friend()
                    print 'You have %d friends' % number_of_friends
                elif menu_choice == 4:
                    number_of_friends = remove_spy_friend()
                elif menu_choice == 5:
                    send_message()
                elif menu_choice == 6:
                    read_message()
                elif menu_choice == 7:
                    read_chat_history()
                else:
                    show_menu = False

    else:

        print colored('Sorry you are not of the correct age to be a spy', 'red')

# continue with the default user details imported
if existing == "Y":

    start_chat(spy)

else:
    # different variables are created
    # Spy is a class
    spy = Spy('', '', 0, 0.0)

    # raw_input is used to get input from user
    # spy_name is a variable used to store the name entered
    spy.name = raw_input(colored('Welcome to spy chat, you must tell me your spy name first:', 'red'))

    if len(spy.name) > 0:

        # we have used "+" sign to concat that is join the name with the message
        print 'Welcome ' + spy.name + '. Glad to have you back with us.'

        # spy_salutation is a variable
        spy.salutation = raw_input(colored("what should we call you (Mr. or Ms. ?)", 'red'))

        # raw_input always gives us a string
        spy.age = raw_input(colored("What is your age?", 'red'))

        # type conversion from string to integer
        spy.age = int(spy.age)

        spy.rating = raw_input(colored("What is your spy rating?", 'red'))

        # type conversion from string to float
        spy.rating = float(spy.rating)

        # nested if-else
        if spy.rating > 4.5:
            print colored('Great ace!', 'red')

        # other way to write
        # elif 3.5 < spy.rating <= 4.5
        elif spy.rating > 3.5 and spy.rating <= 4.5:
            print colored('You are one of the good ones.', 'red')

        # other way to write
        # elif 2.5 <= spy.rating <= 3.5
        elif spy.rating >= 2.5 and spy.rating <= 3.5:
            print colored('You can always do better', 'red')

        else:
            print colored('We can always use somebody to help in the office.', 'red')

        start_chat(spy)

    else:

        print colored('A spy needs to have a valid name. Try again please.', 'red')
