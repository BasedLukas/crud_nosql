import db_tools
import templates
import uuid


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
def create_product():
    product = templates.Product()
    product.name = input("Enter product name: ")
    product.price = float(input("enter the product price (Numbers only)"))
    product.barcode = str(uuid.uuid1().int)
    dict = product.format_dict()
    print(dict)
    append_to_list(dict, main_doc, main_doc["Product"])
def create_student():
    student = templates.Student()
    student.id = str(uuid.uuid1().int)
    student.name = input("Enter student name: ")
    student.email = input("Enter student email: ")
    #TODO Add studies, make it possible to have multiple studies
    student.address = {"street":input("Enter street: "),"house":input("Enter house number: "),"postal_code":input("Enter postal code: ")}
    dict = student.format_dict()
    print("The following data has been added", dict)
    x = append_to_list(dict, main_doc,main_doc["Student"])



def create_master_data():
    options= ["student", "studies", "address", "product", "event", "go back"]
    while True:
        for key, value in enumerate(options):
            print(key, value)
        selection = input("What would you like to create: ")
        if selection == "0":
            create_student()
        if selection == "1":
            print("This functionality has not yet been added")
            #TODO add this menu option
        if selection =="2":
            print("This functionality has not yet been added")
            # TODO add this menu option
        if selection == "3":
            create_product()
            # TODO add this menu option
        if selection == "4":
            print("This functionality has not yet been added")
            # TODO add this menu option
        if selection == "5":
            return



def create_transaction():
    #TODO implement proper way to view and search
    student_name = input("enter student name ")
    product_name = input("Enter product name ")
    student_index = db_tools.search_students_by_name(student_name)
    student = main_doc["Student"][student_index]
    event = {"key": "value"}
    product = db_tools.search_products_by_name(product_name)
    quantity = int(input("number purchased "))
    datetime = input("date purchased ")
    dict = templates.Transaction(student, event,product, quantity, datetime).format_transaction()

    db_response = append_to_list(dict, transactions, transactions["purchases"] )
    #TODO verify response

1

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


