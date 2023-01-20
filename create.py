import db_tools
import templates

server = db_tools.server
db = db_tools.db
transactions = db_tools.transactions
main_doc = db_tools.main_doc


# this is an example of how to create a new transaction:
#1) create all the relevant object; address and student
# address = templates.Address("streetname", "housenumber", "postalcode").format_dict()
# student1 = templates.Student("1234", "how many times will this be added", "lukas1234@hva.nl", address).format_dict()
#2) Now you can create a transaction using the objects you created
# transaction1 = templates.Transaction(student1,None,None,3,"datetime" ).format_transaction()
#3) Use the relevant function to add the transaction to the document
# append_to_list(transaction1, transactions,transactions["purchases"])


#Append data into any LIST in the doc
def append_to_list(data: dict,  document:object, doc_location:list ): # the location in the doc must be a list
    doc_location.append(data)
    response = db_tools.save_document(document)
    #TODO verify that write has succeeded (response is: ('main_db', True, '25-60e76bc514caaaa7d0be9de5faa56469'))
    return response


# # Overwrite any LIST in the doc
# def overwrite_list(data: list, document:object, doc_location: str):# doc is couchdb3 object
#     print(document[doc_location])
#     document[doc_location] = data
#     print(document[doc_location])

def create_student():
    student = templates.Student()
    student.id = "id" #TODO add unique ids
    student.name = input("Enter student name: ")
    student.email = input("Enter student email: ")
    #TODO Add studies, make it possible to have multiple studies
    student.address = {"street":input("Enter street: "),"house":input("Enter house number: "),"postal_code":input("Enter postal code: ")}
    dict = student.format_dict()
    print(dict)

def create_master_data():
    options= ["student", "studies", "address", "product", "event", "go back"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("What would you like to create: ")
        if selection == "0":
            create_student()
        if selection == "1":
            pass
            #TODO add this menu option
        if selection =="2":
            pass
            # TODO add this menu option
        if selection == "3":
            pass
            # TODO add this menu option
        if selection == "4":
            pass
            # TODO add this menu option
        if selection == "5":
            return



def create_transaction(student_name:str, event:dict, product_name:str, quantity:int, datetime:str):
    #TODO implement proper way to view and search
    student = db_tools.search_students_by_name(student_name)
    # event = {"key": "value"}
    product = db_tools.search_products_by_name(product_name)
    # quantity = 4
    # datetime = "some date time 1234"
    dict = templates.Transaction(student, event,product, quantity, datetime).format_transaction()
    print(dict)
    db_response = append_to_list(dict, transactions, transactions["purchases"] )
    #TODO verify response


def create_main_menu():
    print("\nHere you can create master data and transactions")
    options = ["Create master data", "Create transaction", "Main menu"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("Select an option, q to quit: ")
        if selection == "q":
            quit()
        if selection == "0":
            create_master_data()
        if selection == "1":
            create_transaction()
        if selection == "2":
            break


