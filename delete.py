import db_tools

server = db_tools.server
db = db_tools.db
templates = db_tools.templates
main_doc = db_tools.main_doc


# Edit any list in the doc
def delete_list(document:object, doc_location:str):
    print(document[doc_location])
    document[doc_location] = []
    print(document[doc_location])
    response = db_tools.save_document(document)
    print(response)
    #TODO verify that edit has succeeded

# Edit any list item by index in the doc
def delete_list_index(document:object, doc_location:str, index:int):
    # sample: delete_list_index(main_doc, "events", 3)
    print(document[doc_location])
    document[doc_location].pop(index)
    print(document[doc_location])
    response = db_tools.save_document(document)
    print(response)
    #TODO verify that edit has succeeded

def delete_main_menu():
    print("delete main menu")