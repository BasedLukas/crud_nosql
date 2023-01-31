import db_tools
import templates
import uuid


server = db_tools.server
db = db_tools.db
transactions = db_tools.transactions
main_doc = db_tools.main_doc


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
    if student is None:
        print("Not found")
        return
    def create_student():
        student = templates.Student()
        student.id = str(uuid.uuid1().int)
        student.name = input("Enter student name: ")
        student.email = input("Enter student email: ")
        # TODO Add studies, make it possible to have multiple studies
        student.address = {"street": input("Enter street: "), "house": input("Enter house number: "),
                           "postal_code": input("Enter postal code: ")}
        dict = student.format_dict()
        return dict
    data = create_student()
    edit_list(data, main_doc, "Student", student)

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
            print("not yet available")
        if selection == "1":
            edit_student()
        if selection == "2":
            pass
        if selection == "3":
            pass
        if selection == "4":
            pass
        if selection == "5":
            return
