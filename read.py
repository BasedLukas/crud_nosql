import db_tools


# returns the entire json document from the db
def read_doc(doc_name: str)-> any:
    your_doc = db_tools.db[doc_name]
    return your_doc

def read_sub_doc(doc_name:str, subsection_name:str)-> any:
    doc = db_tools.db[doc_name][subsection_name]
    return doc

def read_master_data_menu():
    options = ["Students", "Products", "Event", "Address", "Go Back"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("Select an option, q to quit: ")
        if selection == "0":
            doc = read_sub_doc("main_doc", "Student")
        if selection == "1":
            doc = read_sub_doc("main_doc", "Product")
        if selection == "2":
            doc = read_sub_doc("main_doc", "Event")
        if selection == "3":
            doc = read_sub_doc("main_doc", "Address")
        if selection == "4":
            break
        if selection == "q":
            quit()
        for i in doc:
            print(i)


def read_transaction_data_menu():
    options = ["Transactions", "Go Back"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("select an option")
        if selection == "0":
            doc = read_doc("transactions")
        if selection == "1":
            break
        for i in doc:
            print(i)



def read_main_menu():
    options = ["View Master data", "View transaction data", "Main menu"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("Select an option, q to quit: ")
        if selection == "q":
            quit()
        if selection == "0":
            read_master_data_menu()
        if selection == "1":
            read_transaction_data_menu()
        if selection == "2":
            break