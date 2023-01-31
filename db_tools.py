import requests
import config
import couchdb3

server = couchdb3.Server(config.IP_WITH_AUTH)
db = server['parties']
main_doc = db["main_doc"]
transactions =db["transactions"]

# you can make changes to the document object and then save them using this function
def save_document(document: any):
    reply = db.save(document)
    #TODO verify response
    return reply

#GET request
def get_request(url:str) -> dict:
    data = requests.get(url, auth=(config.USERNAME, config.PASSWORD))
    status_code = data.status_code
    #TODO handle failed or bad requests
    return data.json()


#Post Request
def post_request(url:str, data, headers):
    response = requests.post(url, auth=(config.USERNAME, config.PASSWORD), data=data, headers=headers)
    print(response.json())


# these functions below are used to fetch master data to be used when crafting transactions
def search_students_by_name(name:str)->int:
    #TODO implement proper search
    for key, value in enumerate(main_doc["Student"]):
        print(key,value, value["name"])
        if name.upper().strip() == value["name"].upper().strip():
            return key


def search_products_by_name(name:str)->dict:
    #TODO implement map reduce server side to properly search db, standardize search etc
    for i in main_doc["Product"]:
        if name.upper() == i["name"].upper():
            return i

def search_addresses_by_street(street:str)->dict:
    #TODO implement map reduce server side to properly search db
    for i in main_doc["addresses"]:
        if street.upper() == i["street"].upper():
            return i