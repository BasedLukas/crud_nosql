import os

welcome = "Welcome to my stupendous CRUD app for couch db studentenfeest \n"
menu_options = ["Read","Create","Update","Delete"]
number_of_menu_options = len(menu_options)


while True:
    print(welcome)
    for key, option in enumerate(menu_options):
        print(key, option)
    print("q to quit")
    selection = input("Please select an option: ")
    if selection == "q":
        quit()
    if selection == "0":
        import read
        read.read_main_menu()
    if selection == "1":
        import create
        create.create_main_menu()
    if selection == "2":
        import update
        update.update_main_menu()
    if selection == "3":
        import delete
        delete.delete_main_menu()

    #clear terminal doesn't work in IDE's
    os.system('cls' if os.name == 'nt' else 'clear')
