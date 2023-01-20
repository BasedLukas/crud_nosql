import db_tools

server = db_tools.server
db = db_tools.db
transactions = db_tools.transactions
main_doc = db_tools.main_doc

# sample data to add to db
student = {"name": "Aimee", "email": "Aimee.Stroink@hva.nl", "birth_day": "01-01-2000"}
beer = {"name": "dry martini", "price": "75", "barcode": "bond"}
my_list = [1,2]

# Edit any list index in the doc
def edit_list(data: any,  document:object, doc_location:str, index:int ):
    # sample function call:
    # edit_list(student, main_doc, "students", 1)
    print(document[doc_location][index])
    document[doc_location][index] = data
    print(document[doc_location][index])
    response = db_tools.save_document(document)
    print(response)
    #TODO verify that edit has succeeded

def edit_student():
    name = input("enter the name of the student you wish to edit: ")
    student = db_tools.search_students_by_name(name)
    data = "add a method to edit the data"
    edit_list(data, main_doc, main_doc["students"], 0)

def update_main_menu():
    print("You can edit any of the following data: ")
    options = ["Transactions","Students","Products","Events","Studies", "Go back"]
    for key, value in enumerate(options):
        print(key, value)
    while True:
        selection = input("Select an option: ")
        if selection == "q":
            quit()
        if selection == "0":
            pass
        if selection == "1":
            pass
        if selection == "2":
            pass
        if selection == "3":
            pass
        if selection == "4":
            pass
        if selection == "5":
            return
