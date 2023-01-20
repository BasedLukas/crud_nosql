import db_tools


# returns the entire json document from the db
def read_doc(doc_name: str)-> any:
    your_doc = db_tools.db[doc_name]
    return your_doc


def read_sub_doc(doc_name:str, subsection_name:str)-> any:
    doc = db_tools.db[doc_name][subsection_name]
    return doc


def read_main_menu():
    options = ["View Master data", "View transaction data", "Main menu"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("Select an option, q to quit: ")
        if selection == "q":
            quit()
        if selection == "0":
            print("master data")
        if selection == "1":
            print("transaction data")
        if selection == "2":
            break